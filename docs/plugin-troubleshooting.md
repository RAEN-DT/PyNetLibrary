<!-- SPDX-License-Identifier: MIT -->
<!-- Copyright (c) 2024-2026 RAEN Digital Tools SL - PyNET Platform -->

# Guide: the PyNET ribbon does not appear in the host

What to do when PyNET is installed but its tab / panel is missing in Revit (and, by analogy,
Navisworks or AutoCAD), usually with **no error dialog at all**. This is a host start-up problem, not
a bridge problem — for missing `mcp__pynet-bridge__*` tools see
[bridge-troubleshooting.md](bridge-troubleshooting.md).

> **Key lesson: another vendor's add-in can stop PyNET from loading.** Revit starts third-party
> add-ins one after another in a single chain. If one of them breaks that chain, every add-in queued
> after it silently never starts — PyNET included — and Revit shows nothing. Always check the
> start-up order before suspecting the PyNET build.

---

## 1. Rule out the quick causes

- **Add-ins Manager** (Revit 2026+, *Manage → Add-ins Manager*): PyNET must be ticked and
  *Disable all third-party add-ins* unticked. The same state lives in
  `%APPDATA%\Autodesk\Revit\Autodesk Revit <year>\AddinsData\AddInsSettings.json`
  (`"Disabled": false` for GUID `655c109a-2852-47b0-b8b2-983ffc1a8093`, `"DisableAllAddIns": false`).
- **PyNET's own log**: `%APPDATA%\Raen\Pynet\error.log`. Any exception during PyNET's start-up is
  written there with its stack trace even when no dialog is shown. An empty/missing log plus a
  missing ribbon means PyNET's code **never ran** — go to step 2.
- **Installed files**: `%APPDATA%\Autodesk\ApplicationPlugins\Raen.Revit.Pynet.bundle\Contents\<year>\`
  must contain `Raen.Revit.PyNet.<year>.dll` and `Raen.Revit.PyNet.addin`.

## 2. Read the right journal

`%LOCALAPPDATA%\Autodesk\Revit\Autodesk Revit <year>\Journals\` — take the newest
**`journal.NNNN.txt`**, from a session where the ribbon was missing, with Revit closed.

> **Ignore `journal.NNNN.worker1.log`.** Revit 2027 runs a UI-less *RevitWorker* process that only
> loads DB applications; PyNET (a UI application) is never started there, so its absence in that file
> means nothing. Its header says `UI-less InitNativeInstance`.

Pasting a whole journal into a chat truncates it (~50k characters) before the add-in section. Ask for
the file saved to disk and read it yourself, or have the user extract the relevant lines:

```powershell
$j = "$env:LOCALAPPDATA\Autodesk\Revit\Autodesk Revit 2027\Journals\journal.0034.txt"
Select-String -Path $j -Pattern 'Starting External Application|655c109a|API_ERROR|AddInManifest.*PyNET' |
  Out-File "$env:USERPROFILE\Desktop\pynet_journal.txt" -Encoding utf8
```

## 3. Interpret it

| Journal shows | Meaning |
|---|---|
| no `Raen.Revit.Pynet.bundle ... was registered` line | Revit never found the bundle — install path / `PackageContents.xml` |
| registered, then `Starting External Application: PyNET Platform` + `Added pushbutton` lines | PyNET loaded; the problem is elsewhere (UI layout, licence window) |
| registered, but **no** `Starting External Application: PyNET Platform` | PyNET was never started — find where the chain stopped (below) |
| `API_ERROR ... Assembly version conflict ... RevitAPI of version 27.0.x conflicts with ... 27.2` | a warning about an add-in shipping its own copy of the Revit API; not fatal on its own |

In the `[Jrn.AddInManifest]` summary near the end, the number after `AddInLoadFailureMessage: NoError`
is the start-up time. **`0.000000` means the add-in never started**; a healthy PyNET shows ~1–2 s.

**Find where the chain stopped:** list the `Starting External Application` lines in order. Third-party
add-ins start after Autodesk's, in manifest-name order. The last third-party add-in that started is
the prime suspect; every add-in after it will show `0.000000`. If Autodesk's own *File exporter for
Navisworks* is among those that never started, the cause is certainly not PyNET.

## 4. Confirm by disabling

In the Add-ins Manager, untick the suspect, restart Revit, and check that **all** the add-ins that were
missing come back (not only PyNET). If it is not obvious which add-in is at fault, bisect: disable
half of the third-party add-ins, restart, repeat.

Tell the user which add-in blocks the others so they can report it to its vendor. If they cannot do
without it, a possible workaround is to make PyNET start earlier in the chain (a manifest name that
sorts before the offender) — untested, offer it only as a last resort.

---

## Known incidents

- **2026-09-28 — Revit 2027.2, NonicaTab FREE + PRO installed together.** The ribbon was missing with
  no error on 2027 while 2025 was fine. The journal showed start-up stopping right after
  *NonicaTab PRO Loader*: Editeca MCP, Chaos Veras, Autodesk's Navisworks exporter and PyNET all
  logged `0.000000`. Disabling NonicaTab in the Add-ins Manager restored them. Red herrings along the
  way: the worker journal (no UI add-ins by design) and the Revit version difference.
