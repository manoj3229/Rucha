*** Settings ***
Library     ../libraries/BluetoothLibrary.py
Resource    ../resources/variables.robot

*** Keywords ***

Validate Device Connection

    ${device}=    Check Device Connection

    Log    Connected Device: ${device}

Turn ON Bluetooth

    Enable Bluetooth

Validate Bluetooth Enabled

    ${status}=    Verify Bluetooth Status

    Should Be Equal
    ...    ${status}
    ...    ${EXPECTED_STATUS}

Capture Device Logs

    Capture Logcat

Turn OFF Bluetooth

    Disable Bluetooth