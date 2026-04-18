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
    When I Run Python Code "from lynx_mining.models import AnalysisReport, CompanyProfile, CompanyStage, CompanyTier, Commodity, JurisdictionTier, Relevance, MarketIntelligence; print('OK')"
    Then The Exit Code Should Be 0
    Then The Output Should Contain "OK"

Classify Company Tier
    [Documentation]    GIVEN a market cap WHEN I classify tier THEN the correct tier is returned
    When I Run Python Code "from lynx_mining.models import classify_tier; print(classify_tier(100_000_000).value)"
    Then The Exit Code Should Be 0
    Then The Output Should Contain "Micro Cap"

Classify Mining Stage
    [Documentation]    GIVEN a description WHEN I classify stage THEN the correct stage is returned
    When I Run Python Code "from lynx_mining.models import classify_stage; print(classify_stage('NI 43-101 resource estimate', 0).value)"
    Then The Exit Code Should Be 0
    Then The Output Should Contain "Advanced Explorer"

Classify Commodity
    [Documentation]    GIVEN a description WHEN I classify commodity THEN uranium is detected
    When I Run Python Code "from lynx_mining.models import classify_commodity; print(classify_commodity('uranium u3o8 exploration', 'Uranium').value)"
    Then The Exit Code Should Be 0
    Then The Output Should Contain "Uranium"

Classify Jurisdiction
    [Documentation]    GIVEN a country WHEN I classify jurisdiction THEN tier is correct
    When I Run Python Code "from lynx_mining.models import classify_jurisdiction; print(classify_jurisdiction('Canada').value)"
    Then The Exit Code Should Be 0
    Then The Output Should Contain "Tier 1"

Get Relevance For Explorer
    [Documentation]    GIVEN an explorer stage WHEN I check P/E relevance THEN it is irrelevant
    When I Run Python Code "from lynx_mining.metrics.relevance import get_relevance; from lynx_mining.models import CompanyTier, CompanyStage; print(get_relevance('pe_trailing', CompanyTier.MICRO, 'valuation', CompanyStage.EXPLORER).value)"
    Then The Exit Code Should Be 0
    Then The Output Should Contain "irrelevant"

Get Relevance For Cash Runway
    [Documentation]    GIVEN an explorer WHEN I check cash runway relevance THEN it is critical
    When I Run Python Code "from lynx_mining.metrics.relevance import get_relevance; from lynx_mining.models import CompanyTier, CompanyStage; print(get_relevance('cash_runway_years', CompanyTier.MICRO, 'solvency', CompanyStage.EXPLORER).value)"
    Then The Exit Code Should Be 0
    Then The Output Should Contain "critical"

Get Metric Explanation
    [Documentation]    GIVEN a metric key WHEN I get explanation THEN it returns details
    When I Run Python Code "from lynx_mining.metrics.explanations import get_explanation; e = get_explanation('cash_to_market_cap'); print(e.full_name)"
    Then The Exit Code Should Be 0
    Then The Output Should Contain "Cash-to-Market-Cap"

Get Sector Insight
    [Documentation]    GIVEN a sector WHEN I get insight THEN it returns mining context
    When I Run Python Code "from lynx_mining.metrics.sector_insights import get_sector_insight; s = get_sector_insight('Basic Materials'); print(s.overview[:50])"
    Then The Exit Code Should Be 0
    Then The Output Should Contain "materials"

Get Industry Insight For Uranium
    [Documentation]    GIVEN uranium industry WHEN I get insight THEN it returns uranium-specific data
    When I Run Python Code "from lynx_mining.metrics.sector_insights import get_industry_insight; i = get_industry_insight('Uranium'); print(i.overview[:50])"
    Then The Exit Code Should Be 0
    Then The Output Should Contain "Uranium"

Storage Mode Switching
    [Documentation]    GIVEN the storage module WHEN I set testing mode THEN it switches
    When I Run Python Code "from lynx_mining.core.storage import set_mode, get_mode, is_testing; set_mode('testing'); print(get_mode(), is_testing())"
    Then The Exit Code Should Be 0
    Then The Output Should Contain "testing True"

Export Format Enum
    [Documentation]    GIVEN the export module WHEN I check formats THEN all three exist
    When I Run Python Code "from lynx_mining.export import ExportFormat; print(ExportFormat.TXT.value, ExportFormat.HTML.value, ExportFormat.PDF.value)"
    Then The Exit Code Should Be 0
    Then The Output Should Contain "txt html pdf"

About Text Structure
    [Documentation]    GIVEN the package WHEN I get about text THEN it has all required fields
    When I Run Python Code "from lynx_mining import get_about_text; a = get_about_text(); assert all(k in a for k in ['name','suite','version','author','license','description']); print('OK')"
    Then The Exit Code Should Be 0
    Then The Output Should Contain "OK"
