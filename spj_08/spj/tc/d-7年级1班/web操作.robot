*** Settings ***
Library  pylib.WebOpLibShare
Library  pylib.WebOpLibTeacher
Library  pylib.WebOpLibStudent
Library  pylib.TeacherLib
Library    pylib.StudentLib
Variables  cfg.py

Suite Setup   open browser
Suite Teardown   close browser


*** Test Cases ***
老师登录1 - tc005001

    ${addRet}=  add teacher    tuobajun   拓跋俊
           ...  ${g_subject_math_id}
           ...  ${suite_g7c1_classid}
           ...  13100000001  1301@g.com  320520001

    should be true  $addRet['retcode']==0


    teacher login   tuobajun   888888

    ${teacherinfo}=  get_teacher_homepage_info
    ${eteacherinfo}=  create list  松勤学院0001   拓跋俊
                  ...  初中数学   0   0   0

    should be equal   ${teacherinfo}    ${eteacherinfo}


    ${classstudent}=  get_teacher_class_students_info
    should be true   $classstudent=={'七年级1班':[]}

    [Teardown]  delete teacher   &{addRet}[id]


学生登录1 - tc005081

    ${addRet}=  add student   xiexuan   谢玄
        ...  ${g_grade_7_id}
        ...  ${suite_g7c1_classid}    13200000001

    should be true  $addRet['retcode']==0


    student login   xiexuan   888888

    ${studentinfo}=  get_student_homepage_info
    ${estudentinfo}=  create list   谢玄    松勤学院0001   0  0

    should be equal   ${studentinfo}    ${estudentinfo}


    ${wrongquestioninfo}=  get_student_wrongquestions
    should be equal   ${wrongquestioninfo}    您尚未有错题入库哦

    [Teardown]  delete student   &{addRet}[id]
