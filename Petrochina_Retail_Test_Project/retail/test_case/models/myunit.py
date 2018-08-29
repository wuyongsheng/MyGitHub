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


class Myunittest(unittest.TestCase):

    def setUp(self):
        self.driver = Web_Driver().firefox_driver()
        self.driver.maximize_window()
        Web_Driver().load_url(self.driver, 'http://11.11.164.134:9081/rmms/modules/ep.rmms.portal/login/login.jsp')
        time.sleep(5)

    def tearDown(self):
        #self.driver.quit()
        pass

if __name__ == '__main__':
    unittest.main()
