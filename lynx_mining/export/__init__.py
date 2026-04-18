"""Export package for mining analysis reports."""

from __future__ import annotations
from enum import Enum
from pathlib import Path
from typing import Optional
from lynx_mining.models import AnalysisReport

class ExportFormat(str, Enum):
    TXT = "txt"; HTML = "html"; PDF = "pdf"

def export_report(report: AnalysisReport, fmt: ExportFormat, output_path: Optional[Path] = None) -> Path:
    from lynx_mining.core.storage import get_company_dir
    from datetime import datetime
    if output_path is None:
        output_path = get_company_dir(report.profile.ticker) / f"report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.{fmt.value}"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    if fmt == ExportFormat.TXT:
        from lynx_mining.export.txt_export import export_txt; return export_txt(report, output_path)
    elif fmt == ExportFormat.HTML:
        from lynx_mining.export.html_export import export_html; return export_html(report, output_path)
    elif fmt == ExportFormat.PDF:
        from lynx_mining.export.pdf_export import export_pdf; return export_pdf(report, output_path)
    raise ValueError(f"Unknown format: {fmt}")
