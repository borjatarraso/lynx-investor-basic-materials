# Changelog

All notable changes to Lynx Basic Materials Analysis are documented here.

## [2.0] - 2026-04-19

Major release — **Lince Investor Suite v2.0** unified release.

### Changed
- **Unified suite**: All Lince Investor projects now share consistent
  version numbering, logos, keybindings, CLI patterns, export styling,
  installation instructions, and documentation structure.
- **Export styling**: Monospace HTML (Consolas family), 90-char TXT width,
  unified with other suite projects.
- **Documentation**: Standardized installation section with dependency
  table matching other suite projects.
- **Git branch**: Renamed `master` → `main` for consistency.

## [1.0] - 2026-04-19

### Added
- **Comprehensive test suite**: 151 unit tests + 42 robot tests = 193 total
  - test_sector_validation.py — 14 tests for sector gate (allow/block scenarios, false positive prevention)
  - test_export.py — 14 tests for TXT/HTML exports (format handling, XSS, white background, word wrap, print media, footer)
- **SectorMismatchError** exported from analyzer for programmatic handling

### Fixed
- **Sector validation empty string bug**: Empty industry `""` matched as substring of every allowed industry via `"" in "gold"` → added guard `if industry:` before substring check
- **export_report accepts both string and enum**: Resolves `'str' object has no attribute 'value'` across all modes

### Changed
- Version bumped to 1.0 — first stable release
- All documentation updated for v1.0

## [0.6] - 2026-04-19

### Added
- **Sector validation gate**: Analysis is blocked with a prominent red blinking warning for companies outside Basic Materials / Commodities / Energy sectors
  - Console: Red bordered panel with "!! WRONG SECTOR !!" title and blinking text
  - Interactive: Same red panel with sector mismatch details
  - TUI: Bold red blinking status message with allowed sectors list
  - GUI: Custom dark red dialog with warning icons, sector list, and close button
- **SectorMismatchError** exception class in analyzer for programmatic handling
- **Mining-specific description validation**: Uses word-boundary regex patterns to detect genuine mining companies (avoids false positives like "App Store" matching "ore" or "lithium-ion battery" matching "lithium")

### Fixed
- **GUI export button**: Fixed closure variable capture — `fmt.get()` is now called before `win.destroy()` to prevent the StringVar from being garbage collected
- **False positive sector validation**: "ore" no longer matches inside "store", "lithium" no longer matches "lithium-ion battery" contexts — uses mining-specific phrase patterns instead of bare commodity names
- Added status message during export ("Exporting as HTML...")

## [0.5] - 2026-04-19

### Added
- **Commodity market context** in all modes (console, interactive, TUI, GUI, exports):
  - Live commodity spot prices (Gold, Silver, Copper, Lithium, Nickel, Zinc) from yfinance futures
  - Commodity 52-week range with visual position bar
  - Sector ETF performance (GDX, SIL, COPX, URA, URNM, LIT, PICK, XME, REMX) with 3-month returns
  - Peer ETF comparison for cross-referencing sector momentum
  - Automatic commodity detection from company description links to the right market data
- **Commodity context in exports**: TXT and HTML exports include commodity & sector context section

### Changed
- **HTML export redesigned** with professional financial report styling:
  - Georgia serif headings with navy (#1a2744) color palette
  - Subtle card shadows and thin borders instead of colored borders
  - Elegant score bars with green/amber/red professional colors
  - Understated verdict cards (pastel backgrounds, not garish)
  - Small-caps uppercase section headers with letter spacing
  - Professional footer with branding and disclaimer
  - Print-optimized with @media print rules and card break-inside:avoid
  - Alternating table row backgrounds (#f9fafb)
  - Proper typographic hierarchy

### Fixed
- Robot export tests: Updated CSS assertions to match new styling (`#fff` vs `#ffffff`, spaced vs compact property values)

## [0.4] - 2026-04-19

### Fixed
- **Path traversal vulnerability**: Ticker names with `../` are now sanitized via `_sanitize_ticker()` to prevent directory escapes
- **`--max-filings` validation**: Now rejects 0 and negative values with `_positive_int` validator
- **`calc_intrinsic_value` with empty statements**: Method selection (primary/secondary) now always set even when no financial data is available
- **HTML export XSS**: Verified all user-supplied strings are HTML-escaped via `html.escape()`

### Added
- **26 new edge case tests** (`tests/test_edge_cases.py`):
  - Path traversal prevention (8 tests)
  - ISIN validation (4 tests)
  - NaN/Inf handling in metrics, conclusion, and exports (4 tests)
  - Zero division scenarios (3 tests)
  - HTML export security (2 tests)
  - Empty report display (2 tests)
  - Calculator edge cases with empty/missing data (3 tests)
- **Storage `_sanitize_ticker()`**: Strips special characters, prevents `..` traversal, uppercases, handles empty input
- Total: 158 tests (116 unit + 42 robot), all passing

## [0.3] - 2026-04-18

### Fixed
- **HTML export**: Changed from dark Catppuccin theme to professional white background with dark text, readable when printed
- **HTML tables**: Added `table-layout:fixed` and `overflow-wrap:break-word` to prevent any text truncation in cells
- **HTML print support**: Added `@media print` CSS with `break-inside:avoid` on cards
- **HTML score bars**: Adjusted colors for readability on white background (green/amber/red)
- **Robot export tests**: Rewrote to use Python API with synthetic reports (avoids network timeouts), added HTML quality assertions
- **Export timeout**: Increased Robot Framework process timeout to 300s for network tests

### Changed
- HTML export now produces professional print-ready reports with white background
- Export tests now verify white background, word-wrap, and print media support
- Robot test suite: 42 tests (was 38), all passing
- Unit test suite: 90 tests, all passing
- Total: 132 tests, all passing

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
