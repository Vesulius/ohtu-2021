*** Settings ***
Resource  resource.robot
Resource  login_resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page
Test Teardown  Reset Application

*** Test Cases ***
Register With Valid Username And Password
    Set Username  tester
    Set Password  password1
    Set Confirmation  password1
    Submit Profile
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  hi
    Set Password  password1
    Set Confirmation  password1
    Submit Profile
    Register Should Fail With Message  Username must be at least 3 characters


Register With Valid Username And Too Short Password
    Set Username  tester
    Set Password  pass1
    Set Confirmation  pass1
    Submit Profile
    Register Should Fail With Message  Password must be at least 8 characters

Register With Nonmatching Password And Password Confirmation
    Set Username  tester    
    Set Password  password1
    Set Confirmation  wordpass1
    Submit Profile
    Register Should Fail With Message  Password and password confirmation did not match

Login After Successful Registration
    Set Username  tester
    Set Password  password1
    Set Confirmation  password1
    Submit Profile
    Register Should Succeed
    Go To Login Page
    Set Username  tester
    Set Password  password1
    Submit Credentials
    Login Should Succeed

** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Profile
    Click Button  Register

Set Confirmation
    [Arguments]  ${confirmation}
    Input Password  password_confirmation  ${confirmation}