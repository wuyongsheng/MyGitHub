'''
Code description：积分规则/活动申请 page
Create time：
Developer：
'''

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import logging
import sys
from retail.test_case.page_obj.base_page import BasePage, eleData
from retail.test_case.models.log import Logger

log = Logger(__name__, CmdLevel=logging.INFO, FileLevel=logging.INFO)

class ActiveRule(BasePage):

    # 积分规则/活动申请 菜单
    itemMenu = (By.XPATH, eleData.readExcel(64, 3))

    # 测试数据:申请原因
    reason = time.strftime('%Y-%m-%d:%H:%M:%S') +'测试'
    valueList = [reason, reason+'name', 'test', '2018-09-10', '2018-09-10', '00:00:00', '23:59:59']

    # 申请类型
    typeBtn = (By.ID, eleData.readExcel(65, 3))
    typeItem = \
        [(By.XPATH, eleData.readExcel(66, 3)),# 积分累计规则
        (By.XPATH, "//*[@class='u-combobox-items-container']/table/tbody/tr[2]")] # 积分累计活动

    # 添加规则
    addruleBtn = (By.LINK_TEXT, eleData.readExcel(68, 3))
    # 删除规则
    deleruleBtn = (By.LINK_TEXT, eleData.readExcel(69, 3))
    # 保存申请
    saveBtn = (By.LINK_TEXT, eleData.readExcel(70, 3))
    # 提交申请
    submitBtn = (By.LINK_TEXT, eleData.readExcel(71, 3))

    # 申请类型未积分累计活动时，所有的必填输入项
    eleList = \
        [(By.ID, eleData.readExcel(72, 3)), # 申请原因
        (By.ID, eleData.readExcel(73, 3)), # 活动名称
        (By.ID, eleData.readExcel(74, 3)), # 活动描述
        (By.ID, eleData.readExcel(75, 3)), # 开始日期
        (By.ID, eleData.readExcel(76, 3)), # 结束日期
        (By.ID, eleData.readExcel(77, 3)), # 开始时间
        (By.ID, eleData.readExcel(78, 3))] # 结束时间

    # 错误提示框
    msgInfo = (By.XPATH, eleData.readExcel(79, 3))

    # 添加规则页面
    createRule = (By.XPATH, eleData.readExcel(80, 3))


    # 查找主菜单
    def addRuleMenu(self):
        """

        :return:
        """

        self.findElement(*self.menuList[7]).click()
        time.sleep(1)
        self.findElement(*self.itemMenu).click()
        time.sleep(2)
        log.logger.info('page [%s] :found the menu [%s] and [%s]' %(sys._getframe().f_code.co_name, self.menuList[7],self.itemMenu ))

    # 点击按钮
    def cBtn(self, button):
        """

        :param button:
        :return:
        """
        btn = self.findElement(*button)
        try:
            btn.click()
        except Exception:
            log.logger.exception(
                'can not click the button' ,exc_info=True)
        else:
            log.logger.info(
                'page [%s] :clicking the button [%s]' % (sys._getframe().f_code.co_name, button))

    # 下拉选项
    def selectItem(self, typeItem):
        """

        :param typeItem:
        :return:
        """
        item = self.findElement(*typeItem)
        time.sleep(1)
        try:
            action = ActionChains(self.driver)
            action.move_to_element(item).perform()
            time.sleep(1)
            item.click()
            action.reset_actions()
        except Exception:
            log.logger.exception('the element not found, move_to requires a WebElement', exc_info=True)
            raise
        else:
            log.logger.info('selected item success!')

    # 输入一组数据
    def inputGroupValue(self, element_list, value_list):
        """

        :param element_list: 一组元素列表
        :param value_list: 一组数据列表
        :return: none
        """
        for eleLen in range(len(element_list)):
            try:
                self.inputValue(element_list[eleLen], value_list[eleLen])
            except Exception:
                log.logger.exception('element [%s] type value [%s] wrong !' %(element_list[eleLen], value_list[eleLen]))
                raise
            else:
                log.logger.info('element [%s] is typing value [%s]' %(element_list[eleLen], value_list[eleLen]))


if __name__=='__main__':
    pass