"""Data models for Lynx Basic Materials — mining-focused fundamental analysis."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Optional


# ---------------------------------------------------------------------------
# Company tier classification (market cap based)
# ---------------------------------------------------------------------------

class CompanyTier(str, Enum):
    MEGA = "Mega Cap"
    LARGE = "Large Cap"
    MID = "Mid Cap"
    SMALL = "Small Cap"
    MICRO = "Micro Cap"
    NANO = "Nano Cap"


def classify_tier(market_cap: Optional[float]) -> CompanyTier:
    if market_cap is None or market_cap <= 0:
        return CompanyTier.NANO
    if market_cap >= 200_000_000_000:
        return CompanyTier.MEGA
    if market_cap >= 10_000_000_000:
        return CompanyTier.LARGE
    if market_cap >= 2_000_000_000:
        return CompanyTier.MID
    if market_cap >= 300_000_000:
        return CompanyTier.SMALL
    if market_cap >= 50_000_000:
        return CompanyTier.MICRO
    return CompanyTier.NANO


# ---------------------------------------------------------------------------
# Mining company stage classification
# ---------------------------------------------------------------------------

class CompanyStage(str, Enum):
    GRASSROOTS = "Grassroots Explorer"
    EXPLORER = "Advanced Explorer"
    DEVELOPER = "Developer"
    PRODUCER = "Producer"
    ROYALTY = "Royalty/Streaming"


class Commodity(str, Enum):
    GOLD = "Gold"
    SILVER = "Silver"
    COPPER = "Copper"
    URANIUM = "Uranium"
    LITHIUM = "Lithium"
    NICKEL = "Nickel"
    ZINC = "Zinc"
    RARE_EARTHS = "Rare Earths"
    OTHER = "Other"


class JurisdictionTier(str, Enum):
    TIER_1 = "Tier 1 — Low Risk"
    TIER_2 = "Tier 2 — Moderate Risk"
    TIER_3 = "Tier 3 — High Risk"
    UNKNOWN = "Unknown"


class Relevance(str, Enum):
    CRITICAL = "critical"
    RELEVANT = "relevant"
    CONTEXTUAL = "contextual"
    IRRELEVANT = "irrelevant"


# ---------------------------------------------------------------------------
# Core data models
# ---------------------------------------------------------------------------

@dataclass
class CompanyProfile:
    ticker: str
    name: str
    isin: Optional[str] = None
    sector: Optional[str] = None
    industry: Optional[str] = None
    country: Optional[str] = None
    exchange: Optional[str] = None
    currency: Optional[str] = None
    market_cap: Optional[float] = None
    description: Optional[str] = None
    website: Optional[str] = None
    employees: Optional[int] = None
    tier: CompanyTier = CompanyTier.NANO
    stage: CompanyStage = CompanyStage.GRASSROOTS
    primary_commodity: Commodity = Commodity.OTHER
    jurisdiction_tier: JurisdictionTier = JurisdictionTier.UNKNOWN
    jurisdiction_country: Optional[str] = None


@dataclass
class ValuationMetrics:
    pe_trailing: Optional[float] = None
    pe_forward: Optional[float] = None
    pb_ratio: Optional[float] = None
    ps_ratio: Optional[float] = None
    p_fcf: Optional[float] = None
    ev_ebitda: Optional[float] = None
    ev_revenue: Optional[float] = None
    peg_ratio: Optional[float] = None
    dividend_yield: Optional[float] = None
    earnings_yield: Optional[float] = None
    enterprise_value: Optional[float] = None
    market_cap: Optional[float] = None
    price_to_tangible_book: Optional[float] = None
    price_to_ncav: Optional[float] = None
    ev_per_resource_oz: Optional[float] = None
    ev_per_resource_lb: Optional[float] = None
    p_nav: Optional[float] = None
    cash_to_market_cap: Optional[float] = None
    nav_per_share: Optional[float] = None


@dataclass
class ProfitabilityMetrics:
    roe: Optional[float] = None
    roa: Optional[float] = None
    roic: Optional[float] = None
    gross_margin: Optional[float] = None
    operating_margin: Optional[float] = None
    net_margin: Optional[float] = None
    fcf_margin: Optional[float] = None
    ebitda_margin: Optional[float] = None
    aisc_per_unit: Optional[float] = None
    aisc_unit: str = "oz"
    cash_cost_per_unit: Optional[float] = None
    aisc_margin: Optional[float] = None


@dataclass
class SolvencyMetrics:
    debt_to_equity: Optional[float] = None
    debt_to_ebitda: Optional[float] = None
    current_ratio: Optional[float] = None
    quick_ratio: Optional[float] = None
    interest_coverage: Optional[float] = None
    altman_z_score: Optional[float] = None
    net_debt: Optional[float] = None
    total_debt: Optional[float] = None
    total_cash: Optional[float] = None
    cash_burn_rate: Optional[float] = None
    cash_runway_years: Optional[float] = None
    working_capital: Optional[float] = None
    cash_per_share: Optional[float] = None
    tangible_book_value: Optional[float] = None
    ncav: Optional[float] = None
    ncav_per_share: Optional[float] = None
    quarterly_burn_rate: Optional[float] = None
    burn_as_pct_of_market_cap: Optional[float] = None


@dataclass
class GrowthMetrics:
    revenue_growth_yoy: Optional[float] = None
    revenue_cagr_3y: Optional[float] = None
    revenue_cagr_5y: Optional[float] = None
    earnings_growth_yoy: Optional[float] = None
    earnings_cagr_3y: Optional[float] = None
    earnings_cagr_5y: Optional[float] = None
    fcf_growth_yoy: Optional[float] = None
    book_value_growth_yoy: Optional[float] = None
    dividend_growth_5y: Optional[float] = None
    shares_growth_yoy: Optional[float] = None
    shares_growth_3y_cagr: Optional[float] = None
    fully_diluted_shares: Optional[float] = None
    dilution_ratio: Optional[float] = None
    production_growth_yoy: Optional[float] = None


@dataclass
class EfficiencyMetrics:
    asset_turnover: Optional[float] = None
    inventory_turnover: Optional[float] = None
    receivables_turnover: Optional[float] = None
    days_sales_outstanding: Optional[float] = None
    days_inventory: Optional[float] = None
    cash_conversion_cycle: Optional[float] = None


@dataclass
class MiningQualityIndicators:
    quality_score: Optional[float] = None
    management_quality: Optional[str] = None
    insider_ownership_pct: Optional[float] = None
    management_track_record: Optional[str] = None
    jurisdiction_assessment: Optional[str] = None
    jurisdiction_score: Optional[float] = None
    geological_quality: Optional[str] = None
    resource_grade_assessment: Optional[str] = None
    resource_scale_assessment: Optional[str] = None
    financial_position: Optional[str] = None
    dilution_risk: Optional[str] = None
    share_structure_assessment: Optional[str] = None
    catalyst_density: Optional[str] = None
    near_term_catalysts: list[str] = field(default_factory=list)
    strategic_backing: Optional[str] = None
    competitive_position: Optional[str] = None
    asset_backing: Optional[str] = None
    niche_position: Optional[str] = None
    insider_alignment: Optional[str] = None
    revenue_predictability: Optional[str] = None
    roic_history: list[Optional[float]] = field(default_factory=list)
    gross_margin_history: list[Optional[float]] = field(default_factory=list)


@dataclass
class IntrinsicValue:
    dcf_value: Optional[float] = None
    graham_number: Optional[float] = None
    lynch_fair_value: Optional[float] = None
    ncav_value: Optional[float] = None
    asset_based_value: Optional[float] = None
    nav_per_share: Optional[float] = None
    ev_resource_implied_price: Optional[float] = None
    current_price: Optional[float] = None
    margin_of_safety_dcf: Optional[float] = None
    margin_of_safety_graham: Optional[float] = None
    margin_of_safety_ncav: Optional[float] = None
    margin_of_safety_asset: Optional[float] = None
    margin_of_safety_nav: Optional[float] = None
    primary_method: Optional[str] = None
    secondary_method: Optional[str] = None


@dataclass
class ShareStructure:
    shares_outstanding: Optional[float] = None
    fully_diluted_shares: Optional[float] = None
    warrants_outstanding: Optional[float] = None
    options_outstanding: Optional[float] = None
    insider_ownership_pct: Optional[float] = None
    institutional_ownership_pct: Optional[float] = None
    float_shares: Optional[float] = None
    share_structure_assessment: Optional[str] = None
    warrant_overhang_risk: Optional[str] = None


@dataclass
class InsiderTransaction:
    """A single insider buy/sell transaction."""
    insider: str = ""
    position: str = ""
    transaction_type: str = ""  # e.g. "Exercise of options", "Disposition"
    shares: Optional[float] = None
    value: Optional[float] = None
    date: str = ""


@dataclass
class MarketIntelligence:
    """Market sentiment, insider activity, institutional holdings, and technicals.

    This section aggregates signals that are especially important for
    basic materials investors: insider buying in juniors is a strong
    signal, short interest indicates sentiment, and analyst targets
    provide a consensus reference for illiquid stocks.
    """
    # Insider activity
    insider_transactions: list[InsiderTransaction] = field(default_factory=list)
    net_insider_shares_3m: Optional[float] = None  # Net shares bought/sold last 3 months
    insider_buy_signal: Optional[str] = None  # "Strong buying", "Neutral", "Selling"

    # Institutional holders
    top_holders: list[str] = field(default_factory=list)  # Top 5 holder names
    institutions_count: Optional[int] = None
    institutions_pct: Optional[float] = None  # Total institutional %

    # Analyst consensus
    analyst_count: Optional[int] = None
    recommendation: Optional[str] = None  # "strong_buy", "buy", "hold", etc.
    target_high: Optional[float] = None
    target_low: Optional[float] = None
    target_mean: Optional[float] = None
    target_upside_pct: Optional[float] = None  # (target_mean - price) / price

    # Short interest
    shares_short: Optional[float] = None
    short_pct_of_float: Optional[float] = None
    short_ratio_days: Optional[float] = None  # Days to cover
    short_squeeze_risk: Optional[str] = None

    # Price technicals
    price_current: Optional[float] = None
    price_52w_high: Optional[float] = None
    price_52w_low: Optional[float] = None
    pct_from_52w_high: Optional[float] = None  # Negative = below high
    pct_from_52w_low: Optional[float] = None  # Positive = above low
    price_52w_range_position: Optional[float] = None  # 0-1 where in the range
    sma_50: Optional[float] = None
    sma_200: Optional[float] = None
    above_sma_50: Optional[bool] = None
    above_sma_200: Optional[bool] = None
    golden_cross: Optional[bool] = None  # 50d > 200d
    beta: Optional[float] = None
    avg_volume: Optional[float] = None
    volume_10d_avg: Optional[float] = None
    volume_trend: Optional[str] = None  # "Increasing", "Decreasing", "Stable"

    # Projected dilution (for pre-revenue miners)
    projected_dilution_annual_pct: Optional[float] = None
    projected_shares_in_2y: Optional[float] = None
    financing_warning: Optional[str] = None

    # Risk warnings
    risk_warnings: list[str] = field(default_factory=list)

    # Mining-specific disclaimers
    disclaimers: list[str] = field(default_factory=list)


@dataclass
class FinancialStatement:
    period: str
    revenue: Optional[float] = None
    cost_of_revenue: Optional[float] = None
    gross_profit: Optional[float] = None
    operating_income: Optional[float] = None
    net_income: Optional[float] = None
    ebitda: Optional[float] = None
    interest_expense: Optional[float] = None
    total_assets: Optional[float] = None
    total_liabilities: Optional[float] = None
    total_equity: Optional[float] = None
    total_debt: Optional[float] = None
    total_cash: Optional[float] = None
    current_assets: Optional[float] = None
    current_liabilities: Optional[float] = None
    operating_cash_flow: Optional[float] = None
    capital_expenditure: Optional[float] = None
    free_cash_flow: Optional[float] = None
    dividends_paid: Optional[float] = None
    shares_outstanding: Optional[float] = None
    eps: Optional[float] = None
    book_value_per_share: Optional[float] = None
    exploration_expenditure: Optional[float] = None
    mineral_properties: Optional[float] = None


@dataclass
class AnalysisConclusion:
    overall_score: float = 0.0
    verdict: str = ""
    summary: str = ""
    category_scores: dict = field(default_factory=dict)
    category_summaries: dict = field(default_factory=dict)
    strengths: list = field(default_factory=list)
    risks: list = field(default_factory=list)
    tier_note: str = ""
    stage_note: str = ""
    screening_checklist: dict = field(default_factory=dict)


@dataclass
class MetricExplanation:
    key: str
    full_name: str
    description: str
    why_used: str
    formula: str
    category: str


@dataclass
class Filing:
    form_type: str
    filing_date: str
    period: str
    url: str
    description: Optional[str] = None
    local_path: Optional[str] = None


@dataclass
class NewsArticle:
    title: str
    url: str
    published: Optional[str] = None
    source: Optional[str] = None
    summary: Optional[str] = None
    local_path: Optional[str] = None


@dataclass
class AnalysisReport:
    profile: CompanyProfile
    valuation: Optional[ValuationMetrics] = None
    profitability: Optional[ProfitabilityMetrics] = None
    solvency: Optional[SolvencyMetrics] = None
    growth: Optional[GrowthMetrics] = None
    efficiency: Optional[EfficiencyMetrics] = None
    mining_quality: Optional[MiningQualityIndicators] = None
    intrinsic_value: Optional[IntrinsicValue] = None
    share_structure: Optional[ShareStructure] = None
    market_intelligence: Optional[MarketIntelligence] = None
    financials: list[FinancialStatement] = field(default_factory=list)
    filings: list[Filing] = field(default_factory=list)
    news: list[NewsArticle] = field(default_factory=list)
    fetched_at: str = field(default_factory=lambda: datetime.now().isoformat())


# ---------------------------------------------------------------------------
# Stage classification helpers
# ---------------------------------------------------------------------------

_STAGE_KEYWORDS = {
    CompanyStage.PRODUCER: [
        "production", "producing", "mining operations", "mill", "processing plant",
        "AISC", "all-in sustaining", "cash cost per", "ore processed",
    ],
    CompanyStage.DEVELOPER: [
        "feasibility study", "pre-feasibility", "bankable", "construction",
        "development stage", "permitting", "environmental assessment",
        "and development of", "exploration and development",
    ],
    CompanyStage.EXPLORER: [
        "resource estimate", "NI 43-101", "JORC", "PEA", "preliminary economic",
        "mineral resource", "indicated resource", "measured resource",
        "inferred resource", "advanced exploration",
    ],
    CompanyStage.GRASSROOTS: [
        "exploration", "grassroots", "prospecting", "drill program",
        "early stage", "target generation",
    ],
}

_COMMODITY_KEYWORDS = {
    Commodity.GOLD: ["gold", "au", "gold equivalent", "auEq"],
    Commodity.SILVER: ["silver", "ag"],
    Commodity.COPPER: ["copper", "cu"],
    Commodity.URANIUM: ["uranium", "u3o8", "U3O8", "nuclear"],
    Commodity.LITHIUM: ["lithium", "li", "spodumene", "brine"],
    Commodity.NICKEL: ["nickel", "ni"],
    Commodity.ZINC: ["zinc", "zn"],
    Commodity.RARE_EARTHS: ["rare earth", "REE", "neodymium"],
}

_TIER_1_JURISDICTIONS = {
    "canada", "ontario", "quebec", "saskatchewan", "british columbia",
    "newfoundland", "labrador", "yukon",
    "united states", "nevada", "arizona", "wyoming", "utah", "idaho",
    "australia", "western australia",
    "finland", "ireland", "sweden",
}

_TIER_2_JURISDICTIONS = {
    "mexico", "peru", "chile", "brazil", "colombia", "argentina",
    "botswana", "namibia", "tanzania", "ghana", "burkina faso",
    "spain", "portugal", "turkey", "serbia",
}


def classify_stage(description: Optional[str], revenue: Optional[float],
                   info: Optional[dict] = None) -> CompanyStage:
    if description is None:
        description = ""
    desc_lower = description.lower()

    if revenue is not None and revenue > 10_000_000:
        for kw in ["royalty", "streaming", "stream"]:
            if kw in desc_lower:
                return CompanyStage.ROYALTY
        for kw in _STAGE_KEYWORDS[CompanyStage.PRODUCER]:
            if kw.lower() in desc_lower:
                return CompanyStage.PRODUCER

    for stage in [CompanyStage.PRODUCER, CompanyStage.DEVELOPER,
                  CompanyStage.EXPLORER, CompanyStage.GRASSROOTS]:
        for kw in _STAGE_KEYWORDS[stage]:
            if kw.lower() in desc_lower:
                return stage

    if info:
        industry = (info.get("industry") or "").lower()
        if "gold" in industry or "metals" in industry or "mining" in industry:
            return CompanyStage.EXPLORER

    return CompanyStage.GRASSROOTS


def classify_commodity(description: Optional[str],
                       industry: Optional[str] = None) -> Commodity:
    import re
    text = ((description or "") + " " + (industry or "")).lower()
    scores: dict[Commodity, int] = {}
    for commodity, keywords in _COMMODITY_KEYWORDS.items():
        count = 0
        for kw in keywords:
            kw_lower = kw.lower()
            # Use word boundary matching for short keywords to avoid false matches
            if len(kw_lower) <= 3:
                if re.search(r'\b' + re.escape(kw_lower) + r'\b', text):
                    count += 1
            else:
                if kw_lower in text:
                    count += 1
        if count > 0:
            scores[commodity] = count
    if scores:
        return max(scores, key=scores.get)
    return Commodity.OTHER


def classify_jurisdiction(country: Optional[str],
                          description: Optional[str] = None) -> JurisdictionTier:
    if not country:
        return JurisdictionTier.UNKNOWN
    c_lower = country.lower().strip()
    desc_lower = (description or "").lower()
    for j in _TIER_1_JURISDICTIONS:
        if j in c_lower or j in desc_lower:
            return JurisdictionTier.TIER_1
    for j in _TIER_2_JURISDICTIONS:
        if j in c_lower or j in desc_lower:
            return JurisdictionTier.TIER_2
    return JurisdictionTier.TIER_3
