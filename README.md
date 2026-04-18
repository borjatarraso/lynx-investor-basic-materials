# Lynx Basic Materials Analysis

> Fundamental analysis specialized for junior mining, uranium, copper, gold, and basic materials companies.

Part of the **Lince Investor Suite**.

## Overview

Lynx Basic Materials is a comprehensive fundamental analysis tool built specifically for basic materials investors. It evaluates companies across all development stages — from grassroots explorers to producers — using mining-specific metrics, valuation methods, and risk assessments.

### Key Features

- **Stage-Aware Analysis**: Automatically classifies companies as Grassroots Explorer, Advanced Explorer, Developer, Producer, or Royalty/Streaming — and adapts all metrics and scoring accordingly
- **Mining-Specific Metrics**: Cash-to-market-cap ratio, share dilution tracking, cash runway, burn rate analysis, share structure assessment
- **4-Level Relevance System**: Marks each metric as Critical, Relevant, Contextual, or Irrelevant based on the company's development stage
- **Market Intelligence**: Insider transactions, institutional holders, analyst consensus, short interest analysis, price technicals with golden/death cross detection
- **10-Point Mining Screening Checklist**: Evaluates cash runway, dilution, insider ownership, share structure, debt, jurisdiction, and more
- **Jurisdiction Risk Classification**: Tier 1/2/3 based on Fraser Institute methodology
- **Commodity Detection**: Automatic identification of primary commodity (Gold, Silver, Copper, Uranium, Lithium, etc.)
- **Multiple Interface Modes**: Console CLI, Interactive REPL, Textual TUI, Tkinter GUI
- **Export**: TXT, HTML, and PDF report generation
- **Sector & Industry Insights**: Deep context for Gold, Uranium, Copper, Silver, Lithium, Rare Earths, and more

### Target Companies

Designed for analyzing companies like:
- **Uranium**: Denison Mines (DML.TO), F3 Uranium (FUU.V), Energy Fuels (UUUU), NexGen Energy (NXE.TO)
- **Copper**: Oroco Resource Corp (OCO.V)
- **Gold**: Various TSXV/TSX explorers and producers
- **Lithium, Rare Earths, PGMs**: Specialty miners

## Installation

```bash
# Clone or download
cd lynx-investor-basic-materials

# Install dependencies
pip install -r requirements.txt

# Install in development mode
pip install -e .
```

### Requirements
- Python >= 3.10
- yfinance, requests, beautifulsoup4, rich, textual, feedparser, pandas, numpy

## Usage

### Direct Execution
```bash
# Via the runner script
./lynx-investor-basic-materials.py -p UUUU

# Via Python
python3 lynx-investor-basic-materials.py -p DML.TO

# Via pip-installed command
lynx-mining -p FUU.V
```

### Execution Modes

| Flag | Mode | Description |
|------|------|-------------|
| `-p` | Production | Uses `data/` for persistent cache |
| `-t` | Testing | Uses `data_test/` (isolated, always fresh) |

### Interface Modes

| Flag | Interface | Description |
|------|-----------|-------------|
| (none) | Console | Progressive CLI output |
| `-i` | Interactive | REPL with commands |
| `-tui` | TUI | Textual terminal UI with themes |
| `-x` | GUI | Tkinter graphical interface |

### Examples

```bash
# Analyze a uranium explorer
lynx-mining -p DML.TO

# Force fresh data download
lynx-mining -p UUUU --refresh

# Search by company name
lynx-mining -p "Denison Mines"

# Interactive mode
lynx-mining -p -i

# Export HTML report
lynx-mining -p DML.TO --export html

# Explain a metric
lynx-mining --explain cash_to_market_cap

# Skip filings and news for faster analysis
lynx-mining -t FUU.V --no-reports --no-news
```

## Analysis Sections

1. **Company Profile** — Tier, stage, commodity, jurisdiction classification
2. **Sector & Industry Insights** — Mining-specific context and benchmarks
3. **Valuation Metrics** — Traditional + mining-specific (Cash/Market Cap, P/B, EV/EBITDA)
4. **Profitability Metrics** — ROE, ROIC, margins (hidden for pre-revenue stages with explanation)
5. **Solvency & Survival** — Cash runway, burn rate, working capital, NCAV
6. **Growth & Dilution** — Share dilution tracking, 3Y dilution CAGR
7. **Share Structure** — Outstanding/diluted shares, insider/institutional ownership
8. **Mining Quality** — Insider alignment, financial position, dilution risk, asset backing
9. **Intrinsic Value** — DCF, Graham Number, NCAV, Asset-Based (method selection by stage)
10. **Market Intelligence** — Analysts, short interest, technicals, insider trades, risk warnings
11. **Financial Statements** — 5-year annual summary
12. **SEC/SEDAR Filings** — Downloadable regulatory filings
13. **News** — Yahoo Finance + Google News RSS
14. **Assessment Conclusion** — Weighted score, verdict, strengths/risks, screening checklist
15. **Mining Disclaimers** — Stage-specific risk disclosures

## Relevance System

Each metric is classified by importance for the company's development stage:

| Level | Display | Meaning |
|-------|---------|---------|
| **Critical** | `*` bold cyan star | Must-check for this stage |
| **Relevant** | Normal | Important context |
| **Contextual** | Dimmed | Informational only |
| **Irrelevant** | Hidden | Not meaningful for this stage |

Example: For a Grassroots Explorer, Cash Runway is **Critical** while P/E is **Irrelevant**.

## Scoring Methodology

The overall score (0-100) is a weighted average of 5 categories, with weights adapted by both company tier AND development stage:

| Stage | Valuation | Profitability | Solvency | Growth | Mining Quality |
|-------|-----------|---------------|----------|--------|----------------|
| Grassroots | 5% | 5% | 40% | 15% | 35% |
| Explorer | 10% | 5% | 35% | 15% | 35% |
| Developer | 10% | 10% | 35% | 15% | 30% |
| Producer | 20% | 20% | 20% | 20% | 20% |
| Royalty | 25% | 25% | 15% | 15% | 20% |

Verdicts: Strong Buy (>=75), Buy (>=60), Hold (>=45), Caution (>=30), Avoid (<30).

## Project Structure

```
lynx-investor-basic-materials/
├── lynx-investor-basic-materials.py  # Runner script
├── pyproject.toml                     # Build configuration
├── requirements.txt                   # Dependencies
├── img/                               # Logo images
├── data/                              # Production cache
├── data_test/                         # Testing cache
├── docs/                              # Documentation
│   └── API.md                         # API reference
├── robot/                             # Robot Framework tests
│   ├── cli_tests.robot
│   ├── api_tests.robot
│   └── export_tests.robot
├── tests/                             # Unit tests
└── lynx_mining/                       # Main package (29 files, ~10,000 LOC)
```

## Testing

```bash
# Unit tests
pytest tests/ -v

# Robot Framework acceptance tests
robot robot/
```

## License

BSD 3-Clause License. See LICENSE in source.

## Author

**Borja Tarraso** — borja.tarraso@member.fsf.org
