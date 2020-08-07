
from spj.pylib.MobileOpLibShare import Mobile_SHARE


class MobileOpLibAdmin:
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def vcode_login(self,vcode):

        code = 'new UiSelector().text("请输入vcode")'
        ele = Mobile_SHARE.wd.find_element_by_android_uiautomator(code)
        ele.send_keys(vcode)


        code = 'new UiSelector().text("登录")'
        ele = Mobile_SHARE.wd.find_element_by_android_uiautomator(code)
        ele.click()

        eles = Mobile_SHARE.wd.find_elements_by_id('android:id/alertTitle')
        # 找到报错窗口，登录失败
        if eles:
            errInfo = Mobile_SHARE.wd.find_element_by_id('android:id/message').text
            print(errInfo)
            return False,errInfo

        return True,''











git@github.com:bijp/spj_08.git