*** Settings ***
Documentation    CLI integration tests for lynx-mining
Library          Process
Library          OperatingSystem

*** Variables ***
${PYTHON}        python3
${APP}           -m lynx_mining

*** Keywords ***
Given The Application Is Available
    ${result}=    Run Process    ${PYTHON}    ${APP}    --version
    Should Contain    ${result.stdout}    lynx-mining

When I Run The Help Command
    ${result}=    Run Process    ${PYTHON}    ${APP}    -p    --help
    Set Test Variable    ${OUTPUT}    ${result.stdout}
    Set Test Variable    ${RC}    ${result.rc}

When I Run About
    ${result}=    Run Process    ${PYTHON}    ${APP}    --about
    Set Test Variable    ${OUTPUT}    ${result.stdout}${result.stderr}
    Set Test Variable    ${RC}    ${result.rc}

When I Run Version
    ${result}=    Run Process    ${PYTHON}    ${APP}    --version
    Set Test Variable    ${OUTPUT}    ${result.stdout}
    Set Test Variable    ${RC}    ${result.rc}

When I Explain Metric "${metric}"
    ${result}=    Run Process    ${PYTHON}    ${APP}    --explain    ${metric}
    Set Test Variable    ${OUTPUT}    ${result.stdout}${result.stderr}
    Set Test Variable    ${RC}    ${result.rc}

When I List All Metrics
    ${result}=    Run Process    ${PYTHON}    ${APP}    --explain
    Set Test Variable    ${OUTPUT}    ${result.stdout}${result.stderr}
    Set Test Variable    ${RC}    ${result.rc}

When I Explain Section "${section}"
    ${result}=    Run Process    ${PYTHON}    ${APP}    --explain-section    ${section}
    Set Test Variable    ${OUTPUT}    ${result.stdout}${result.stderr}
    Set Test Variable    ${RC}    ${result.rc}

When I Explain Conclusion "${category}"
    ${result}=    Run Process    ${PYTHON}    ${APP}    --explain-conclusion    ${category}
    Set Test Variable    ${OUTPUT}    ${result.stdout}${result.stderr}
    Set Test Variable    ${RC}    ${result.rc}

When I Analyze "${ticker}" In Testing Mode
    ${result}=    Run Process    ${PYTHON}    ${APP}    -t    ${ticker}    --no-reports    --no-news
    ...    timeout=120s
    Set Test Variable    ${OUTPUT}    ${result.stdout}${result.stderr}
    Set Test Variable    ${RC}    ${result.rc}

When I Search For "${query}"
    ${result}=    Run Process    ${PYTHON}    ${APP}    -p    -s    ${query}
    ...    timeout=30s
    Set Test Variable    ${OUTPUT}    ${result.stdout}${result.stderr}
    Set Test Variable    ${RC}    ${result.rc}

When I List Cache In Testing Mode
    ${result}=    Run Process    ${PYTHON}    ${APP}    -t    --list-cache
    Set Test Variable    ${OUTPUT}    ${result.stdout}${result.stderr}
    Set Test Variable    ${RC}    ${result.rc}

When I Drop All Cache In Testing Mode
    ${result}=    Run Process    ${PYTHON}    ${APP}    -t    --drop-cache    ALL
    Set Test Variable    ${OUTPUT}    ${result.stdout}${result.stderr}
    Set Test Variable    ${RC}    ${result.rc}

When I Export "${ticker}" As "${format}" In Testing Mode
    ${result}=    Run Process    ${PYTHON}    ${APP}    -t    ${ticker}    --no-reports    --no-news    --export    ${format}
    ...    timeout=120s
    Set Test Variable    ${OUTPUT}    ${result.stdout}${result.stderr}
    Set Test Variable    ${RC}    ${result.rc}

Then The Exit Code Should Be ${expected}
    Should Be Equal As Integers    ${RC}    ${expected}

Then The Output Should Contain "${text}"
    Should Contain    ${OUTPUT}    ${text}

Then The Output Should Not Contain "${text}"
    Should Not Contain    ${OUTPUT}    ${text}

*** Test Cases ***
Show Help
    [Documentation]    GIVEN the app is available WHEN I run help THEN it shows usage
    Given The Application Is Available
    When I Run The Help Command
    Then The Exit Code Should Be 0
    Then The Output Should Contain "lynx-mining"
    Then The Output Should Contain "production-mode"
    Then The Output Should Contain "testing-mode"
    Then The Output Should Contain "--gui"
    Then The Output Should Contain "--export"

Show Version
    [Documentation]    GIVEN the app WHEN I run version THEN it shows version info
    Given The Application Is Available
    When I Run Version
    Then The Exit Code Should Be 0
    Then The Output Should Contain "lynx-mining"
    Then The Output Should Contain "1.0"

Show About
    [Documentation]    GIVEN the app WHEN I run about THEN it shows author and license
    Given The Application Is Available
    When I Run About
    Then The Exit Code Should Be 0
    Then The Output Should Contain "Lynx Basic Materials Analysis"
    Then The Output Should Contain "Borja Tarraso"
    Then The Output Should Contain "BSD-3-Clause"
    Then The Output Should Contain "Lince Investor Suite"

Explain A Valuation Metric
    [Documentation]    GIVEN the app WHEN I explain a metric THEN it shows details
    Given The Application Is Available
    When I Explain Metric "cash_to_market_cap"
    Then The Exit Code Should Be 0
    Then The Output Should Contain "Cash-to-Market-Cap"
    Then The Output Should Contain "explorers"

Explain A Mining-Specific Metric
    [Documentation]    GIVEN the app WHEN I explain shares_growth_yoy THEN it shows dilution info
    Given The Application Is Available
    When I Explain Metric "shares_growth_yoy"
    Then The Exit Code Should Be 0
    Then The Output Should Contain "Share Dilution"
    Then The Output Should Contain "junior miners"

List All Available Metrics
    [Documentation]    GIVEN the app WHEN I list metrics THEN it shows the full table
    Given The Application Is Available
    When I List All Metrics
    Then The Exit Code Should Be 0
    Then The Output Should Contain "pe_trailing"
    Then The Output Should Contain "cash_to_market_cap"
    Then The Output Should Contain "quality_score"

Explain A Section
    [Documentation]    GIVEN the app WHEN I explain a section THEN it shows section description
    Given The Application Is Available
    When I Explain Section "mining_quality"
    Then The Exit Code Should Be 0
    Then The Output Should Contain "Mining Quality"

Explain Conclusion Methodology
    [Documentation]    GIVEN the app WHEN I explain conclusion THEN it shows scoring method
    Given The Application Is Available
    When I Explain Conclusion "overall"
    Then The Exit Code Should Be 0
    Then The Output Should Contain "mining quality"

Search For A Company
    [Documentation]    GIVEN the app WHEN I search for a company THEN results are shown
    Given The Application Is Available
    When I Search For "uranium"
    Then The Exit Code Should Be 0
    Then The Output Should Contain "Search Results"

Drop All Test Cache
    [Documentation]    GIVEN the app WHEN I drop all test cache THEN it confirms
    Given The Application Is Available
    When I Drop All Cache In Testing Mode
    Then The Exit Code Should Be 0
    Then The Output Should Contain "Removed"
