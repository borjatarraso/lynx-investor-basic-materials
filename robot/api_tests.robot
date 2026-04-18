*** Settings ***
Documentation    Python API tests for lynx-mining
Library          Process

*** Variables ***
${PYTHON}        python3

*** Keywords ***
When I Run Python Code "${code}"
    ${result}=    Run Process    ${PYTHON}    -c    ${code}    timeout=120s
    Set Test Variable    ${OUTPUT}    ${result.stdout}${result.stderr}
    Set Test Variable    ${RC}    ${result.rc}

Then The Exit Code Should Be ${expected}
    Should Be Equal As Integers    ${RC}    ${expected}

Then The Output Should Contain "${text}"
    Should Contain    ${OUTPUT}    ${text}

*** Test Cases ***
Import All Models
    [Documentation]    GIVEN the package WHEN I import models THEN all classes are available
    When I Run Python Code "from lynx_mining.models import AnalysisReport, CompanyProfile, CompanyStage, CompanyTier, Commodity, JurisdictionTier, Relevance, MarketIntelligence, InsiderTransaction; print('OK')"
    Then The Exit Code Should Be 0
    Then The Output Should Contain "OK"

Import All Calculators
    [Documentation]    GIVEN the package WHEN I import calculators THEN all functions exist
    When I Run Python Code "from lynx_mining.metrics.calculator import calc_valuation, calc_profitability, calc_solvency, calc_growth, calc_efficiency, calc_share_structure, calc_mining_quality, calc_intrinsic_value, calc_market_intelligence; print('OK')"
    Then The Exit Code Should Be 0
    Then The Output Should Contain "OK"

Classify Company Tier Mega Cap
    [Documentation]    GIVEN a large market cap WHEN I classify THEN it returns Mega Cap
    When I Run Python Code "from lynx_mining.models import classify_tier; print(classify_tier(500_000_000_000).value)"
    Then The Exit Code Should Be 0
    Then The Output Should Contain "Mega Cap"

Classify Company Tier Micro Cap
    [Documentation]    GIVEN a small market cap WHEN I classify THEN it returns Micro Cap
    When I Run Python Code "from lynx_mining.models import classify_tier; print(classify_tier(100_000_000).value)"
    Then The Exit Code Should Be 0
    Then The Output Should Contain "Micro Cap"

Classify Company Tier None
    [Documentation]    GIVEN None market cap WHEN I classify THEN it returns Nano Cap
    When I Run Python Code "from lynx_mining.models import classify_tier; print(classify_tier(None).value)"
    Then The Exit Code Should Be 0
    Then The Output Should Contain "Nano Cap"

Classify Mining Stage Explorer
    [Documentation]    GIVEN a description with resource estimate WHEN I classify THEN Explorer
    When I Run Python Code "from lynx_mining.models import classify_stage; print(classify_stage('NI 43-101 resource estimate', 0).value)"
    Then The Exit Code Should Be 0
    Then The Output Should Contain "Advanced Explorer"

Classify Mining Stage Producer
    [Documentation]    GIVEN a description with production WHEN I classify THEN Producer
    When I Run Python Code "from lynx_mining.models import classify_stage; print(classify_stage('gold mining operations with AISC', 50000000).value)"
    Then The Exit Code Should Be 0
    Then The Output Should Contain "Producer"

Classify Mining Stage Developer
    [Documentation]    GIVEN a feasibility study description WHEN I classify THEN Developer
    When I Run Python Code "from lynx_mining.models import classify_stage; print(classify_stage('feasibility study complete', 0).value)"
    Then The Exit Code Should Be 0
    Then The Output Should Contain "Developer"

Classify Mining Stage Grassroots
    [Documentation]    GIVEN exploration description WHEN I classify THEN Grassroots
    When I Run Python Code "from lynx_mining.models import classify_stage; print(classify_stage('early stage exploration drill program', 0).value)"
    Then The Exit Code Should Be 0
    Then The Output Should Contain "Grassroots Explorer"

Classify Commodity Uranium
    [Documentation]    GIVEN uranium text WHEN I classify THEN Uranium detected
    When I Run Python Code "from lynx_mining.models import classify_commodity; print(classify_commodity('uranium u3o8 exploration', 'Uranium').value)"
    Then The Exit Code Should Be 0
    Then The Output Should Contain "Uranium"

Classify Commodity Gold
    [Documentation]    GIVEN gold text WHEN I classify THEN Gold detected
    When I Run Python Code "from lynx_mining.models import classify_commodity; print(classify_commodity('gold mining au', 'Gold').value)"
    Then The Exit Code Should Be 0
    Then The Output Should Contain "Gold"

Classify Jurisdiction Tier 1
    [Documentation]    GIVEN Canada WHEN I classify THEN Tier 1
    When I Run Python Code "from lynx_mining.models import classify_jurisdiction; print(classify_jurisdiction('Canada').value)"
    Then The Exit Code Should Be 0
    Then The Output Should Contain "Tier 1"

Classify Jurisdiction Tier 2
    [Documentation]    GIVEN Mexico WHEN I classify THEN Tier 2
    When I Run Python Code "from lynx_mining.models import classify_jurisdiction; print(classify_jurisdiction('Mexico').value)"
    Then The Exit Code Should Be 0
    Then The Output Should Contain "Tier 2"

Relevance Explorer PE Irrelevant
    [Documentation]    GIVEN explorer WHEN I check P/E THEN irrelevant
    When I Run Python Code "from lynx_mining.metrics.relevance import get_relevance; from lynx_mining.models import CompanyTier, CompanyStage; print(get_relevance('pe_trailing', CompanyTier.MICRO, 'valuation', CompanyStage.EXPLORER).value)"
    Then The Exit Code Should Be 0
    Then The Output Should Contain "irrelevant"

Relevance Explorer Cash Runway Critical
    [Documentation]    GIVEN explorer WHEN I check cash runway THEN critical
    When I Run Python Code "from lynx_mining.metrics.relevance import get_relevance; from lynx_mining.models import CompanyTier, CompanyStage; print(get_relevance('cash_runway_years', CompanyTier.MICRO, 'solvency', CompanyStage.EXPLORER).value)"
    Then The Exit Code Should Be 0
    Then The Output Should Contain "critical"

Relevance Producer EV EBITDA Critical
    [Documentation]    GIVEN producer WHEN I check EV/EBITDA THEN critical
    When I Run Python Code "from lynx_mining.metrics.relevance import get_relevance; from lynx_mining.models import CompanyTier, CompanyStage; print(get_relevance('ev_ebitda', CompanyTier.MID, 'valuation', CompanyStage.PRODUCER).value)"
    Then The Exit Code Should Be 0
    Then The Output Should Contain "critical"

Get Metric Explanation
    [Documentation]    GIVEN metric key WHEN I get explanation THEN details returned
    When I Run Python Code "from lynx_mining.metrics.explanations import get_explanation; e = get_explanation('cash_to_market_cap'); print(e.full_name)"
    Then The Exit Code Should Be 0
    Then The Output Should Contain "Cash-to-Market-Cap"

Get Unknown Metric Returns None
    [Documentation]    GIVEN bad key WHEN I get explanation THEN None
    When I Run Python Code "from lynx_mining.metrics.explanations import get_explanation; print(get_explanation('nonexistent'))"
    Then The Exit Code Should Be 0
    Then The Output Should Contain "None"

Get Sector Insight
    [Documentation]    GIVEN Basic Materials WHEN I get insight THEN data returned
    When I Run Python Code "from lynx_mining.metrics.sector_insights import get_sector_insight; s = get_sector_insight('Basic Materials'); print('OK' if s else 'FAIL')"
    Then The Exit Code Should Be 0
    Then The Output Should Contain "OK"

Get Industry Insight Uranium
    [Documentation]    GIVEN Uranium WHEN I get insight THEN data returned
    When I Run Python Code "from lynx_mining.metrics.sector_insights import get_industry_insight; i = get_industry_insight('Uranium'); print('OK' if i else 'FAIL')"
    Then The Exit Code Should Be 0
    Then The Output Should Contain "OK"

Storage Mode Switching
    [Documentation]    GIVEN storage WHEN I switch modes THEN it works
    When I Run Python Code "from lynx_mining.core.storage import set_mode, get_mode, is_testing; set_mode('testing'); assert is_testing(); set_mode('production'); assert not is_testing(); print('OK')"
    Then The Exit Code Should Be 0
    Then The Output Should Contain "OK"

Storage Invalid Mode Raises Error
    [Documentation]    GIVEN storage WHEN I set invalid mode THEN error
    When I Run Python Code "from lynx_mining.core.storage import set_mode; set_mode('invalid')"
    Then The Exit Code Should Be 1
    Then The Output Should Contain "ValueError"

Export Formats Available
    [Documentation]    GIVEN export module WHEN I check formats THEN all exist
    When I Run Python Code "from lynx_mining.export import ExportFormat; print(ExportFormat.TXT.value, ExportFormat.HTML.value, ExportFormat.PDF.value)"
    Then The Exit Code Should Be 0
    Then The Output Should Contain "txt html pdf"

About Text Has All Fields
    [Documentation]    GIVEN package WHEN I get about THEN all fields present
    When I Run Python Code "from lynx_mining import get_about_text; a = get_about_text(); assert all(k in a for k in ['name','suite','version','author','license','description']); print('OK')"
    Then The Exit Code Should Be 0
    Then The Output Should Contain "OK"

Conclusion Generation
    [Documentation]    GIVEN minimal report WHEN I generate conclusion THEN a verdict is produced
    When I Run Python Code "from lynx_mining.models import AnalysisReport, CompanyProfile; from lynx_mining.core.conclusion import generate_conclusion; r = AnalysisReport(profile=CompanyProfile(ticker='TEST', name='Test')); c = generate_conclusion(r); assert c.verdict in ['Strong Buy','Buy','Hold','Caution','Avoid']; print('OK')"
    Then The Exit Code Should Be 0
    Then The Output Should Contain "OK"

Mining Metrics In Explanations
    [Documentation]    GIVEN explanations WHEN I list THEN mining metrics present
    When I Run Python Code "from lynx_mining.metrics.explanations import list_metrics; keys = [m.key for m in list_metrics()]; assert 'cash_to_market_cap' in keys; assert 'quality_score' in keys; print('OK')"
    Then The Exit Code Should Be 0
    Then The Output Should Contain "OK"
