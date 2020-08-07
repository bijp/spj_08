*** Settings ***
Library   pylib.MobileOpLibShare
Library   pylib.MobileOpLibAdmin

Suite Setup  open_mobile
Suite Teardown  close_mobile

*** Test Cases ***
vcode登录1 - tc006001

    ${ret}  ${info}    vcode_login   xxxxxx

    should be true   $ret==False
    should be true   $info=='登录失败 : vcode format error:1'

