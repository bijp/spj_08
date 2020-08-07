from appium import webdriver




desired_caps = {
    'platformName': 'Android',
    'automationName': 'UIAutomator2',
    'platformVersion': '9',
    'deviceName': 'xxx',
    # 'app': r'd:\apk\toutiao.apk',
    'appPackage': 'com.yjyxapp',
    'appActivity': 'com.yjyxapp.MainActivity',
    # 'unicodeKeyboard': True,
    # 'resetKeyboard': True,
    'noReset': True,
    'newCommandTimeout': 6000,
}


class Mobile_SHARE:
    wd = None

# 创建webdrier对象，并打开app
def open_mobile():
    Mobile_SHARE.wd = webdriver.Remote('http://localhost:4723/wd/hub',
                                       desired_caps)
    Mobile_SHARE.wd.implicitly_wait(10)

def close_mobile():
    Mobile_SHARE.wd.quit()