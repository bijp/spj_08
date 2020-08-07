*** Settings ***
Library    pylib.TeacherLib
Variables   cfg.py

Suite Setup    add teacher    tuobajun   拓跋俊
           ...  ${g_subject_math_id}
           ...  ${suite_g7c1_classid}
           ...  13100000001  1301@g.com  320520001
           ...  suite_math_teacher_id

Suite Teardown    delete teacher   ${suite_math_teacher_id}
