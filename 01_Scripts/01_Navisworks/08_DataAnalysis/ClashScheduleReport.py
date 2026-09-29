# SPDX-License-Identifier: MIT
# Copyright (c) 2024-2026 RAEN Digital Tools SL - PyNET Platform

"""
Priority report that crosses clash results with the TimeLiner schedule: a clash is "Critico" if
both linked tasks are already built, "Urgente" if one is in progress, "Planificado" otherwise.
See docs/dashboards.md for the HTML/Plotly report pattern this follows.

Project-specific parts that only make sense for THIS building's classification — adapt per
project, same as the ClashDetection skill's test-naming convention (docs/clash-dashboard.md):
- house_of(): splits elements into houses by finding the two largest gaps along Y. Assumes N
  buildings laid out along one axis with no overlap; a different site layout needs a different
  split.
- GROUP_OF_CODE / GROUP_LABEL: maps this project's PYNET_Classification codes (PIL, LOS, FAC, PAR,
  CON, TUB) to TimeLiner task groups. Update both for another project's codes and task names.
"""

import sys
from pathlib import Path
from datetime import date, datetime
import webbrowser
import pandas as pd
import plotly.graph_objects as go
import plotly.offline as pyo

sys.path.append(str(Path.home() / "AppData" / "Roaming" / "Pynet" / "Library" / "01_Scripts" / "00_utils"))
from pynet_clash import get_clash_tests, iter_results

from Autodesk.Navisworks.Api import Application
from Autodesk.Navisworks.Api.Clash import DocumentClash
from Autodesk.Navisworks.Api.Timeliner import DocumentTimeliner
from Raen.Core.Pynet.Resources import CastUtils

doc = Application.ActiveDocument
clashDoc = CastUtils.CastTo[DocumentClash](doc.Clash)
tl = CastUtils.CastTo[DocumentTimeliner](doc.Timeliner)
model = doc.Models[0]

TODAY = date.today()

classified = {}
for item in model.RootItem.Descendants:
    if item.ClassDisplayName != "Tipo":
        continue
    code = None
    for cat in item.PropertyCategories:
        if cat.DisplayName != "Tipo Personalizar":
            continue
        for prop in cat.Properties:
            if prop.DisplayName == "PYNET_Classification":
                try:
                    code = prop.Value.ToDisplayString() or None
                except Exception:
                    pass
    if code:
        classified[hash(item)] = (code, item)

ys, covered = [], set()
for h, (code, type_item) in classified.items():
    for desc in type_item.Descendants:
        if desc.HasGeometry and hash(desc) not in covered:
            covered.add(hash(desc))
            bb = desc.BoundingBox()
            ys.append((bb.Min.Y + bb.Max.Y) / 2.0)
ys.sort()
gaps = sorted(((ys[i + 1] - ys[i], i) for i in range(len(ys) - 1)), reverse=True)
cut1, cut2 = sorted([ys[gaps[0][1]], ys[gaps[1][1]]])


def house_of(y):
    if y <= cut1: return "Casita 1"
    if y <= cut2: return "Casita 2"
    return "Casita 3"


GROUP_OF_CODE = {"PIL": "Estructura", "LOS": "Estructura", "FAC": "Cerramientos", "PAR": "Cerramientos",
                  "CON": "Instalaciones", "TUB": "Instalaciones"}
GROUP_LABEL = {"Estructura": "(PIL+LOS)", "Cerramientos": "(FAC+PAR)", "Instalaciones": "(CON+TUB)"}

task_dates = {t.DisplayName: (t.PlannedStartDate, t.PlannedEndDate) for t in tl.Tasks}


def task_lookup(house, group):
    name = "{} - {} {}".format(house, group, GROUP_LABEL[group])
    return task_dates.get(name), name


def to_date(dt_net):
    return date(dt_net.Year, dt_net.Month, dt_net.Day)


def status_of(s, e):
    if e < TODAY: return "Completada"
    if s <= TODAY <= e: return "En curso"
    return "No iniciada"


TIER_LABEL = {"1-CRITICO": "Critico (ya construido)", "2-URGENTE": "Urgente (en ejecucion)", "3-PLANIFICADO": "Planificado"}
TIER_COLOR = {"1-CRITICO": "#ef4444", "2-URGENTE": "#f97316", "3-PLANIFICADO": "#eab308"}

all_tests = get_clash_tests(clashDoc)

rows = []
for test in all_tests:
    parts = test.DisplayName.split("_vs_")
    if len(parts) != 2:
        continue
    left, right = parts[0].split("_"), parts[1].split("_")
    code_a, code_b = left[-1], right[-1]
    group_a, group_b = GROUP_OF_CODE.get(code_a), GROUP_OF_CODE.get(code_b)
    if not group_a or not group_b:
        continue
    for r in iter_results(test):
        c = r.Center
        house = house_of(c.Y)
        (dates_a, name_a) = task_lookup(house, group_a)
        (dates_b, name_b) = task_lookup(house, group_b)
        if dates_a is None or dates_b is None:
            continue
        sa, ea = to_date(dates_a[0]), to_date(dates_a[1])
        sb, eb = to_date(dates_b[0]), to_date(dates_b[1])
        status_a, status_b = status_of(sa, ea), status_of(sb, eb)
        collision_date = max(sa, sb)
        if status_a == "Completada" and status_b == "Completada":
            tier = "1-CRITICO"
        elif status_a == "En curso" or status_b == "En curso":
            tier = "2-URGENTE"
        else:
            tier = "3-PLANIFICADO"
        rows.append({
            "Prioridad": TIER_LABEL[tier], "_tier": tier, "Casa": house, "Test": test.DisplayName,
            "Fecha colision": collision_date, "Elemento A": r.Item1.DisplayName or "(sin nombre)",
            "Tarea A": name_a, "Estado A": status_a,
            "Elemento B": r.Item2.DisplayName or "(sin nombre)", "Tarea B": name_b, "Estado B": status_b,
            "Distancia (mm)": round(abs(r.Distance) * 1000, 1),
        })

df = pd.DataFrame(rows).sort_values(["_tier", "Fecha colision"]).reset_index(drop=True)

tier_counts = df["_tier"].value_counts().reindex(["1-CRITICO", "2-URGENTE", "3-PLANIFICADO"]).fillna(0).astype(int)
house_tier = df.groupby(["Casa", "_tier"]).size().unstack(fill_value=0)

# --- charts ---
bar = go.Figure()
for tier in ["1-CRITICO", "2-URGENTE", "3-PLANIFICADO"]:
    if tier in house_tier.columns:
        bar.add_trace(go.Bar(name=TIER_LABEL[tier], x=house_tier.index, y=house_tier[tier],
                              marker_color=TIER_COLOR[tier]))
bar.update_layout(barmode="stack", title="Interferencias por casa y prioridad", height=380,
                   plot_bgcolor="white", paper_bgcolor="white")
bar_div = pyo.plot(bar, output_type="div", include_plotlyjs=False)

donut = go.Figure(data=[go.Pie(labels=[TIER_LABEL[t] for t in tier_counts.index], values=tier_counts.values,
                                marker_colors=[TIER_COLOR[t] for t in tier_counts.index], hole=0.55)])
donut.update_layout(title="Distribucion global de prioridad", height=380, paper_bgcolor="white")
donut_div = pyo.plot(donut, output_type="div", include_plotlyjs=False)

plotly_js = pyo.get_plotlyjs()


def kpi_card(label, value, color):
    return '<div class="kpi" style="border-top-color:{c}"><div class="kpi-val">{v}</div><div class="kpi-lbl">{l}</div></div>'.format(c=color, v=value, l=label)


kpis = (
    kpi_card("Total interferencias", len(df), "#334155")
    + kpi_card(TIER_LABEL["1-CRITICO"], int(tier_counts.get("1-CRITICO", 0)), TIER_COLOR["1-CRITICO"])
    + kpi_card(TIER_LABEL["2-URGENTE"], int(tier_counts.get("2-URGENTE", 0)), TIER_COLOR["2-URGENTE"])
    + kpi_card(TIER_LABEL["3-PLANIFICADO"], int(tier_counts.get("3-PLANIFICADO", 0)), TIER_COLOR["3-PLANIFICADO"])
)


def badge(status):
    color = {"Completada": "#334155", "En curso": "#f97316", "No iniciada": "#94a3b8"}.get(status, "#94a3b8")
    return '<span class="badge" style="background:{c}">{s}</span>'.format(c=color, s=status)


rows_html = ""
for _, row in df.iterrows():
    tier_color = TIER_COLOR[row["_tier"]]
    rows_html += (
        '<tr style="border-left:4px solid {tc}">'
        '<td>{prio}</td><td>{casa}</td><td>{test}</td><td>{fecha}</td>'
        '<td>{ea}<br>{ba}<br><small>{ta}</small></td>'
        '<td>{eb}<br>{bb}<br><small>{tb}</small></td>'
        '<td>{dist} mm</td></tr>'
    ).format(tc=tier_color, prio=row["Prioridad"], casa=row["Casa"], test=row["Test"],
              fecha=row["Fecha colision"].isoformat(), ea=row["Elemento A"], ba=badge(row["Estado A"]),
              ta=row["Tarea A"], eb=row["Elemento B"], bb=badge(row["Estado B"]), tb=row["Tarea B"],
              dist=row["Distancia (mm)"])

# The "load" handler forces a Plotly resize once the flex layout below has settled — without it,
# each chart keeps the size it had at the exact moment its inline <script> ran, which can be
# narrower than its final flex column (see docs/dashboards.md).
html = """<!doctype html>
<html lang="es"><head><meta charset="utf-8">
<title>Interferencias priorizadas por planificacion</title>
<script>{plotly_js}</script>
<style>
body {{ font-family: Segoe UI, Arial, sans-serif; margin: 0; background: #f8fafc; color: #0f172a; }}
header {{ background: #0f172a; color: white; padding: 20px 30px; }}
header h1 {{ margin: 0; font-size: 22px; }}
header p {{ margin: 4px 0 0; color: #94a3b8; font-size: 13px; }}
.container {{ padding: 24px 30px; }}
.kpis {{ display: flex; gap: 16px; margin-bottom: 24px; flex-wrap: wrap; }}
.kpi {{ background: white; border-top: 4px solid; border-radius: 8px; padding: 16px 20px; min-width: 160px;
        box-shadow: 0 1px 3px rgba(0,0,0,.08); }}
.kpi-val {{ font-size: 28px; font-weight: 700; }}
.kpi-lbl {{ font-size: 12px; color: #64748b; margin-top: 4px; }}
.charts {{ display: flex; gap: 16px; margin-bottom: 24px; flex-wrap: wrap; }}
.chart-box {{ background: white; border-radius: 8px; padding: 8px; flex: 1; min-width: 380px;
              box-shadow: 0 1px 3px rgba(0,0,0,.08); }}
table {{ width: 100%; border-collapse: collapse; background: white; border-radius: 8px; overflow: hidden;
         box-shadow: 0 1px 3px rgba(0,0,0,.08); }}
th {{ background: #1e293b; color: white; text-align: left; padding: 10px 12px; font-size: 12px; }}
td {{ padding: 10px 12px; font-size: 13px; border-bottom: 1px solid #e2e8f0; vertical-align: top; }}
small {{ color: #64748b; }}
.badge {{ color: white; padding: 2px 8px; border-radius: 10px; font-size: 11px; }}
</style></head>
<body>
<header><h1>Interferencias priorizadas por planificacion</h1>
<p>{doc_title} · fecha de datos {today} · {total} interferencias en {num_tests} clash tests</p></header>
<div class="container">
<div class="kpis">{kpis}</div>
<div class="charts">
  <div class="chart-box">{donut_div}</div>
  <div class="chart-box">{bar_div}</div>
</div>
<table>
<thead><tr><th>Prioridad</th><th>Casa</th><th>Test</th><th>Fecha colision</th>
<th>Elemento A</th><th>Elemento B</th><th>Distancia</th></tr></thead>
<tbody>{rows_html}</tbody>
</table>
</div>
<script>
window.addEventListener('load', function() {{
  document.querySelectorAll('.plotly-graph-div').forEach(function(div) {{ Plotly.Plots.resize(div); }});
}});
</script>
</body></html>""".format(plotly_js=plotly_js, doc_title=doc.Title, today=TODAY.isoformat(), total=len(df),
                          num_tests=len(all_tests), kpis=kpis, donut_div=donut_div, bar_div=bar_div,
                          rows_html=rows_html)

out_dir = Path.home() / "AppData" / "Roaming" / "Pynet" / "Navisworks"
out_dir.mkdir(parents=True, exist_ok=True)
out_path = out_dir / "ClashScheduleReport_{}_{}.html".format(doc.Title.replace(" ", "_"), datetime.now().strftime("%Y%m%d_%H%M%S"))
out_path.write_text(html, encoding="utf-8")
webbrowser.open("file:///" + str(out_path).replace("\\", "/"))

ia_Result = {"type": "ReportResult", "path": str(out_path), "rows": len(df),
             "tier_counts": {TIER_LABEL[k]: int(v) for k, v in tier_counts.items()}}
