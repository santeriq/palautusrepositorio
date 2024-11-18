*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  santeri
    Set Password  santeri123
    Set Password Confirmation  santeri123
    Create Account
    Account Creation Should Succeed

Register With Too Short Username And Valid Password
# ...

Register With Valid Username And Too Short Password
# ...

Register With Valid Username And Invalid Password
# salasana ei sisällä halutunlaisia merkkejä
# ...

Register With Nonmatching Password And Password Confirmation
# ...

Register With Username That Is Already In Use



*** Keywords ***
Create Account
    Click Button  Register

Account Creation Should Succeed
    Main Page Should Be Open