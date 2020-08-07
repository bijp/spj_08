*** Settings ***
Library    pylib.StudentLib
Variables   cfg.py


*** Test Cases ***
添加学生1 - tc002001
    ${addRet}=   add student   xielingyun2   谢灵运2
        ...  ${g_grade_7_id}
        ...  ${suite_g7c1_classid}    13200000002

    Should be true   $addRet["retcode"]==0


    ${listRet}=   list student

    studentlist should contain   &{listRet}[retlist]
        ...  xielingyun2   谢灵运2    &{addRet}[id]
        ...  13200000002    ${suite_g7c1_classid}

    [Teardown]  delete student   &{addRet}[id]

