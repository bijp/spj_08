
from spj.cfg import *
import time

from spj.pylib.WebOpLibShare import WEB_SHARE


class WebOpLibStudent:
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'




    def student_login(self,username,password):
        WEB_SHARE.wd.get(g_student_login_url)
        WEB_SHARE.wd.find_element_by_id('username').send_keys(username)
        WEB_SHARE.wd.find_element_by_id('password').send_keys(password)
        WEB_SHARE.wd.find_element_by_id('submit').click()

        # 确保首页打开，登录成功
        WEB_SHARE.wd.find_element_by_id('div-home')

    def get_student_homepage_info(self):
        # 查看 a 元素发现其位置不是主页按钮位置
        WEB_SHARE.wd.find_element_by_css_selector("a[href='#/home']>li").click()
        # 确保首页打开
        WEB_SHARE.wd.find_element_by_id('div-home')

        # 由于数据是异步获取，需要sleep一段时间，假设需求是2秒必须获取数据
        time.sleep(2)

        eles = WEB_SHARE.wd.find_elements_by_css_selector('#div-home .ng-binding')

        eles.pop(2)

        return [ele.text for ele in eles]

    def get_student_wrongquestions(self):
        WEB_SHARE.wd.find_element_by_css_selector('a[href="#/yj_wrong_questions"] >li').click()

        # 由于数据是异步获取，需要sleep一段时间，假设需求是2秒必须获取数据
        time.sleep(2)

        return WEB_SHARE.wd.find_element_by_id('page-wrapper').text



    def  studentDoExam(self):
        WEB_SHARE.wd.find_element_by_css_selector('a[href="#/task_manage"] >li').click()

        # 由于数据是异步获取，需要sleep一段时间，假设需求是2秒必须获取数据
        time.sleep(2)

        # 点击打开第一个任务
        WEB_SHARE.wd.find_element_by_css_selector('button[ng-click*=viewTask]').click()

        # 全部选A
        firstAnwsers = WEB_SHARE.wd.find_elements_by_css_selector(
            '.btn-group button:nth-child(1)'
        )

        for one in firstAnwsers:
            one.click()

        WEB_SHARE.wd.find_element_by_css_selector('button[ng-click*=saveMyResult]').click()


        # 点击确定
        WEB_SHARE.wd.find_element_by_css_selector(
            'div.bootstrap-dialog  .bootstrap-dialog-footer-buttons  button:nth-child(2)'
        ).click()

        time.sleep(2)



if  __name__ == '__main__':
    wo = WebOpLib()
    wo.open_browser()



    wo.student_login('xiexuan','888888')
    wo.studentDoExam()



    wo.teacher_login('tuobajun','888888')
    wo.teacher_get_latest_student_task()