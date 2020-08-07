*** Settings ***
Library    pylib.TeacherLib
Variables   cfg.py


*** Test Cases ***
添加老师1 - tc001001
# 添加 老师
    ${addRet}=    add teacher    tuobaguang   拓跋光
                ...  ${g_subject_math_id}
                ...  ${suite_g7c1_classid}
                ...  13100000003  1303@g.com  320520003

    should be true     $addRet['retcode']==0

#列出老师，检验一下
    ${listRet}=    list teacher

    teacherlist should contain   &{listRet}[retlist]
                 ...  tuobaguang   拓跋光   &{addRet}[id]
                 ...   ${suite_g7c1_classid}
                 ...  13100000003  1303@g.com  320520003

    [Teardown]    delete teacher   &{addRet}[id]
