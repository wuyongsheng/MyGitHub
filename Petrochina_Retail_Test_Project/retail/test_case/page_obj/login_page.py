#----------------------------------
'''                                                           
代码说明：登录页面
编写日期：2018.08.13
设计  者：linux超
'''
#----------------------------------

from .base_page import Base_Page

class Login_Page(Base_Page):

    # 输入用户名
    def input_username_text(self, username='rmln'):
        self.find_ele_by_id('username').send_keys(username)

    # 输入密码
    def input_password_text(self, password='a'):
        self.find_ele_by_id('password').send_keys(password)

    # 登录按钮
    def click_login_button(self, login_button='loginSubmitButton'):
        self.find_ele_by_id(login_button).click()

    # 登录失败时提示
    def login_failed_text(self, failed_button = 'inputTdRight'):
        return self.find_ele_by_id(failed_button).text

    # 登录失败时弹出的alert
    def handle_alert(self):
        alert = self.driver.switch_to_alert()
        text = alert.text
        alert.accept()
        return text

    # 统一登录函数
    def login_function(self, username='rmln', password='qwert1234!@#$'):
        self.input_username_text(username)
        self.input_password_text(password)
        self.click_login_button()

if __name__ == '__main__':
    pass