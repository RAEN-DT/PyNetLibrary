# SPDX-License-Identifier: MIT
# Copyright (c) 2024-2026 RAEN Digital Tools SL - PyNET Platform

import clr
import sys
from pathlib import Path

clr.AddReference("Autodesk.Navisworks.Api")
from Autodesk.Navisworks.Api import Application

# PyNET bundle folder of the RUNNING Navisworks (right year, never hardcoded): the folder
# of the engine assembly executing this script. See docs/navisworks.md "CastUtils".
from System import AppDomain
bundlePath = Path(next(a for a in AppDomain.CurrentDomain.GetAssemblies()
               if a.GetName().Name == "Raen.Core.Pynet.Engine").Location).parent
sys.path.append(str(bundlePath))

doc = Application.ActiveDocument


class NwcSourceInspector:
    @staticmethod
    def Run(document):
        results = []
        for model in document.Models:
            source = NwcSourceInspector.GetSourceFile(model.RootItem)
            nwc_name = Path(model.FileName).name if model.FileName else "(unknown)"
            results.append({"nwc": nwc_name, "source_rvt": source})
            print(f"{nwc_name}  →  {source or '(not found)'}")
        return results

    @staticmethod
    def GetSourceFile(root_item):
        # Sample the first descendant that has the "Elemento" category with "Archivo de origen"
        for item in root_item.Descendants:
            for cat in item.PropertyCategories:
                if cat.DisplayName == "Elemento":
                    for prop in cat.Properties:
                        if prop.DisplayName == "Archivo de origen":
                            try:
                                val = prop.Value.ToDisplayString()
                                if val:
                                    return val
                            except:
                                pass
        return None


ia_Result = NwcSourceInspector.Run(doc)
