*** Settings ***
Documentation    Export workflow tests for lynx-mining
Library          Process
Library          OperatingSystem

*** Variables ***
${PYTHON}        python3
${APP}           -m lynx_mining

*** Keywords ***
Given A Fresh Test Cache
    Run Process    ${PYTHON}    ${APP}    -t    --drop-cache    ALL

When I Analyze And Export "${ticker}" As "${format}"
    ${result}=    Run Process    ${PYTHON}    ${APP}    -t    ${ticker}    --no-reports    --no-news    --export    ${format}
    ...    timeout=120s
    Set Test Variable    ${OUTPUT}    ${result.stdout}${result.stderr}
    Set Test Variable    ${RC}    ${result.rc}

Then The Exit Code Should Be ${expected}
    Should Be Equal As Integers    ${RC}    ${expected}

Then The Output Should Contain "${text}"
    Should Contain    ${OUTPUT}    ${text}

Then An Export File Should Exist With Extension "${ext}"
    Should Contain    ${OUTPUT}    .${ext}

*** Test Cases ***
Export TXT Report
    [Documentation]    GIVEN a clean cache WHEN I analyze and export as TXT THEN a file is created
    Given A Fresh Test Cache
    When I Analyze And Export "UUUU" As "txt"
    Then The Exit Code Should Be 0
    Then The Output Should Contain "Exported to"
    Then An Export File Should Exist With Extension "txt"

Export HTML Report
    [Documentation]    GIVEN a clean cache WHEN I analyze and export as HTML THEN a file is created
    Given A Fresh Test Cache
    When I Analyze And Export "UUUU" As "html"
    Then The Exit Code Should Be 0
    Then The Output Should Contain "Exported to"
    Then An Export File Should Exist With Extension "html"
