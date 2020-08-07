*** Settings ***
Library  pylib.WebOpLibShare
Library  pylib.WebOpLibTeacher
Library  pylib.WebOpLibStudent
Variables  cfg.py

Suite Setup   open browser
Suite Teardown   close browser


*** Test Cases ***
老师发布作业1 - tc005101



    teacher_login    tuobajun   888888
    teacher_deliver_task     测试作业第3个


    student_login     xiexuan   888888
    studentDoExam



    teacher_login    tuobajun   888888
    ${choices}=    teacher_get_latest_student_task

    should be true     $choices==['A', 'A', 'A']


