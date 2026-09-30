<!-- SPDX-License-Identifier: MIT -->
<!-- Copyright (c) 2024-2026 RAEN Digital Tools SL - PyNET Platform -->

# Guide: editing external DWG files (AutoCAD / Civil 3D)

Read [autocad-civil.md](autocad-civil.md) first — boilerplate, write pattern and the three API misuses that abort the host apply here too.

---

Two validated patterns — choose based on whether the file should appear in the UI.

### Pattern A — Background (file never opens in UI)

```python
from Autodesk.AutoCAD.DatabaseServices import Database, FileOpenMode, DwgVersion

db = Database(False, True)
db.ReadDwgFile(str(file_path), FileOpenMode.OpenForReadAndAllShare, False, "")
try:
    t = db.TransactionManager.StartTransaction()
    try:
        # ... modifications ...
        t.Commit()
    except:
        t.Abort()
        raise
    # 4-arg SaveAs required — 2-arg fails on databases opened via ReadDwgFile
    db.SaveAs(str(file_path), False, DwgVersion.Current, None)
finally:
    db.Dispose()  # always — releases file handle, no stale .dwl files
```

- Use `OpenForReadAndAllShare` (not `OpenForReadAndWriteNoShare`) — an exclusive lock prevents `SaveAs` overwriting the same path.
- `db.Save()` and 2-arg `db.SaveAs(path, version)` both fail on `ReadDwgFile` databases inside the host. Always use 4-arg `SaveAs(path, bakAndRename, version, None)`.
- `db.Dispose()` in `finally` — omitting it on exception leaves a stale `.dwl` lock file.

### Pattern B — UI (file opens as a tab, stays open)

```python
from Autodesk.AutoCAD.ApplicationServices import Application as AcadApp, DocumentCollectionExtension

# DocumentCollectionExtension.Open is a static extension method — call as static
file_doc = DocumentCollectionExtension.Open(AcadApp.DocumentManager, str(file_path), True, "")
db = file_doc.Database

file_doc.UpgradeDocOpen()       # upgrade read-only -> read-write
lock = file_doc.LockDocument()  # required for write access in transactions
try:
    t = db.TransactionManager.StartTransaction()
    try:
        # ... modifications ...
        t.Commit()
    except:
        t.Abort()
        raise
finally:
    lock.Dispose()

# QSAVE saves through the document system — clears the asterisk in the UI tab
file_doc.SendStringToExecute("_.QSAVE ", True, False, False)
# Document stays open — do NOT close it; user sees it in the UI
```

- `DocumentCollectionExtension.Open` is a **static extension method**, not an instance method on `DocumentCollection`.
- Open with `forReadOnly=True` — opening with `False` then calling `UpgradeDocOpen()` throws `eWasOpenForWrite`.
- `LockDocument()` is still required after `UpgradeDocOpen()` — transactions throw `eLockViolation` without it.
- `lock.Dispose()` in `finally`, not `lock.Close()` — `LockDocument()` returns a `DocumentLock`.
- Save with `SendStringToExecute("_.QSAVE ")`, **not** `db.SaveAs()` — `SaveAs` leaves the modified asterisk on a document database.

### Reference scripts

- `01_Scripts/03_AutoCAD/04_WinForms/EditDwg_Background.py` — Pattern A, end-to-end with WinForms.
- `01_Scripts/03_AutoCAD/04_WinForms/EditDwg_WithUI.py` — Pattern B, end-to-end with WinForms.
