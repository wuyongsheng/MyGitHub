# ----------------------------------
'''                                                           
代码说明：会员档案查询页面
编写日期：2018.08.15
设计  者：linux超
'''
# ----------------------------------
from retail.test_case.page_obj.primary_page import Primary_Menu
import time

class Member_Record_Query_Page(Primary_Menu):

    # 会员查询页面的3个列表
    Ui_element_list = ['/html/body/section/section/section/section[2]/section/section/div/div[1]/div[1]/span[1]',
                       r'/html/body/section/section/section/section[2]/section/section/div/div[3]/div[1]/span[1]',
                       r'/html/body/section/section/section/section[2]/section/section/div/div[3]/div[1]/span[1]']

    query_failed_error_list = '/html/body/div[5]/div[1]'  # 查询失败弹出的错误提示框

    values_list = ['#', '123', '汉字']
    member_list = ['MemberNo', 'MemberName', 'PhoneNumber']  # 3个查询条件框元素
    member_type = ['个人会员','企业会员','其它']
    member_level = ['标准会员','黄金会员','铂金会员','钻石会员']

    # 重写父类 方法 查找菜单
    def function_menu(self):
        self.find_menu_element(self.menu_list[1]).click()
        self.find_menu_element('会员档案查询').click()
        time.sleep(4)

    # 会员类型/会员级别选择
    def find_member_type_level(self, xpath):
        member_type_level = self.driver.find_element_by_xpath(xpath)
        text = member_type_level.text
        return text, member_type_level

    # 点击查询和重置按钮
    def click_query_reset_button(self, id='_pagef_0000000043unieap_form_Button_0_unieap_input'):
        self.driver.find_element_by_id(id).click()

    # 输入查询条件
    def input_member_query_terms(self, id, values_list):
        member_number_name_phone = self.find_ele_by_id(id)
        member_number_name_phone.clear()
        member_number_name_phone.send_keys(values_list)

    # 获取条件输入框的内容
    def get_inputbox_text(self,id):
        get_member_number_name_phone_text = self.find_ele_by_xpath(id)
        text=get_member_number_name_phone_text.get_attribute('value')
        return text

    # 重置功能的重载
    def reset(self):
        self.driver.find_element_by_id('_pagef_0000000043formMemberNo_unieap_input').clear()
        self.driver.find_element_by_id('_pagef_0000000043formMemberName_unieap_input').clear()
        self.driver.find_element_by_id('_pagef_0000000043formPhoneNumber_unieap_input').clear()

    # 查询功能
    def query_function(self, id, values_list, button='_pagef_0000000043unieap_form_Button_0_unieap_input'):
        self.input_member_query_terms(id, values_list)
        self.click_query_reset_button(button)


if __name__ == '__main__':
    pass
