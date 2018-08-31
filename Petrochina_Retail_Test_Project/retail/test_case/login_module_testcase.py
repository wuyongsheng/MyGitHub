#----------------------------------
'''                                                           
代码说明：登录模块测试用例
编写日期：2018.08.13
设计  者：linux超
'''
#----------------------------------

from .models.myunit import Myunittest
from .models.login_function import Login_function_public
from .page_obj.login_page import Login_Page
from selenium.common import exceptions
import time

class Login_Test_Cases(Myunittest):

    # ............................................................................................#
    # test case 1: 正确的用户名和密码-登录成功
    def test_login_success_correct_username_password(self):
        self.login.login_function()
        curr_url = self.driver.current_url # 获取当前的url地址 为了断言是否登录成功
        self.assertIn('main', curr_url, '登录失败')

    # ............................................................................................#
    # test case 2: 错误的用户名 正确的密码-登录失败
    def test_login_failed_incorrect_username(self):
        self.login.login_function('rmlv', 'qwert1234!@#$')
        #time.sleep(5)
        login_failed = self.login.login_failed_text()
        self.assertIn('输入的用户名或密码错误', login_failed, '提示信息错误')

    # ............................................................................................#
    # test case 3：正确的用户名 错误的密码-登录失败
    def test_login_failed_incorrect_password(self):
        self.login.login_function('rmln', 'qwert1234!@#')
        #time.sleep(5)
        login_failed = self.login.login_failed_text()
        self.assertIn('输入的用户名或密码错误', login_failed, '提示信息错误')

    # ............................................................................................#
    # test case 4：用户名和密码为空
    def test_login_failed_username_password_blank(self):
        self.login.login_function('', '')
        #time.sleep(5)
        login_failed = self.login.handle_alert() # 获取alert的提示信息
        self.assertEqual('请填写用户名', login_failed, '提示信息错误')

    # ............................................................................................#
    # test case 5: 密码为空的
    def test_login_failed_password_blank(self):
        self.login.login_function('rmln', '')
        #time.sleep(5)
        login_failed = self.login.handle_alert() # 获取alert的提示信息
        self.assertEqual('请填写用户密码', login_failed, '提示信息错误')
    # ............................................................................................#

if __name__ == '__main__':
    pass
