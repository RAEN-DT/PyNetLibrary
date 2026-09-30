<!-- SPDX-License-Identifier: MIT -->
<!-- Copyright (c) 2024-2026 RAEN Digital Tools SL - PyNET Platform -->

# Guide: install (or repair) the MCP bridge — agent procedure

Follow this when the user asks to install or reinstall the PyNET bridge, or when
[bridge-troubleshooting.md](bridge-troubleshooting.md) sends you here. It is the **only** supported
install path: **uv**, one tool environment, one launcher. Run each step yourself from PowerShell and
check its result before moving on.

> **Never install the bridge with `pip`.** A pip copy lives in a different interpreter from the uv
> launcher, `pip show` then reports a version that is not the one running, and the two drift apart
> (see "The dual-install trap" in [bridge-troubleshooting.md](bridge-troubleshooting.md)). If uv is
> missing, install uv — do not fall back to pip.

Installing software is a write on the user's machine: say in one line what you are about to install
before step 2 and step 3.

---

## 1. Check what is already there (read-only)

```powershell
Get-Command uv, pynet-bridge -ErrorAction SilentlyContinue | Select-Object Name, Source
uv tool list 2>$null
py -0p 2>$null          # installed Pythons (the bridge needs 3.10+)
```

- `pynet-bridge` resolves **and** `uv tool list` shows `pynet-mcp-bridge` → already installed; go to
  step 4 to verify it, and only reinstall if step 4 fails.
- `pip show pynet-mcp-bridge` finds a copy → there is a pip install to remove (step 5).

## 2. Install uv (only if `uv` is missing)

```powershell
powershell -ExecutionPolicy Bypass -c "irm https://astral.sh/uv/install.ps1 | iex"
$env:Path = [Environment]::GetEnvironmentVariable("Path","User") + ";" + [Environment]::GetEnvironmentVariable("Path","Machine")
uv --version
```

uv does not need a system Python: if `py -0p` found no 3.10+, add `--python 3.12` in step 3 and uv
downloads a private interpreter for the tool.

## 3. Install the bridge

Stop any running bridge first — a live process locks `pynet-bridge.exe` and leaves a half-built
environment:

```powershell
Get-Process pynet-bridge, pynet-mcp-bridge -ErrorAction SilentlyContinue | Stop-Process -Force -Confirm:$false
uv tool install pynet-mcp-bridge --force --with "mcp[cli]>=1.2,<2"
```

**Keep `--with "mcp[cli]>=1.2,<2"`.** Bridge 1.5.4 and older declare `mcp[cli]` without an upper
bound, so a fresh resolve picks `mcp` 2.x, which removed `mcp.server.fastmcp` — the bridge then dies
on import (`MCP error -32000: Connection closed`). 1.5.5 ships the pin itself; the flag is harmless
there and still protects any install that ends up on an older release.

From a local checkout of the `PyNetBridge` repo instead of PyPI (development):
`uv tool install . --force --with "mcp[cli]>=1.2,<2"` run inside that folder.

## 4. Verify — mandatory

```powershell
& "$env:USERPROFILE\.local\bin\pynet-bridge.exe" --version; "exit=$LASTEXITCODE"
& "$env:APPDATA\uv\tools\pynet-mcp-bridge\Scripts\python.exe" -c "import mcp.server.fastmcp, importlib.metadata as m; print('mcp', m.version('mcp'))"
```

Both must succeed and `mcp` must be `1.x`. `--version` exits immediately: it is the only way this
guide ever runs the bridge by hand (see the rule below).

## 5. Remove a pip copy (only if step 1 found one)

```powershell
py -m pip uninstall -y pynet-mcp-bridge
```

Repeat for each interpreter that has it (`py -0p` lists them). Then re-run step 4.

## 6. Register the bridge in the AI client

Every client launches the bridge itself over stdio from its config — the command is the absolute
path of `pynet-bridge.exe` (`(Get-Command pynet-bridge).Source`, normally
`%USERPROFILE%\.local\bin\pynet-bridge.exe`), no arguments.

| Client | File | Entry |
|---|---|---|
| Claude Code | `%USERPROFILE%\.claude.json` → `mcpServers` | `"pynet-bridge": {"type":"stdio","command":"<path>","args":[]}` |
| Claude Desktop | `%APPDATA%\Claude\claude_desktop_config.json` → `mcpServers` | same as Claude Code |
| Codex | `%USERPROFILE%\.codex\config.toml` | `[mcp_servers.pynet-bridge]` / `command = "<path>"` / `args = []` |
| GitHub Copilot (VS Code) | `%APPDATA%\Code\User\mcp.json` → `servers` | same JSON entry |

Use forward slashes or escaped backslashes in the path. Edit only the `pynet-bridge` entry — leave
every other server in the file untouched. Read the file before writing it.

## 7. Reconnect

The client reads its MCP config **once, at session start**. Tell the user the one action needed:
reload the VS Code window (Claude Code / Copilot) or restart Codex / Claude Desktop. After that,
confirm the `pynet-bridge` tools are listed and call `list_active_instances` as the smoke test.

---

## Rule: the bridge is reached only through the client's MCP tools

**Never start the bridge as a separate process to talk to it** — no `pynet-bridge` launched in a
background terminal, no hand-written stdio / JSON-RPC client, no script that imports `pynet_mcp` and
calls its functions, no second server "just to get the tools working". The client already owns one
bridge process; a second one fights it for the host connection and leaves orphan processes, and
nothing it returns is visible to the session as MCP tools.

If the tools are missing, the fix is always the client connection: steps 4 → 6 → 7 here, or the
diagnostic ladder in [bridge-troubleshooting.md](bridge-troubleshooting.md). Running
`pynet-bridge.exe --version` to read a startup error is allowed; anything that keeps the bridge
running outside the client is not.
