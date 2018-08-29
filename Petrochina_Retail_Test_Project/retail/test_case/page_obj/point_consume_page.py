# ----------------------------------
'''                                                           
代码说明：
编写日期：
设计  者：
'''
# ----------------------------------
from retail.test_case.page_obj.base_page import Base_Page
import time
from retail.test_case.models.is_element_exist import Isnot_element_exist
from selenium.webdriver.common.action_chains import ActionChains

class Point_Consume(Base_Page):
    check_page_element = ['积分结果查询', '查询条件', '积分累计明细']

    # 查找菜单
    def function_menu(self):
        self.driver.find_element_by_link_text('积分消费查询').click()
        self.driver.find_element_by_link_text('积分查询').click()
        time.sleep(4)
    # 输入查询条件
    def input_query_text(self, id, values):
        ele = self.find_ele_by_id(id)
        ele.clear()
        ele.send_keys(values)
    # 交易来源选择
    def find_consume_source(self,xpath):
        self.find_ele_by_id('_pagef_0000000080addSource').click()
        time.sleep(2)
        element = self.find_ele_by_xpath(xpath)
        ActionChains(self.driver).move_to_element(element).perform()
        element.click()
    # 关闭弹窗
    def close_error_massage(self,id):
        close1 = self.driver.find_element_by_id(id)
        close1.click()

    # 点击查询和重置按钮
    def click_query_reset_button(self,button):
        self.driver.find_element_by_link_text(button).click()
    # 重写重置功能
    def reset(self):
        pass

if __name__ == '__main__':
    pass
