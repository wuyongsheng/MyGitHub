'''
Code description： login page
Create time：
Developer：
'''

from selenium.webdriver.common.by import By
import logging
import sys
from retail.test_case.page_obj.base_page import BasePage, eleData, testLoginData
from retail.test_case.models.log import Logger

log = Logger(__name__, CmdLevel=logging.INFO, FileLevel=logging.INFO)


class LoginPage(BasePage):

    """用户名，密码，登录按钮，保存信息，错误提示"""
    userNameEle = (By.ID, eleData.readExcel(1, 3))
    passWordEle = (By.ID, eleData.readExcel(2, 3))
    loginBtnEle = (By.ID, eleData.readExcel(3, 3))
    saveInfoEle = (By.NAME, eleData.readExcel(4, 3))
    errorMessage = (By.ID, eleData.readExcel(5, 3))
    quitBtn = (By.ID, eleData.readExcel(6, 3))

    # 用户名和密码
    unpwData = \
        [[testLoginData.readExcel(1, 0), testLoginData.readExcel(1, 1)],# 正确的用户名和正确的密码
         [testLoginData.readExcel(2, 0), testLoginData.readExcel(2, 1)],# 错误的用户名和正确的密码
         [testLoginData.readExcel(3, 0), testLoginData.readExcel(3, 1)],# 空的用户名和正确的密码
         [testLoginData.readExcel(4, 0), testLoginData.readExcel(4, 1)],# 错误的用户名和错误的密码
         [testLoginData.readExcel(5, 0), testLoginData.readExcel(5, 1)],# 正确的用户名和空密码
         [testLoginData.readExcel(6, 0), testLoginData.readExcel(6, 1)],# 正确的用户名和错误的密码
         [testLoginData.readExcel(7, 0), testLoginData.readExcel(7, 1)]]# 空用户名和空密码


    # 登录按钮
    def clickLoginBtn(self):
        """

        :return:
        """
        element = self.findElement(*self.loginBtnEle)
        element.click()
        log.logger.info('%s ,logining....!' % sys._getframe().f_code.co_name)
    # 登录失败时提示
    def getFailedText(self):
        """

        :return:
        """
        info = self.findElement(*self.errorMessage).text
        log.logger.info('login failed : %s' %info)
        return info

    # 登录失败时弹出的alert
    def handleAlert(self):
        """

        :return:
        """
        try:
            alert = self.driver.switch_to_alert()
            text = alert.text
            alert.accept()
        except Exception:
            log.logger.exception('handle alert failed, please check the details' ,exc_info=True)
            raise
        else:
            log.logger.info('login failed ,%s handle alert successed alert info: %s!' %(sys._getframe().f_code.co_name, text))
            return text

    # 统一登录函数
    def loginFunc(self, username='rmln', password='qwert1234!@#'):
        """
        :param username:
        :param password:
        :return:
        """
        self.inputValue(self.userNameEle, username)
        self.inputValue(self.passWordEle, password)
        self.clickLoginBtn()

    # 清空输入框数据
    def clearValue(self, element):

        empty = self.findElement(*element)
        empty.clear()
        log.logger.info('emptying value.......')


    # 推出
    def quit(self):
        self.findElement(*self.quitBtn).click()
        log.logger.info('quit')

if __name__ == '__main__':
    pass