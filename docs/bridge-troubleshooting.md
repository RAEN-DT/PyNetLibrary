<!-- SPDX-License-Identifier: MIT -->
<!-- Copyright (c) 2024-2026 RAEN Digital Tools SL - PyNET Platform -->

# Guide: the MCP bridge is not connected — diagnose and reconnect

What to do when the `mcp__pynet-bridge__*` tools are **missing from the session**, or a call to one
fails with a transport error such as:

```
MCP error -32000: Connection closed
```

That error almost never means "the bridge is busy" or "the host is closed". It means the client
**launched the bridge process and it died before completing the MCP handshake** — usually an import
error at startup. The client does not retry, so the tools stay absent for the rest of the session.

> **Do not conclude "the viewer/host is unavailable" and stop.** The viewer and the Autodesk host are
> separate processes and are usually alive and fine. Work the ladder below first.

It also covers the two Python environments in play (bridge vs host) and what to do when a
whitelisted library is **missing inside the host** — a different failure from a dead bridge, and one
that is fixed by installing the package, not by rewriting the script.

Source of truth for the bridge itself: the **`PyNetBridge`** repo (`pynet_mcp/server.py`,
`pyproject.toml`). See [docs/viewer-mcp.md](viewer-mcp.md) for the `viewer_*` tools once connected.

---

## Diagnostic ladder

Run these in order. Each step is cheap and narrows the cause.

### 1. Confirm what is actually running

```powershell
Get-CimInstance Win32_Process -Filter "Name='python.exe' OR Name='pynet-bridge.exe'" |
    Select-Object ProcessId, CreationDate, CommandLine | Format-List
```

The viewer's `pnt_server.py --headless --port <n>` showing up here means the **viewer is healthy** —
it is not the problem. A missing `pynet-bridge` process is expected when the launch crashed.

### 2. Launch the bridge by hand — this is the step that tells you the real error

The MCP client swallows the traceback and reports only `Connection closed`. Running the shim
directly prints it:

```powershell
& "$env:USERPROFILE\.local\bin\pynet-bridge.exe" --version; "exit=$LASTEXITCODE"
```

- `exit=0` → the bridge is fine; the problem is the client's connection (go to step 5).
- A `ModuleNotFoundError` / traceback → go to step 3 or 4 depending on which module is missing.

### 3. `No module named 'pynet_mcp'` — the tool environment is half-built

An interrupted `uv tool install` leaves the launcher shim in place but the environment empty. Check:

```powershell
uv tool list    # "Failed find package `pynet-mcp-bridge` in tool environment" = broken
Get-ChildItem "$env:APPDATA\uv\tools\pynet-mcp-bridge\Lib\site-packages"   # empty = broken
```

Fix: reinstall from the repo (step 6).

### 4. `No module named 'mcp.server.fastmcp'` — a dependency major-bumped

`server.py` imports `from mcp.server.fastmcp import FastMCP, Context`, which exists in **`mcp` 1.x
only** — it was removed in `mcp` 2.0. If `pyproject.toml` leaves `mcp[cli]` unpinned, any reinstall
can silently resolve to 2.x and break every subsequent launch.

The dependency is pinned to `"mcp[cli]>=1.2,<2"`. If you find it unpinned again (e.g. after a merge),
re-pin it before reinstalling — otherwise the fix does not survive the next install. Verify:

```powershell
& "$env:APPDATA\uv\tools\pynet-mcp-bridge\Scripts\python.exe" -c "import mcp.server.fastmcp; print('OK')"
```

### 5. The bridge runs fine but the tools are still absent

The client connects **once, at session start**. A bridge fixed mid-session does not reattach on its
own. **Reload the VS Code window** (or restart the MCP connection), then confirm the
`mcp__pynet-bridge__*` tools are present before continuing.

### 6. Reinstall

```powershell
Get-Process pynet-bridge -ErrorAction SilentlyContinue | Stop-Process -Force -Confirm:$false
uv tool install pynet-mcp-bridge --force   # uv only — never pip (see "The dual-install trap")
```

Killing running processes first is required — they lock the `.exe` shim and the install fails or
half-completes (which is how you get step 3). Then re-run step 2 to verify `exit=0`.

---

## The dual-install trap

`pynet-mcp-bridge` can be installed **twice**: via `pip` (Python 3.10) and via `uv tool`. The real
launcher, `~/.local/bin/pynet-bridge.exe`, runs the **uv** environment — so upgrading the pip copy
alone changes nothing, and `pip show pynet-mcp-bridge` can cheerfully report the right version while
the environment that actually runs is broken.

**Trust `uv tool list` and step 2 over `pip show`.** Confirm which interpreter a running process
uses (`Get-CimInstance Win32_Process`, inspect `CommandLine`) before assuming a reload will fix
anything. Do not edit the copy under `AppData\Roaming\uv\tools\...\site-packages` — it is
overwritten on every `uv tool install`.

---

## Two Python environments — never pip-install into the wrong one

| Interpreter | What runs there | Where |
|---|---|---|
| **The host's CPython 3.10** | every script sent with `send_command` / `send_command_by_path` | embedded in Navisworks / Revit / AutoCAD by pythonnet; ask the host for its `sys.prefix` |
| **The bridge's uv environment** | only the MCP server (`pynet_mcp/server.py`) | `%APPDATA%\uv\tools\pynet-mcp-bridge` |
| **QGIS's own Python** | standalone `04_QGIS` scripts, outside the bridge | installed from the OSGeo4W shell — see [qgis.md](qgis.md) |

`pandas`, `openpyxl`, `matplotlib`, `numpy`, `shapely`, `ifcopenshell` … belong to the **host**
interpreter. Installing them into the uv environment changes nothing for scripts.

## A whitelisted library is missing in the host (`No module named 'pandas'`)

Being on the security whitelist means the validator *lets the import through*, not that the package
is installed. Missing packages are one of the most common script failures. **This is not a dead end
and not a reason to rewrite the script without pandas — install it and re-run.**

1. Ask the running host which interpreter it is (read-only, no confirmation needed):

   ```python
   import sys
   ia_Result = [{"type": "env", "prefix": sys.prefix, "version": sys.version,
                 "site": [p for p in sys.path if "site-packages" in p]}]
   ```

2. Install into **that** interpreter from PowerShell (the one genuine OS fallback, AGENTS.md §9):

   ```powershell
   & "<sys.prefix>\python.exe" -m pip install pandas
   ```

   If `<sys.prefix>` has no `python.exe` (embedded layout), target the site-packages folder reported
   in step 1 instead: `py -3.10 -m pip install --target "<site-packages>" pandas`.

3. Re-run the script. The host interpreter is persistent but `site-packages` is already on
   `sys.path`, so a fresh `import` normally picks the package up with no restart. If it still fails,
   restart the host.

**Rules:**
- Only install packages already on the whitelist ([security.md](security.md)) — the validator rejects
  the import of anything else on the next send, so installing it is wasted work. If a script really
  needs a new package, say so and let the user decide; widening the whitelist is a bridge change.
- Installing is a write on the user's machine: tell the user what you are installing and why before
  running pip.
- If pip fails with a locked-file / permission error while *upgrading* a package the host already
  loaded (typical with `numpy`), close the Autodesk host, install, reopen.

---

## Known incidents

- **2026-08-04 — `mcp` 2.0.0 broke every launch.** A reinstall pulled unpinned `mcp` 2.0.0, which
  removed `mcp.server.fastmcp`; the bridge crashed on import and the client reported
  `-32000: Connection closed`. The failed install also left `site-packages` empty. Fixed by pinning
  `mcp[cli]>=1.2,<2` in `PyNetBridge/pyproject.toml` and reinstalling with `uv tool install . --force`.
  The viewer's `pnt_server` was healthy throughout — the outage was entirely the bridge.
