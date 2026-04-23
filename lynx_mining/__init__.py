"""Lynx Basic Materials — Fundamental analysis for junior mining & basic materials companies."""

from pathlib import Path

# Suite-level constants come from lynx-investor-core (shared across every agent).
from lynx_investor_core import (
    LICENSE_NAME,
    LICENSE_TEXT,
    LICENSE_URL,
    SUITE_LABEL,
    SUITE_NAME,
    SUITE_VERSION,
    __author__,
    __author_email__,
    __license__,
    __year__,
)
from lynx_investor_core import storage as _core_storage

# Initialize the shared storage layer with this agent's project root so
# data/ and data_test/ live beside *this* package.
_core_storage.set_base_dir(Path(__file__).resolve().parent.parent)

# ---------------------------------------------------------------------------
# Agent-specific identity
# ---------------------------------------------------------------------------

__version__ = "4.0.1"  # lynx-investor-basic-materials version (independent of core)

APP_NAME = "Lynx Basic Materials Analysis"
APP_SHORT_NAME = "Basic Materials Analysis"
APP_TAGLINE = "Junior Mining & Basic Materials"
APP_SCOPE = "basic materials and commodities"
PROG_NAME = "lynx-mining"
PACKAGE_NAME = "lynx_mining"
USER_AGENT_PRODUCT = "LynxMining"
NEWS_SECTOR_KEYWORD = "mining stock"

TICKER_SUGGESTIONS = (
    "  - For TSXV stocks, try: OCO.V, FUU.V",
    "  - For TSX stocks, try: DML.TO, NXE.TO",
    "  - For US stocks, try: UUUU, EFR",
    "  - You can also type the full company name: 'Denison Mines'",
)

DESCRIPTION = (
    "Fundamental analysis specialized for junior mining, uranium, "
    "copper, gold, and basic materials companies. Evaluates companies "
    "across all stages from grassroots exploration to production using "
    "mining-specific metrics: EV/resource, P/NAV, AISC, cash runway, "
    "share structure analysis, jurisdiction risk, and more.\n\n"
    "Part of the Lince Investor Suite."
)

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _load_logo_ascii() -> str:
    """Load the ASCII logo from img/logo_ascii.txt."""
    from lynx_investor_core.logo import load_logo_ascii
    return load_logo_ascii(Path(__file__).resolve().parent)


def get_about_text() -> dict:
    """Return structured about information (uniform across agents)."""
    from lynx_investor_core.about import AgentMeta, build_about
    meta = AgentMeta(
        app_name=APP_NAME,
        short_name=APP_SHORT_NAME,
        tagline=APP_TAGLINE,
        package_name=PACKAGE_NAME,
        prog_name=PROG_NAME,
        version=__version__,
        description=DESCRIPTION,
        scope_description=APP_SCOPE,
    )
    return build_about(meta, logo_ascii=_load_logo_ascii())
