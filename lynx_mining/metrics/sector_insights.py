"""Mining-focused sector and industry insights."""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class SectorInsight:
    sector: str; overview: str; critical_metrics: list[str] = field(default_factory=list)
    key_risks: list[str] = field(default_factory=list); what_to_watch: list[str] = field(default_factory=list)
    typical_valuation: str = ""

@dataclass
class IndustryInsight:
    industry: str; sector: str; overview: str; critical_metrics: list[str] = field(default_factory=list)
    key_risks: list[str] = field(default_factory=list); what_to_watch: list[str] = field(default_factory=list)
    typical_valuation: str = ""

_SECTORS: dict[str, SectorInsight] = {}
_INDUSTRIES: dict[str, IndustryInsight] = {}

def _add_sector(sector, overview, cm, kr, wtw, tv):
    _SECTORS[sector.lower()] = SectorInsight(sector=sector, overview=overview, critical_metrics=cm, key_risks=kr, what_to_watch=wtw, typical_valuation=tv)

def _add_industry(industry, sector, overview, cm, kr, wtw, tv):
    _INDUSTRIES[industry.lower()] = IndustryInsight(industry=industry, sector=sector, overview=overview, critical_metrics=cm, key_risks=kr, what_to_watch=wtw, typical_valuation=tv)

_add_sector("Basic Materials",
    "Basic materials (mining, chemicals, metals) are commodity-driven and highly cyclical. Reserves, production costs, and commodity price cycles dominate valuation. Balance sheet strength is critical to survive downturns. Junior miners are effectively venture capital — high risk, high reward.",
    ["AISC for producers", "Cash Runway for explorers", "EV/resource oz or lb", "P/NAV", "Share Dilution Rate", "Reserve Life"],
    ["Commodity price collapse", "Permitting delays/denials", "Dilutive financing at unfavorable terms", "Jurisdictional/political risk", "Capital cost overruns (20-50% common)"],
    ["Commodity price cycle position", "Drill results and resource growth", "Economic study progression (PEA->PFS->FS)", "Insider buying/selling", "Major miner strategic interest"],
    "P/NAV is primary for mining. EV/EBITDA 4-7 for producers. P/E unreliable due to commodity cycles. EV/resource for explorers.")

_add_sector("Energy",
    "Energy companies are tied to commodity prices. Uranium companies are included here and benefit from nuclear fleet growth and supply deficits.",
    ["Reserve Replacement", "Debt/EBITDA", "FCF Yield", "Breakeven Price"],
    ["Commodity price volatility", "Regulatory/permitting risk", "Energy transition uncertainty", "Geopolitical risk"],
    ["Supply-demand fundamentals", "Contract vs spot pricing", "Nuclear fleet growth (uranium)", "Capital discipline"],
    "EV/EBITDA 4-8. FCF yield is the best valuation anchor for producers.")

_add_industry("Gold", "Basic Materials",
    "Gold miners are leveraged to gold prices. AISC determines profitability. Reserve grade, mine life, and jurisdictional risk are critical. Junior gold explorers are valued on EV/oz and geological potential.",
    ["AISC per Ounce ($1,200-1,400 industry avg)", "Reserve Grade (>5 g/t open-pit, >12 g/t underground)", "Mine Life", "EV/oz ($10-50 inferred, $30-100 indicated)", "P/NAV"],
    ["Gold price decline", "Grade dilution as mines age", "Political/jurisdictional risk", "Rising energy and labor costs", "Permitting delays"],
    ["Gold price cycle", "AISC trend", "Exploration success and resource growth", "M&A discipline", "Insider buying"],
    "P/NAV 0.5-1.5x. EV/EBITDA 5-10 for producers. EV/oz for explorers. Avoid P/E — too volatile with gold cycles.")

_add_industry("Other Industrial Metals & Mining", "Basic Materials",
    "Industrial metals miners (copper, zinc, nickel, lithium) driven by industrial demand. Electrification and EV demand are structural tailwinds for copper and battery metals. Junior explorers carry high risk but asymmetric upside.",
    ["Cash Cost per Unit", "Resource/Reserve Size", "Grade and Recovery", "Jurisdictional Risk", "EV/lb for copper"],
    ["Commodity price volatility", "Permitting delays", "Capital cost overruns", "Financing dilution for explorers", "Metallurgical complexity"],
    ["Supply-demand balance", "Electrification demand forecasts", "Project economics (NPV/IRR)", "Insider ownership", "Major miner interest"],
    "Explorers: EV/Resource and P/NAV. Producers: EV/EBITDA 4-7. Copper benchmark: EV/lb < $0.08 is attractive.")

_add_industry("Uranium", "Basic Materials",
    "Uranium miners benefit from nuclear fleet growth and structural supply deficit. Contract vs spot dynamics are critical. Long development timelines. ISR (in-situ recovery) vs conventional mining affects cost profile significantly.",
    ["EV/lb U3O8 in ground", "Contract vs spot exposure", "Production cost per lb", "Cash Runway", "Permitting status"],
    ["Uranium price volatility", "Political/regulatory sentiment toward nuclear", "Long permitting timelines (5-15 years)", "Construction cost overruns", "Water rights and environmental issues"],
    ["Nuclear fleet growth (China, India)", "US/EU nuclear renaissance policy", "Supply deficit projections", "Sprott Physical Uranium Trust inventory", "Contract pricing vs spot"],
    "EV/lb of resource. P/NAV from feasibility studies. Denison Mines example: ~$100/lb production capacity. ISR producers trade at premium due to lower capex.")

_add_industry("Other Precious Metals & Mining", "Basic Materials",
    "Platinum group metals (PGMs), silver primary producers. PGMs driven by auto catalysts and hydrogen economy. Silver has both industrial and monetary demand drivers.",
    ["AISC per Ounce", "PGM Basket Price", "Mine Life", "Recovery Rate"],
    ["Auto industry transition to EVs reducing catalyst demand", "Substitution risk", "South African political risk", "Energy costs"],
    ["Hydrogen economy adoption for platinum", "Silver industrial demand growth", "Auto production trends", "Recycling supply"],
    "P/NAV and EV/EBITDA similar to gold miners. Silver valued via gold-silver ratio and silver-equivalent ounces.")

_add_industry("Specialty Mining & Metals", "Basic Materials",
    "Lithium, rare earths, cobalt, and other specialty metals. Driven by EV battery demand and defense/technology applications. High volatility, emerging supply chains.",
    ["Cost per unit of production", "Resource Grade", "Offtake Agreements", "Downstream Processing Capability"],
    ["Extreme price volatility", "Chinese supply dominance (rare earths)", "Technology shifts reducing demand", "Environmental permitting"],
    ["EV adoption rates", "Battery chemistry evolution", "Supply chain diversification policies", "Recycling technology"],
    "DCF at consensus long-term prices. EV/resource comparisons within same commodity only. Offtake agreements de-risk significantly.")

def get_sector_insight(sector: str | None) -> SectorInsight | None:
    return _SECTORS.get(sector.lower()) if sector else None

def get_industry_insight(industry: str | None) -> IndustryInsight | None:
    return _INDUSTRIES.get(industry.lower()) if industry else None

def list_sectors() -> list[str]:
    return sorted(s.sector for s in _SECTORS.values())

def list_industries() -> list[str]:
    return sorted(i.industry for i in _INDUSTRIES.values())
