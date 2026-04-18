"""Metric explanations for Lynx Basic Materials Analysis."""

from __future__ import annotations
from lynx_mining.models import MetricExplanation

METRIC_EXPLANATIONS: dict[str, MetricExplanation] = {}

def _add(key, full_name, description, why_used, formula, category):
    METRIC_EXPLANATIONS[key] = MetricExplanation(key=key, full_name=full_name, description=description,
                                                  why_used=why_used, formula=formula, category=category)

# Valuation
_add("pe_trailing", "Price-to-Earnings Ratio (TTM)", "Compares stock price to trailing 12-month earnings per share.", "Most widely used valuation metric. Low P/E may indicate undervaluation.", "P/E = Price / EPS (TTM)", "valuation")
_add("pb_ratio", "Price-to-Book Ratio", "Compares stock price to book value per share.", "Core metric for value investing. P/B < 1 means trading below liquidation value.", "P/B = Price / Book Value per Share", "valuation")
_add("ps_ratio", "Price-to-Sales Ratio", "Compares stock price to revenue per share.", "Useful for pre-profit companies. P/S < 1 is generally cheap.", "P/S = Market Cap / Revenue", "valuation")
_add("p_fcf", "Price-to-Free Cash Flow", "Compares market cap to free cash flow.", "More reliable than P/E — cash flow is harder to manipulate.", "P/FCF = Market Cap / Free Cash Flow", "valuation")
_add("ev_ebitda", "Enterprise Value / EBITDA", "Capital-structure-neutral valuation.", "EV/EBITDA < 5 is cheap for mining producers. Preferred over P/E for cross-company comparison.", "EV/EBITDA = (Market Cap + Debt - Cash) / EBITDA", "valuation")
_add("ev_revenue", "Enterprise Value / Revenue", "Compares enterprise value to revenue.", "Useful for pre-profit producers. EV/Revenue < 1 is very cheap.", "EV/Revenue = EV / Revenue", "valuation")
_add("peg_ratio", "PEG Ratio", "P/E adjusted by growth rate.", "PEG < 1 suggests undervalued relative to growth. Less relevant for cyclical miners.", "PEG = P/E / Annual EPS Growth Rate", "valuation")
_add("dividend_yield", "Dividend Yield", "Annual dividend as percentage of price.", "Rare for junior miners. Common for large producers and royalty companies.", "Yield = Annual Dividends / Price", "valuation")
_add("earnings_yield", "Earnings Yield", "Inverse of P/E ratio.", "Compare to bond yields for relative attractiveness.", "Earnings Yield = EPS / Price", "valuation")
_add("price_to_tangible_book", "Price / Tangible Book", "Price vs tangible book value per share.", "More conservative than P/B. Critical for asset-heavy mining companies.", "P/TBV = Price / (Equity - Intangibles) / Shares", "valuation")
_add("price_to_ncav", "Price / NCAV (Net-Net)", "Price vs net current asset value per share.", "Graham's net-net criterion. Below NCAV = trading below liquidation value.", "P/NCAV = Price / (Current Assets - Total Liabilities) / Shares", "valuation")
_add("cash_to_market_cap", "Cash-to-Market-Cap Ratio", "How much of market cap is backed by cash.", "Critical for explorers. >50% means buying exploration assets cheaply or even for free. >30% is strong cash backing.", "Cash / Market Cap = Total Cash / Market Capitalization", "valuation")
_add("ev_per_resource_oz", "EV per Resource Ounce", "Enterprise value per ounce of gold/silver resource.", "Key metric for gold/silver miners. Benchmarks: $10-50/oz inferred, $30-100/oz indicated in Tier 1 jurisdictions.", "EV / Total Resource Ounces", "valuation")
_add("ev_per_resource_lb", "EV per Resource Pound", "Enterprise value per pound of copper/uranium resource.", "Key metric for copper/uranium miners. Compare only within same commodity and stage.", "EV / Total Resource Pounds", "valuation")
_add("p_nav", "Price / Net Asset Value", "Market cap vs NAV from economic studies.", "Primary valuation for development/production mining. PEA: 0.1-0.3x, PFS: 0.3-0.5x, FS: 0.5x+, Producer: 0.8-1.2x.", "P/NAV = Market Cap / NPV from Economic Study", "valuation")

# Profitability
_add("roe", "Return on Equity", "Profit generated per dollar of equity.", "Target ROE > 15% for producers. Less meaningful for pre-revenue explorers.", "ROE = Net Income / Equity", "profitability")
_add("roa", "Return on Assets", "Profit per dollar of assets.", "ROA > 5% is good. Not inflated by leverage.", "ROA = Net Income / Total Assets", "profitability")
_add("roic", "Return on Invested Capital", "Return on all invested capital.", "ROIC > 10% suggests competitive advantage. Key for producers.", "ROIC = NOPAT / Invested Capital", "profitability")
_add("gross_margin", "Gross Margin", "Revenue remaining after cost of goods sold.", "For mining producers, indicates cost efficiency. High margins = low-cost producer.", "Gross Margin = Gross Profit / Revenue", "profitability")
_add("operating_margin", "Operating Margin", "Revenue remaining after all operating expenses.", "Shows core business profitability. Relevant for producers only.", "Operating Margin = Operating Income / Revenue", "profitability")
_add("net_margin", "Net Profit Margin", "Revenue remaining as net profit.", "Bottom line profitability. Not applicable for pre-revenue miners.", "Net Margin = Net Income / Revenue", "profitability")
_add("fcf_margin", "Free Cash Flow Margin", "Revenue converted to free cash flow.", "Measures actual cash generation. Critical for producers.", "FCF Margin = FCF / Revenue", "profitability")
_add("ebitda_margin", "EBITDA Margin", "Revenue remaining as EBITDA.", "Approximates operating cash flow. EBITDA Margin > 30% is excellent.", "EBITDA Margin = EBITDA / Revenue", "profitability")

# Solvency
_add("debt_to_equity", "Debt-to-Equity Ratio", "Debt financing vs equity financing.", "Junior explorers should have near-zero debt. Any debt in pre-revenue is a red flag.", "D/E = Total Debt / Equity", "solvency")
_add("current_ratio", "Current Ratio", "Short-term asset coverage of liabilities.", "CR > 2 is healthy for miners. < 1.0 signals near-term liquidity risk.", "Current Ratio = Current Assets / Current Liabilities", "solvency")
_add("quick_ratio", "Quick Ratio", "Liquidity excluding inventory.", "More conservative than current ratio.", "Quick Ratio = (Current Assets - Inventory) / Current Liabilities", "solvency")
_add("interest_coverage", "Interest Coverage", "Ability to pay interest from operating earnings.", "> 4 is comfortable. < 1.5 is dangerous.", "Interest Coverage = Operating Income / Interest Expense", "solvency")
_add("altman_z_score", "Altman Z-Score", "Bankruptcy probability predictor.", "Z > 2.99: Safe. 1.81-2.99: Grey zone. < 1.81: Distress. Less meaningful for pre-revenue miners.", "Z = 1.2(WC/TA) + 1.4(RE/TA) + 3.3(EBIT/TA) + 0.6(MV/TL) + 1.0(Sales/TA)", "solvency")
_add("cash_burn_rate", "Cash Burn Rate", "Annual rate of cash consumption.", "Critical for pre-revenue miners. Determines survival without financing.", "Cash Burn = Annual Operating Cash Flow (when negative)", "solvency")
_add("cash_runway_years", "Cash Runway", "Years of operation at current burn rate.", "< 1 year = imminent financing. > 3 years = comfortable. 18+ months is the target for junior miners.", "Cash Runway = Total Cash / Annual Burn Rate", "solvency")
_add("ncav_per_share", "NCAV Per Share", "Net current asset value per share.", "Graham's net-net. If price < NCAV, trading below liquidation value.", "NCAV/Share = (Current Assets - Total Liabilities) / Shares", "solvency")
_add("burn_as_pct_of_market_cap", "Burn Rate % of Market Cap", "How fast the company consumes value.", "Below 2% quarterly is ideal. >8% annually is a red flag — the company is burning through its market cap too fast.", "Burn % = |Annual Burn Rate| / Market Cap", "solvency")

# Growth
_add("revenue_growth_yoy", "Revenue Growth (YoY)", "Annual revenue change.", "Shows business trajectory. Relevant for producers and royalty companies.", "Growth = (Rev_Current - Rev_Prior) / |Rev_Prior|", "growth")
_add("revenue_cagr_3y", "Revenue CAGR (3-Year)", "3-year compound revenue growth.", "Smooths volatility. > 10% is strong for mature miners.", "CAGR = (End/Start)^(1/3) - 1", "growth")
_add("earnings_growth_yoy", "Earnings Growth (YoY)", "Annual net income change.", "Drives stock appreciation for producers.", "Growth = (NI_Current - NI_Prior) / |NI_Prior|", "growth")
_add("shares_growth_yoy", "Share Dilution (YoY)", "Annual change in shares outstanding.", "THE most critical metric for junior miners. >10%/yr is heavy dilution destroying shareholder value. <5%/yr is acceptable.", "Dilution = (Shares_Current - Shares_Prior) / Shares_Prior", "growth")
_add("shares_growth_3y_cagr", "Dilution CAGR (3-Year)", "3-year compound share dilution rate.", "Shows persistent dilution pattern. >10%/yr CAGR is a structural problem. Companies that started at 30M shares and diluted to 500M+ are red flags.", "CAGR = (Shares_End / Shares_Start)^(1/3) - 1", "growth")
_add("quality_score", "Mining Quality Score", "Composite quality score (0-100).", "Evaluates insider ownership, financial position, dilution risk, asset backing, and business viability. Weights adapt by development stage. >70 is high quality, <30 is weak.", "Weighted sum of: insider alignment, financial position, dilution risk, asset backing, revenue status", "mining_quality")

SECTION_EXPLANATIONS = {
    "profile": {"title": "Company Profile", "description": "Company identification, market cap tier, mining development stage, primary commodity, and jurisdiction risk classification."},
    "valuation": {"title": "Valuation Metrics", "description": "Price-based ratios including traditional metrics and mining-specific valuations (cash-to-market-cap, EV/resource). For pre-revenue explorers, cash backing replaces P/E as the primary metric."},
    "profitability": {"title": "Profitability Metrics", "description": "Margin and return analysis. Not applicable for pre-revenue explorers. For producers, AISC and operating margins indicate cost efficiency on the global cost curve."},
    "solvency": {"title": "Solvency & Survival", "description": "Balance sheet strength, liquidity, and survival metrics. Cash burn rate and runway are critical for junior miners. Explorers should have minimal debt. 18+ months cash runway is the target."},
    "growth": {"title": "Growth & Dilution", "description": "Revenue/earnings growth for producers, and share dilution tracking for all stages. Dilution is the #1 risk for junior miners — heavy dilution (>10%/yr) destroys shareholder value."},
    "share_structure": {"title": "Share Structure", "description": "Analysis of outstanding shares, fully diluted count, insider ownership, and institutional holdings. Tight structure (<150M shares) with high insider ownership (>10%) is ideal."},
    "mining_quality": {"title": "Mining Quality Assessment", "description": "Stage-appropriate quality scoring. Evaluates insider alignment, financial position, dilution risk, asset backing, and revenue status. Replaces traditional moat analysis with mining-specific factors."},
    "intrinsic_value": {"title": "Intrinsic Value Estimates", "description": "Multiple valuation methods adapted by stage. Producers: DCF/P/NAV. Developers: P/NAV from economic studies. Explorers: EV/resource and asset-based. Grassroots: cash backing."},
    "conclusion": {"title": "Assessment Conclusion", "description": "Weighted scoring across 5 categories with weights adapted by both tier and stage. Includes a 10-point mining screening checklist evaluating key quality criteria."},
}

CONCLUSION_METHODOLOGY = {
    "overall": {"title": "Conclusion Methodology", "description": "Score is a weighted average of 5 categories (valuation, profitability, solvency, growth, mining quality). Weights vary by BOTH company tier AND mining stage. Explorers weight solvency at 35-40% and mining quality at 30-35%. Producers use more balanced weights. Verdicts: Strong Buy (>=75), Buy (>=60), Hold (>=45), Caution (>=30), Avoid (<30)."},
    "valuation": {"title": "Valuation Score", "description": "Starts at 50. Adjusted by P/E, P/B, cash-to-market-cap (bonus for explorers), and EV/EBITDA. Pre-revenue metrics are excluded for explorer/grassroots stages."},
    "solvency": {"title": "Solvency Score", "description": "Starts at 50. Debt/equity, current ratio, cash runway, and burn rate as % of market cap. Explorers are penalized heavily for any debt. Cash runway < 1 year = -25 points."},
    "mining_quality": {"title": "Mining Quality Score", "description": "Composite of insider alignment (20pts), financial position (25pts), dilution risk (20pts), asset backing (20pts), and revenue/stage status (15pts). Share structure bonus/penalty."},
}

def get_explanation(key): return METRIC_EXPLANATIONS.get(key)
def get_section_explanation(section): return SECTION_EXPLANATIONS.get(section)
def get_conclusion_explanation(category=None): return CONCLUSION_METHODOLOGY.get(category or "overall")
def list_metrics(category=None):
    metrics = list(METRIC_EXPLANATIONS.values())
    return [m for m in metrics if m.category == category] if category else metrics
