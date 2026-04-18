"""HTML export."""
from __future__ import annotations
from pathlib import Path
from lynx_mining.models import AnalysisReport

def export_html(report: AnalysisReport, output_path: Path) -> Path:
    from lynx_mining.core.conclusion import generate_conclusion
    p, c = report.profile, generate_conclusion(report)
    vc = c.verdict.lower().replace(" ", "-")
    html = f"""<!DOCTYPE html><html><head><meta charset="UTF-8"><title>{p.name}</title>
<style>body{{font-family:sans-serif;max-width:900px;margin:0 auto;padding:20px;background:#1e1e2e;color:#cdd6f4}}
h1{{color:#89b4fa}}h2{{color:#a6e3a1}}table{{width:100%;border-collapse:collapse}}
th,td{{padding:8px;text-align:left;border-bottom:1px solid #45475a}}th{{background:#313244;color:#cba6f7}}
.verdict{{font-size:1.5em;padding:15px;border-radius:8px;text-align:center;margin:20px 0}}
.s{{color:#a6e3a1}}.r{{color:#f38ba8}}.meta{{color:#6c7086;font-size:0.9em}}</style></head>
<body><h1>{p.name} ({p.ticker})</h1>
<p class="meta">Tier: {p.tier.value} | Stage: {p.stage.value} | Commodity: {p.primary_commodity.value} | Jurisdiction: {p.jurisdiction_tier.value}</p>
<div class="verdict"><strong>{c.verdict}</strong> — {c.overall_score:.0f}/100</div><p>{c.summary}</p><p class="meta">{c.stage_note}</p>"""
    if c.strengths or c.risks:
        html += "<h2>Signals</h2><table><tr><th>Strengths</th><th>Risks</th></tr>"
        for i in range(max(len(c.strengths), len(c.risks))):
            s = c.strengths[i] if i < len(c.strengths) else ""; r = c.risks[i] if i < len(c.risks) else ""
            html += f'<tr><td class="s">{s}</td><td class="r">{r}</td></tr>'
        html += "</table>"
    html += f'<hr><p class="meta">Generated: {report.fetched_at}<br>Lynx Basic Materials (Lince Investor Suite)</p></body></html>'
    output_path.write_text(html, encoding="utf-8"); return output_path
