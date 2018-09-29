'''
Code description：积分查询 page
Create time：
Developer：
'''

import logging
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import random
from retail.test_case.page_obj.base_page import BasePage, eleData, queryData
from retail.test_case.models.log import Logger

log = Logger(__name__, CmdLevel=logging.INFO, FileLevel=logging.INFO)
class PointConsume(BasePage):

    # check_page_element = ['积分结果查询', '查询条件', '积分累计明细']

    # 测试数据
    valuesList = \
        [int(queryData.readExcel(5, 1)),
         int(queryData.readExcel(6, 1)),
         int(queryData.readExcel(7, 1)),
         int(queryData.readExcel(8, 1)),
         queryData.readExcel(9, 1)] # 校验条件输入项
    checkList = \
        [[queryData.readExcel(11, 1), int(queryData.readExcel(12, 1)), queryData.readExcel(13, 1)],
         [int(queryData.readExcel(11, 2)), queryData.readExcel(12, 2), queryData.readExcel(13, 2)],
         [int(queryData.readExcel(11, 3)), queryData.readExcel(12, 3), queryData.readExcel(13, 3)]] # 月份， 省密码， 会员编号 输入校验
    # 主菜单下拉选项
    scoreQuery = (By.LINK_TEXT, eleData.readExcel(42, 3))
    consumeRecord = (By.LINK_TEXT, eleData.readExcel(43, 3))

    # 页面检查元素
    uiElements = (By.XPATH, eleData.readExcel(44, 3))

    # 交易开始时间, 交易结束时间, 月份, 省编码, 会员编号
    inputIterm = \
        [(By.ID, eleData.readExcel(45, 3)),
         (By.ID, eleData.readExcel(46, 3)),
         (By.ID, eleData.readExcel(47, 3)),
         (By.ID, eleData.readExcel(48, 3)),
         (By.ID, eleData.readExcel(49, 3))]
    # 交易来源及下拉选项
    consumeSource = (By.ID, eleData.readExcel(50, 3))
    consumeSourceIterm = \
        (By.XPATH, "//*[@class='u-combobox-items-container']/table/tbody/tr["+str(random.randint(1,6))+"]/td/span")

    # 缺省必填项错误提示框
    errFram = (By.XPATH, eleData.readExcel(52, 3))
    errBtn = (By.XPATH, eleData.readExcel(53, 3))
    # 查询与重置
    queryReset = \
        [(By.LINK_TEXT, eleData.readExcel(54, 3)),
         (By.LINK_TEXT, eleData.readExcel(55, 3))]

    # 输入条件不满足需求 提示
    errMsg = (By.XPATH, eleData.readExcel(56, 3))
    closeBtn = (By.CSS_SELECTOR, eleData.readExcel(57, 3))

    # 积分查询菜单
    def integrateMenu(self):
        """

        :return:
        """
        try:
            self.findElement(*self.menuList[2]).click()
            self.findElement(*self.scoreQuery).click()
            time.sleep(2)
        except Exception:
            log.logger.exception('find menu [积分查询] fail', exc_info=True)
            raise
        else:
            log.logger.info('finding menu [积分查询 ]')

    # 输入查询条件
    def inputQueryValue(self, input_box, value):
        """

        :param input_box:
        :param value:
        :return:
        """
        try:
            ele = self.findElement(*input_box)
            ele.clear()
            ele.send_keys(value)
            time.sleep(2)
        except Exception:
            log.logger.exception('input value fail', exc_info=True)
            raise
        else:
            log.logger.info('[%s] input value [%s] success' %(input_box, value))

    # 交易来源选择
    def cConsumeSource(self):
        """

        :return:
        """
        try:
            self.findElement(*self.consumeSource).click()
            time.sleep(2)
            element = self.findElement(*self.consumeSourceIterm)
            ActionChains(self.driver).move_to_element(element).perform()
            element.click()
        except Exception:
            log.logger.exception('error：交易查询未选中！',exc_info=True)
            raise
        else:
            log.logger.info('success: 交易查询选择项被选择')

    # 点击查询和重置按钮
    def cQueryResetBtn(self,query_reset):
        """

        :param query_reset:
        :return:
        """
        try:
            self.findElement(*query_reset).click()
        except Exception:
            log.logger.exception('query/reset button clcik fail', exc_info=True)
            raise
        else:
            log.logger.info('clicking button success!')


    # 切换列表(积分累计记录查询-交易记录查询)
    def changePage(self):
        try:
            element = self.findElement(*self.consumeRecord)
            ActionChains(self.driver).move_to_element(element).perform()
            element.click()
        except Exception:
            log.logger.exception('切换列表失败', exc_info=True)
            raise
        else:
            log.logger.info('切换列表成功!')

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
