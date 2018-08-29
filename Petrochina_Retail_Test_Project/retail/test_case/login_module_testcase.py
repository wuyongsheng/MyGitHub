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
        Login_function_public(self.driver,userid='username',passwordid='password')
        time.sleep(5)
        curr_url = self.driver.current_url # 获取当前的url地址 为了断言是否登录成功
        self.assertIn('main', curr_url, '登录成功')

    # ............................................................................................#
    # test case 2: 错误的用户名 正确的密码-登录失败
    def test_login_failed_incorrect_username(self):
        login = Login_Page(self.driver)
        #login.login_function('rmlv','qwert1234!@#$') # 错误的用户名正确的密码登录
        Login_function_public(self.driver, userid='username', passwordid='password', username='rmlv', password='qwert1234!@#$')
        time.sleep(5)
        try:
            login_failed_get_text = login.login_failed_text()
            self.assertIn('输入的用户名或密码错误', login_failed_get_text, '登录失败')
            print(login_failed_get_text)
        except exceptions.NoSuchElementException as e:
            print(e)

    # ............................................................................................#
    # test case 3：正确的用户名 错误的密码-登录失败
    def test_login_failed_incorrect_password(self):
        login = Login_Page(self.driver)
        Login_function_public(self.driver, userid='username', passwordid='password', username='rmln',
                              password='qwert1234!@#')
        time.sleep(5)
        try:
            login_failed_get_text = login.login_failed_text()
            self.assertIn('输入的用户名或密码错误', login_failed_get_text, '登录失败')
            print(login_failed_get_text)
        except exceptions.NoSuchElementException as e:
            print(e)

    # ............................................................................................#
    # test case 4：用户名和密码为空
    def test_login_failed_username_password_blank(self):
        login = Login_Page(self.driver)
        Login_function_public(self.driver, userid='username', passwordid='password', username='',
                              password='')
        time.sleep(5)
        try:
            login_failed_get_text = login.handle_alert() # 获取alert的提示信息
            self.assertEqual('请填写用户名', login_failed_get_text, '登录失败')
            print(login_failed_get_text)
        except exceptions.NoSuchElementException as e:
            print(e)

    # ............................................................................................#
    # test case 5: 密码为空的
    def test_login_failed_password_blank(self):
        login = Login_Page(self.driver)
        Login_function_public(self.driver, userid='username', passwordid='password', username='rmln',
                              password='')
        time.sleep(5)
        try:
            login_failed_get_text = login.handle_alert() # 获取alert的提示信息
            self.assertEqual('请填写用户密码', login_failed_get_text, '登录失败')
            print(login_failed_get_text)
        except exceptions.NoSuchElementException as e:
            print(e)
    # ............................................................................................#

if __name__ == '__main__':
    pass
