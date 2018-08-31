# ----------------------------------
'''                                                           
代码说明： Myunittest类 继承unittest.TestCase初始化测试用例
编写日期： 2018.08.13
设计  者： linux超
'''
# ----------------------------------
from .driver import Web_Driver
import unittest
import time
from retail.test_case.page_obj.login_page import Login_Page
from retail.test_case.page_obj.login_page import Base_Page

class Myunittest(unittest.TestCase):

    def setUp(self):
        self.driver = Web_Driver().firefox_driver()
        self.driver.maximize_window()
        self.login = Login_Page(self.driver)
        self.login.open()

    def tearDown(self):
        self.driver.quit()
        #pass

if __name__ == '__main__':
    unittest.main()
