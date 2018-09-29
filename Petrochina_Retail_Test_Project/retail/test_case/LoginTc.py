"""
Code description：login testcase
Create time：
Developer：
"""

import unittest
import time
import logging
import sys
from retail.test_case.models.myunit import MyunitTest
from retail.test_case.models.log import Logger

log = Logger(__name__, CmdLevel=logging.INFO, FileLevel=logging.INFO)

class Login_TC(MyunitTest):

    """登录模块测试用例"""

    def test_login_success_correct_username_password(self):
        """用户名正确,密码正确,登录成功"""
        self.login.loginFunc()
        currUrl = self.driver.current_url # 获取当前的url地址
        try:
            self.assertIn('main', currUrl, 'main not in current url!')
        except Exception:
            self.login.saveScreenShot('correct_username_password_fail.png')
            raise
        else:
            self.login.saveScreenShot('correct_username_password_pass.png')
            log.logger.info('%s->run completed! please check the test report' % (sys._getframe().f_code.co_name))

    def test_login_failed_incorrect_username(self):
        """用户名错误,密码正确,登录失败"""

        self.login.loginFunc(self.login.unpwData[1][0], self.login.unpwData[1][1])
        failText = self.login.getFailedText()
        self.assertEqual('输入的用户名或密码错误，请重新输入!', failText, '提示信息错误')
        log.logger.info('%s->run completed! please check the test report' % (sys._getframe().f_code.co_name))

    def test_login_failed_incorrect_password(self):

        """用户名正确,密码错误,登录失败"""

        self.login.loginFunc(self.login.unpwData[5][0], self.login.unpwData[5][1])
        failText = self.login.getFailedText()
        self.assertEqual('输入的用户名或密码错误，请重新输入!', failText, '提示信息错误')
        log.logger.info('%s->run completed! please check the test report' % (sys._getframe().f_code.co_name))

    def test_login_failed_username_password_blank(self):
        """用户名为空,密码为空,登录失败"""

        self.login.loginFunc(self.login.unpwData[6][0], self.login.unpwData[6][1])
        failText = self.login.handleAlert() # 获取alert的提示信息
        self.assertEqual('请填写用户名', failText, '提示信息错误')
        log.logger.info('%s->run completed! please check the test report' % (sys._getframe().f_code.co_name))

    def test_login_failed_password_blank(self):
        """用户名正确,密码为空,登录失败"""

        self.login.loginFunc(self.login.unpwData[4][0], self.login.unpwData[4][1])
        failText = self.login.handleAlert() # 获取alert的提示信息
        self.assertEqual('请填写用户密码', failText, '提示信息错误')
        log.logger.info('%s->run completed! please check the test report' % (sys._getframe().f_code.co_name))

    def test_login_failed_unpw_incorrect(self):
        """用户名错误,密码错误,登录失败"""
        # try:
        self.login.loginFunc(self.login.unpwData[3][0], self.login.unpwData[4][0])
        failText = self.login.getFailedText()
        self.assertEqual ('输入的用户名或密码错误，请重新输入!', failText, 'failed')
        log.logger.info('%s->run completed! please check the test report' % (sys._getframe().f_code.co_name))

    def test_login(self):
        """循环测试登录功能"""
        for listitem in self.login.unpwData:
            self.login.inputValue(self.login.userNameEle,listitem[0])
            time.sleep(2)
            self.login.inputValue(self.login.passWordEle,listitem[1])
            time.sleep(2)
            self.login.clickLoginBtn()
            time.sleep(2)
            if listitem[0] =='rmln' and listitem[1] == 'qwert1234!@#':
                currUrl = self.driver.current_url
                self.assertIn ('main' , currUrl)
                self.login.quit()
            elif listitem[0] == 'rmln' and listitem[1] != 'qwert1234!@#':
                if listitem[1] == '':
                    failText = self.login.handleAlert()  # 获取alert的提示信息
                    self.assertEqual('请填写用户密码', failText, '提示信息错误')
                else:
                    failText = self.login.getFailedText()
                    self.assertEqual('输入的用户名或密码错误，请重新输入!', failText, '提示信息错误')
            elif listitem[0] != 'rmln' and listitem[1] == 'qwert1234!@#':
                if listitem[0]=='':
                    failText = self.login.handleAlert()  # 获取alert的提示信息
                    self.assertEqual('请填写用户名', failText, '提示信息错误')
                else:
                    failText = self.login.getFailedText()
                    self.assertEqual('输入的用户名或密码错误，请重新输入!', failText, '提示信息错误')
            elif listitem[0] == listitem[1] == '':
                failText = self.login.handleAlert()  # 获取alert的提示信息
                self.assertEqual('请填写用户名', failText, '提示信息错误')
            else:
                failText = self.login.getFailedText()
                self.assertEqual('输入的用户名或密码错误，请重新输入!', failText, '提示信息错误')
        log.logger.info('%s->run completed! please check the test report' % (sys._getframe().f_code.co_name))

if __name__ == '__main__':
    unittest.main()


