'''
Code description：会员档案查询 page
Create time：
Developer：
'''

from retail.test_case.page_obj.base_page import queryData
import time
from selenium.webdriver.common.by import By
import logging
import sys
from retail.test_case.page_obj.modifypw_page import PrimaryMenu, eleData
from retail.test_case.models.log import Logger

log = Logger(__name__, CmdLevel=logging.INFO, FileLevel=logging.INFO)


class MemberQuery(PrimaryMenu):
    """

    """
    # 测试数据: 会员编码, 会员姓名, 手机号码
    valuesList = [queryData.readExcel(1, 1), int(queryData.readExcel(2, 1)), queryData.readExcel(3, 1)]

    # 会员档案下拉菜单
    memberMenu = (By.LINK_TEXT, eleData.readExcel(24, 3))

    # 会员查询页面的3个列表(查询条件，会员信息明细，积分变化明细)
    uiElements = (By.XPATH, eleData.readExcel(25, 3))
    # 会员类型
    memberTypeBtn = (By.ID, eleData.readExcel(26, 3))
    # 会员类型下拉选项
    memberTypeNum = [(By.XPATH, eleData.readExcel(27, 3)), (By.XPATH, eleData.readExcel(28, 3)),
                     (By.XPATH, eleData.readExcel(29, 3))]

    # 会员级别
    memberLevelBtn = (By.ID, eleData.readExcel(30, 3))
    # 会员级别下拉选项
    memberLevelNum = [(By.XPATH, eleData.readExcel(31, 3)), (By.XPATH, eleData.readExcel(32, 3)),
                      (By.XPATH, eleData.readExcel(33, 3)), (By.XPATH, eleData.readExcel(34, 3))]

    # 会员编号，会员姓名，手机号码
    memberNumNamePhone = [(By.ID, eleData.readExcel(35, 3)), (By.ID, eleData.readExcel(36, 3)),
                          (By.ID, eleData.readExcel(37, 3))]
    # 查询异常提示框
    qFailerr = (By.XPATH, eleData.readExcel(38, 3))  # 查询失败弹出的错误提示框

    confirmBtn = (By.XPATH, eleData.readExcel(39, 3))

    # 查询与重置
    queryResetBtn = [(By.ID, eleData.readExcel(40, 3)), (By.ID, eleData.readExcel(41, 3))]

    # 点击会员类型
    def selectMemberType(self):
        """

        :return:
        """
        try:
            self.findElement(*self.memberTypeBtn).click()
            self.driver.implicitly_wait(2)
        except Exception:
            log.logger.exception('selecting member type fail ')
            raise
        else:
            log.logger.info('---selecting member type ')

    # 点击会员级别
    def selectMemberLevel(self):
        """

        :return:
        """
        try:
            self.findElement(*self.memberLevelBtn).click()
            self.driver.implicitly_wait(2)
        except Exception:
            log.logger.exception('selecting member level fail ')
            raise
        else:
            log.logger.info('---selecting member level ')

    # 查找会员档案查询菜单
    def memberQueryMenu(self):
        """

        :return:
        """
        self.findElement(*self.menuList[1]).click()
        self.findElement(*self.memberMenu).click()
        time.sleep(4)
        log.logger.info('page [%s] :found the menu [%s] and [%s]' % (
            sys._getframe().f_code.co_name, self.menuList[1], self.memberMenu))

    # 会员类型/会员级别下拉选项
    def memberTypeLevelOption(self, *xpathList):
        """

        :param xpath_list:
        :return:
        """
        try:
            member_type_level = self.findElement(*xpathList)
            text = member_type_level.text
        except Exception:
            log.logger.exception('get element member type/level item text fail', exc_info=True)
            raise
        else:
            log.logger.info('get element [%s] member type/level item text [%s] fail' % (xpathList, text))
            return text, member_type_level

    # 点击查询和重置按钮
    def cQueryResetBtn(self, *queryResetBtn):
        """

        :param query_reset_btn:
        :return:
        """
        try:
            self.findElement(*queryResetBtn).click()
        except Exception:
            log.logger.exception('query/reset button not click', exc_info=True)
            raise
        else:
            log.logger.info('clicking query/reset button ')

    # 输入查询条件
    def iQueryCondition(self, numNamePhone, value):
        """

        :param numNamePhone:
        :param value:
        :return:
        """
        number_name_phone = self.findElement(*numNamePhone)
        try:
            number_name_phone.clear()
            number_name_phone.send_keys(value)
        except Exception:
            log.logger.exception('input value error', exc_info=True)
            raise
        else:
            log.logger.info('[%s] is typing value [%s] ' % (numNamePhone, value))

    # 获取条件输入框的内容
    def getInputboxValue(self, *memberNumNamePhone):
        """

        :param memberNumNamePhone:
        :return:
        """
        try:
            get_member_number_name_phone_text = self.findElement(*memberNumNamePhone)
            text = get_member_number_name_phone_text.get_attribute('value')
        except Exception:
            log.logger.exception('get value of element fail', exc_info=True)
            raise
        else:
            log.logger.info('get value [%s] of element [%s] success' % (memberNumNamePhone, text))
            return text

    # 重置功能的重写
    def reset(self):
        """

        :return:
        """
        try:
            self.findElement(*self.memberNumNamePhone[0]).clear()
            self.findElement(*self.memberNumNamePhone[1]).clear()
            self.findElement(*self.memberNumNamePhone[2]).clear()
        except Exception:
            log.logger.exception('reset fail', exc_info=True)
            raise
        else:
            log.logger.info('reset [%s]-[%s]-[%s] success' % (
                self.memberNumNamePhone[0], self.memberNumNamePhone[1], self.memberNumNamePhone[2]))


if __name__ == '__main__':
    pass
