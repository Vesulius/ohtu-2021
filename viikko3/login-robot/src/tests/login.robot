*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input New Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  tester  tester123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  tester123
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  hi  hello123
    Output Should Contain  Username must be at least 3 characters

Register With Valid Username And Too Short Password
    Input Credentials  tester  tes123
    Output Should Contain  Password must be at least 8 characters

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  tester  testerspassword
    Output Should Contain  Password cant consist of only letters

*** Keywords ***
Create User And Input New Command
    Create User  kalle  kalle123
    Input New Command
