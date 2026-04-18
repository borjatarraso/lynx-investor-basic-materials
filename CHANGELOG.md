# Changelog

All notable changes to Lynx Basic Materials Analysis are documented here.

## [0.2] - 2026-04-18

### Added
- **Market Intelligence section** across all 4 modes (console, interactive, TUI, GUI):
  - Analyst consensus with recommendation, count, and price targets with upside %
  - Short interest analysis with squeeze risk assessment
  - Price technicals: 52-week range position bar, 50d/200d SMA, golden/death cross detection
  - Insider transaction tracking with buy/sell signal classification
  - Top institutional holders with count and percentage
  - Projected dilution analysis for pre-revenue miners
  - Automated risk warnings (high beta, short interest, no analyst coverage, etc.)
  - Mining investment disclaimers (stage-specific)
- **Comprehensive unit tests** (90 tests in 5 test files):
  - test_models.py — 26 tests for classification functions and data models
  - test_calculator.py — 18 tests for all calc_* functions
  - test_relevance.py — 12 tests for stage/tier relevance system
  - test_conclusion.py — 7 tests for verdict generation and screening
  - test_storage.py — 5 tests for storage mode switching
  - test_explanations.py — 11 tests for metric explanations
- **Robot Framework acceptance tests** (38 GIVEN/WHEN/THEN tests):
  - cli_tests.robot — 12 CLI integration tests
  - api_tests.robot — 26 Python API tests
  - export_tests.robot — 2 export workflow tests (TXT, HTML)
- **Full documentation**:
  - README.md — Project overview, features, installation, usage
  - DEVELOPMENT.md — Architecture, data flow, extension guide
  - docs/API.md — Complete API reference with examples
  - CHANGELOG.md — This file
- **Enhanced TXT export** — all 15 analysis sections with aligned formatting
- **Enhanced HTML export** — Catppuccin Mocha theme, responsive cards, score bars, colored screening checklist, word-wrap on all table cells
- `.gitignore` for Python artifacts, cache dirs, IDE files
- Input validation for edge cases (empty identifier, very long input, invalid modes)

### Fixed
- **Robot test process arguments**: `Run Process` now passes `-m` and `lynx_mining` as separate arguments
- **Profitability section**: Shows explanatory message for pre-revenue stages instead of empty table (all 3 modes)
- **GUI table duplication**: Removed `_render_screening` from `_render_all_sections` (was duplicating screening inside conclusion)
- **GUI race condition**: Moved `_prepare_progressive()` from background thread to main thread in `_on_analyze()` to prevent section duplication
- **TUI rendering artifacts**: Replaced ANSI string pre-rendering with native Rich renderable pass-through in `_rich_table_widget()`
- **TUI `i` keybinding**: Now opens metric list with cursor on the currently focused metric instead of always starting at row 0
- **Commodity misclassification**: Word-boundary matching for short keywords (e.g., "ag" no longer matches inside "Saskatchewan")
- **Stage misclassification**: Added "exploration and development" keyword for Developer stage detection
- **GUI info buttons**: Section headers show "info", metric rows show "?" for visual distinction
- **Console text truncation**: Assessment columns use `ratio=1` with `overflow="fold"` for proper wrapping
- **TUI text truncation**: Long-text sections (insights, conclusion, mining quality, share structure, intrinsic value) use Rich Tables via `_rich_table_widget()` for multi-line cell support
- **News title truncation**: Removed 70-char hard limit, titles display in full
- **Business description**: Extended from 500 to 800 characters before truncation
- **Sector/Industry insights**: Added missing "What to Watch" field

### Changed
- `i` and `e` TUI keybindings now have distinct functions: `e` = context-aware explain, `i` = browse metric list with pre-selection
- Interactive `summary` command now includes market intelligence display
- All export formats now include complete analysis data

## [0.1] - 2026-04-18

### Added
- Initial release
- Stage-aware analysis (Grassroots/Explorer/Developer/Producer/Royalty)
- Mining-specific metrics: cash-to-market-cap, share dilution tracking, cash runway, burn rate, share structure assessment
- 4-level relevance system (Critical/Relevant/Contextual/Irrelevant)
- 10-point mining screening checklist
- Jurisdiction risk classification (Fraser Institute methodology)
- Commodity detection (Gold, Silver, Copper, Uranium, Lithium, etc.)
- 4 interface modes: Console CLI, Interactive REPL, Textual TUI, Tkinter GUI
- Export: TXT, HTML, PDF reports
- Sector & industry insights for basic materials
- Mining investment disclaimers
