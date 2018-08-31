#----------------------------------
'''                                                           
代码说明：登录页面
编写日期：2018.08.13
设计  者：linux超
'''
#----------------------------------

from .base_page import Base_Page
from selenium.webdriver.common.by import By
class Login_Page(Base_Page):


    """用户名，密码，登录按钮，保存信息，错误提示"""
    username_element = (By.ID,'username')
    password_eleemnt = (By.ID,'password')
    loginbtn_element = (By.ID,'loginSubmitButton')
    save_info_element = (By.NAME,'checkcookie')
    error_message = (By.ID,'inputTdRight')

    """登录成功判断"""
    login_succ= (By.XPATH,'/html/body/section/header/div/span')

    """登录异常"""
    login_error = \
        (By.ID,'inputTdRight')


    # 输入用户名
    def input_username_text(self,username):
        element = self.find_element_re(*self.username_element)
        element.send_keys(username)

    # 输入密码
    def input_password_text(self,password):
        element = self.find_element_re(*self.password_eleemnt)
        element.send_keys(password)

    # 登录按钮
    def click_login_button(self):
        element = self.find_element_re(*self.loginbtn_element)
        element.click()

    # 登录失败时提示
    def login_failed_text(self):
        return self.find_element_re(*self.error_message).text

    # 登录失败时弹出的alert
    def handle_alert(self):
        try:
            alert = self.driver.switch_to_alert()
            text = alert.text
            alert.accept()
            return text
        except:
            return ''

    # 统一登录函数
    def login_function(self, username='rmln', password='qwert1234!@#$'):
        self.input_username_text(username)
        self.input_password_text(password)
        self.click_login_button()

if __name__ == '__main__':
    pass