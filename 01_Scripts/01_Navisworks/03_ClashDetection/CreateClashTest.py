# SPDX-License-Identifier: MIT
# Copyright (c) 2024-2026 RAEN Digital Tools SL - PyNET Platform

#region references

import clr
import sys
from pathlib import Path

clr.AddReference("Autodesk.Navisworks.Api")
from Autodesk.Navisworks.Api import Application

clr.AddReference("Autodesk.Navisworks.Clash")
from Autodesk.Navisworks.Api.Clash import DocumentClash, ClashTest, ClashTestType

bundlePath = (
    Path.home()
    / "AppData" / "Roaming" / "Autodesk" / "ApplicationPlugins"
    / "RAEN.Navisworks.PyNET.bundle" / "Contents" / "2027"
)
sys.path.append(str(bundlePath))
clr.AddReference("Raen.Core.Pynet.Resources")
from Raen.Core.Pynet.Resources import CastUtils  # type: ignore

doc = Application.ActiveDocument

sys.path.append(str(Path.home() / "AppData" / "Roaming" / "Pynet" / "Library" / "01_Scripts" / "00_utils"))
from pynet_clash import get_clash_tests #type:ignore

#endregion


# ─── Configuration ────────────────────────────────────────────────────────────
#
# The test references two existing SearchSets by DisplayName — SearchSets must
# already exist (see 02_SearchSets/GenerateSearchSets.py) and stay dynamic:
# never build a test from a static CopyFrom(FindAll(...)) snapshot.

SET_A_NAME = "FAC"
SET_B_NAME = "PIL"
TEST_NAME = f"{SET_A_NAME} vs {SET_B_NAME}"
TOLERANCE_MM = 10.0
TEST_TYPE = ClashTestType.Hard  # Hard | Clearance | Duplicate

# ─── Helpers ──────────────────────────────────────────────────────────────────

MM_TO_FEET = 1 / (0.3048 * 1000)


def find_set(root, name):
    """Walk the SelectionSets tree (folders included) looking for `name`."""
    for item in root.Children:
        if item.DisplayName == name:
            return item
        if item.IsGroup:
            found = find_set(item, name)
            if found:
                return found
    return None


class ClashTestBuilder:
    """
    Creates a new ClashTest referencing two existing SearchSets by name.
    """

    @staticmethod
    def RunTests(document):
        clash_doc = CastUtils.CastTo[DocumentClash](document.Clash)
        tests_data = clash_doc.TestsData

        tests_data.TestsRunAllTests()


    @staticmethod
    def Create(document, set_a_name, set_b_name, test_name, tolerance_mm, test_type):
        item_a = find_set(document.SelectionSets.RootItem, set_a_name)
        item_b = find_set(document.SelectionSets.RootItem, set_b_name)

        if item_a is None:
            raise ValueError(f"SearchSet not found: '{set_a_name}'")
        if item_b is None:
            raise ValueError(f"SearchSet not found: '{set_b_name}'")

        source_a = document.SelectionSets.CreateSelectionSource(item_a)
        source_b = document.SelectionSets.CreateSelectionSource(item_b)

        clash_doc = CastUtils.CastTo[DocumentClash](document.Clash)
        tests_data = clash_doc.TestsData

        # Skip if a test with the same name already exists — avoid duplicates
        # on repeated runs.
        existing = next((t for t in get_clash_tests(clash_doc) if t.DisplayName == test_name), None)
        if existing is not None:
            print(f"Test '{test_name}' already exists — skipping.")
            return {"test": test_name, "status": "SKIPPED — already exists"}

        test = ClashTest()
        test.DisplayName = test_name
        test.TestType = test_type
        test.Tolerance = tolerance_mm * MM_TO_FEET
        test.SelectionA.Selection.SelectionSources.Add(source_a)
        test.SelectionB.Selection.SelectionSources.Add(source_b)

        tests_data.TestsAddCopy(None, test)  # None = root level

        print(f"Created '{test_name}' ({set_a_name} vs {set_b_name}) @ {tolerance_mm} mm")
        return {"test": test_name, "status": "OK", "tolerance_mm": tolerance_mm}


# ─── Entry point ──────────────────────────────────────────────────────────────

class FeatureManager:

    @staticmethod
    def Run(document):
        result = ClashTestBuilder.Create(
            document, SET_A_NAME, SET_B_NAME, TEST_NAME, TOLERANCE_MM, TEST_TYPE
        )

        ClashTestBuilder.RunTests(document)


        return result


ia_Result = FeatureManager.Run(doc)

