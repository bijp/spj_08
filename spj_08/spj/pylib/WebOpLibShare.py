from selenium import webdriver



class WEB_SHARE:
    wd = None

def open_browser():
    WEB_SHARE.wd = webdriver.Chrome()
    WEB_SHARE.wd.implicitly_wait(10)

def close_browser():
    WEB_SHARE.wd.quit()