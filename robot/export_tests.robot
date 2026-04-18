*** Settings ***
Documentation    Export workflow tests for lynx-mining
Library          Process
Library          OperatingSystem

*** Variables ***
${PYTHON}        python3
${MODULE}        lynx_mining

*** Keywords ***
Run App
    [Arguments]    @{args}
    ${result}=    Run Process    ${PYTHON}    -m    ${MODULE}    @{args}    timeout=120s
    Set Test Variable    ${OUTPUT}    ${result.stdout}${result.stderr}
    Set Test Variable    ${RC}    ${result.rc}

Given A Fresh Test Cache
    Run App    -t    --drop-cache    ALL

When I Analyze And Export "${ticker}" As "${format}"
    Run App    -t    ${ticker}    --no-reports    --no-news    --export    ${format}

Then The Exit Code Should Be ${expected}
    Should Be Equal As Integers    ${RC}    ${expected}

Then The Output Should Contain "${text}"
    Should Contain    ${OUTPUT}    ${text}

*** Test Cases ***
Export TXT Report
    [Documentation]    GIVEN clean cache WHEN I export as TXT THEN file is created
    Given A Fresh Test Cache
    When I Analyze And Export "UUUU" As "txt"
    Then The Exit Code Should Be 0
    Then The Output Should Contain "Exported to"

Export HTML Report
    [Documentation]    GIVEN clean cache WHEN I export as HTML THEN file is created
    Given A Fresh Test Cache
    When I Analyze And Export "UUUU" As "html"
    Then The Exit Code Should Be 0
    Then The Output Should Contain "Exported to"
