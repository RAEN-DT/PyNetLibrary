# SPDX-License-Identifier: MIT
# Copyright (c) 2024-2026 RAEN Digital Tools SL - PyNET Platform

import clr

clr.AddReference("RhinoCommon")

from Rhino import RhinoDoc

# The host injects the active document as __rhinodoc__
try:
    doc = __rhinodoc__
except NameError:
    doc = RhinoDoc.ActiveDoc

# Rhino layouts are page views; model space is shown in the standard views
layouts = []
for page in doc.Views.GetPageViews():
    layouts.append(
        {
            "type": "Layout",
            "name": page.PageName,
            "page_number": page.PageNumber,
            "width": page.PageWidth,  # page units
            "height": page.PageHeight,
            "details": len(page.GetDetailViews()),
        }
    )
model_views = doc.Views.GetStandardRhinoViews()

layouts = sorted(layouts, key=lambda l: l["page_number"])
print(f"Found {len(layouts)} layouts ({len(model_views)} model views)")
for l in layouts:
    print(f"  [{l['page_number']}] {l['name']} ({l['width']} x {l['height']}, {l['details']} details)")

ia_Result = layouts
