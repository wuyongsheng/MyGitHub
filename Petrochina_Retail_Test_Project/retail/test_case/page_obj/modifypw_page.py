'''
Code description：modify password page
Create time：
Developer：
'''

import logging
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from retail.test_case.page_obj.base_page import BasePage, eleData, modifyPwData
from retail.test_case.models.log import Logger

log = Logger(__name__, CmdLevel=logging.INFO, FileLevel=logging.INFO)
class PrimaryMenu(BasePage):

    """密码数据"""
    pwdList = \
        [[modifyPwData.readExcel(1, 0), modifyPwData.readExcel(1, 1), modifyPwData.readExcel(1, 2)],
         [modifyPwData.readExcel(2, 0), modifyPwData.readExcel(2, 1), modifyPwData.readExcel(2, 2)],
         [modifyPwData.readExcel(3, 0), modifyPwData.readExcel(3, 1), modifyPwData.readExcel(3, 2)],
         [modifyPwData.readExcel(4, 0), modifyPwData.readExcel(4, 1), modifyPwData.readExcel(4, 2)],
         [modifyPwData.readExcel(5, 0), modifyPwData.readExcel(5, 1), modifyPwData.readExcel(5, 2)]]

    """权限管理下拉菜单"""
    menuPersonal = (By.LINK_TEXT, eleData.readExcel(15, 3))
    menuModifyPwd = (By.LINK_TEXT, eleData.readExcel(16, 3))

    """密码修改"""
    oldPwd = (By.ID, eleData.readExcel(17, 3))
    newPwd = (By.ID, eleData.readExcel(18, 3))
    commitPwd = (By.ID, eleData.readExcel(19, 3))

    """错误提示框及确定"""
    errMessage = (By.XPATH, eleData.readExcel(20, 3))
    closeBtn = (By.CSS_SELECTOR, eleData.readExcel(21, 3))

    """密码说明"""
    readMe = (By.ID, eleData.readExcel(22, 3))

    """保存"""
    saveBtn = (By.XPATH, eleData.readExcel(23, 3))

    #   主菜单
    def findMenu(self,*menuList):
        """

        :param menu_list:
        :return:
        """
        return self.findElement(*menuList)

    #   旧密码输入框
    def inputOldPw(self, oldPwd=''):
        """"""
        try:
            self.findElement(*self.oldPwd).clear()
            self.findElement(*self.oldPwd).send_keys(oldPwd)
        except Exception:
            log.logger.exception('input Pw [%s] for oldPw [%s] fail' %(oldPwd, self.oldPwd))
            raise
        else:
            log.logger.info('inputing Pw [%s] for oldPw [%s] ' % (oldPwd, self.oldPwd))
    #   新密码输入框
    def inputNewPw(self, newPwd=''):
        """

        :param newPwd:
        :return:
        """
        try:
            self.findElement(*self.newPwd).clear()
            self.findElement(*self.newPwd).send_keys(newPwd)
        except Exception:
            log.logger.exception('input Pw [%s] for newPw [%s] fail' % (newPwd, self.newPwd))
            raise
        else:
            log.logger.info('inputing Pw [%s] for newPw [%s] ' % (newPwd, self.newPwd))
    #   确认密码输入框
    def inputConfirmPw(self, confirmPwd=''):
        """

        :param confirmPwd:
        :return:
        """
        try:
            self.findElement(*self.commitPwd).clear()
            self.findElement(*self.commitPwd).send_keys(confirmPwd)
        except Exception:
            log.logger.exception('input Pw [%s] for commitPw [%s] fail' %(confirmPwd, self.commitPwd))
            raise
        else:
            log.logger.info('inputing Pw [%s] for commitPw [%s] ' %(confirmPwd, self.commitPwd))
    #   保存
    def saveButton(self):
        """

        :return:
        """
        try:
            self.driver.implicitly_wait(5)
            clickbutton = self.findElement(*self.saveBtn)
            time.sleep(1)
            clickbutton.click()
        except Exception:
            log.logger.exception('click save button fail')
            raise
        else:
            log.logger.info('clciking the button')

    #   修改密码功能菜单
    def modifyPwMenu(self):
        """

        :return:
        """
        try:
            self.findElement(*self.menuList[0]).click()
            self.findElement(*self.menuPersonal).click()
            self.findElement(*self.menuModifyPwd).click()
        except Exception:
            log.logger.exception('not found menu [%s]-[%s]-[%s]' %(self.menuList[0], self.menuPersonal, self.menuModifyPwd))
            raise
        else:
            log.logger.info('finding menu [%s]-[%s]-[%s]' %(self.menuList[0], self.menuPersonal, self.menuModifyPwd))
            self.driver.implicitly_wait(2)

    #   修改密码
    def modifyPw(self, list):
        """

        :param list:
        :return:
        """
        try:
            self.inputOldPw(list[0])
            self.inputNewPw(list[1])
            self.inputConfirmPw(list[2])
            self.saveButton()
        except Exception:
            log.logger.exception('input oldpw/newpw/commitpw [%s]/[%s]/[%s] fail' %(list[0], list[1], list[2]))
            raise
        else:
            log.logger.info('modifing pw [%s]/[%s]/[%s]' %(list[0], list[1], list[2]))

    #   错误提示框
    def errorDialog(self, commit_btn = (By.ID,'unieap_form_Button_1_unieap_input')):
        """
        :type commit_btn: 元祖
        """

        try:
            messages_frame = self.findElement(*self.errMessage)
            text = messages_frame.text
            element = self.findElement(*commit_btn)
            time.sleep(2)
            action = ActionChains(self.driver)
            action.move_to_element(element).perform()
            time.sleep(2)
            element.click()
            action.reset_actions() # 释放鼠标
        except Exception:
            log.logger.exception('close errMsgFram [%s] or get text [%s]fail' %(self.errMessage))
            raise
        else:
            log.logger.info('close errMsgFram [%s] and get text [%s] success' %(self.errMessage, text))
            return text

    # 关闭提示框
    def closeErrMsg(self, element):
        try:
            ele = self.findElement(*element)
            action = ActionChains(self.driver)
            action.move_to_element(ele).perform()
            time.sleep(2)
            ele.click()
            action.reset_actions()
        except Exception:
            log.logger.exception('close the err msg ifram fail', exc_info=True)
            raise
        else:
            log.logger.info('closing the err msg ifram success!')

if __name__ == '__main__':
    pass
