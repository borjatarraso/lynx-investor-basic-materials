"""Plain text export."""
from __future__ import annotations
from pathlib import Path
from lynx_mining.models import AnalysisReport

def export_txt(report: AnalysisReport, output_path: Path) -> Path:
    p = report.profile; lines = []
    lines.append("=" * 70); lines.append(f"LYNX Basic Materials — {p.name} ({p.ticker})")
    lines.append(f"Tier: {p.tier.value} | Stage: {p.stage.value} | Commodity: {p.primary_commodity.value}")
    lines.append("=" * 70); lines.append("")
    if report.solvency:
        s = report.solvency; lines.append("SOLVENCY"); lines.append("-" * 30)
        lines.append(f"  Cash Runway: {s.cash_runway_years:.1f} years" if s.cash_runway_years else "  Cash Runway: N/A")
        lines.append(f"  Total Cash: ${s.total_cash/1e6:,.1f}M" if s.total_cash else "  Total Cash: N/A"); lines.append("")
    if report.share_structure:
        ss = report.share_structure; lines.append("SHARE STRUCTURE"); lines.append("-" * 30)
        lines.append(f"  Assessment: {ss.share_structure_assessment or 'N/A'}")
        lines.append(f"  Insider: {ss.insider_ownership_pct*100:.1f}%" if ss.insider_ownership_pct else "  Insider: N/A"); lines.append("")
    from lynx_mining.core.conclusion import generate_conclusion
    c = generate_conclusion(report); lines.append("CONCLUSION"); lines.append("=" * 30)
    lines.append(f"  {c.verdict} — {c.overall_score:.0f}/100"); lines.append(f"  {c.summary}")
    lines.append(f"\nGenerated: {report.fetched_at}")
    output_path.write_text("\n".join(lines), encoding="utf-8"); return output_path
