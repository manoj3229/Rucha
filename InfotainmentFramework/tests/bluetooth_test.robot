*** Settings ***
Resource    ../keywords/bluetooth_keywords.robot

*** Test Cases ***

Bluetooth Validation Test

    [Documentation]
    ...    Validate infotainment Bluetooth flow

    [Tags]
    ...    regression
    ...    bluetooth

    Validate Device Connection

    Turn ON Bluetooth

    Validate Bluetooth Enabled

    Capture Device Logs

    Turn OFF Bluetooth