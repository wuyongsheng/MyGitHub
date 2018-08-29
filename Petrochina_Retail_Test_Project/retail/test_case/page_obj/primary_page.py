# ----------------------------------
'''                                                           
代码说明：主菜单页(修改密码的功能放在一起了）
编写日期：2018.08.14
设计  者：linux超
'''
# ----------------------------------
from retail.test_case.page_obj.base_page import Base_Page
import time


class Primary_Menu(Base_Page):

    menu_list = ['权限管理', '会员档案', '积分消费查询', '功能演示', '待办工作', '报表', '积分规则/活动查询', '积分规则/活动申请']
    password_list = [['a', 'a', 'a'], ['a', 'qwert', 'qwert'], ['a', 'qwert1234!@#$', 'qwert1234!@#'], ['', '', '']]

    #   主菜单
    def find_menu_element(self, linktext):
        return self.find_ele_by_link_text(linktext)

    #   旧密码输入框
    def input_old_password(self, old_password=''):
        self.find_ele_by_id('_pagesa00000041old_pwd_unieap_input').send_keys('')
        self.find_ele_by_id('_pagesa00000041old_pwd_unieap_input').send_keys(old_password)

    #   新密码输入框
    def input_new_password(self, new_password=''):
        self.find_ele_by_id('_pagesa00000041new_pwd1_unieap_input').send_keys('')
        self.find_ele_by_id('_pagesa00000041new_pwd1_unieap_input').send_keys(new_password)

    #   确认密码输入框
    def input_confirm_password(self, confirm_password):
        self.find_ele_by_id('_pagesa00000041new_pwd2_unieap_input').send_keys('')
        self.find_ele_by_id('_pagesa00000041new_pwd2_unieap_input').send_keys(confirm_password)

    #   保存
    def click_button(self, element='//*[@id="_pagesa00000041unieap_form_Button_0_unieap_input"]'):
        self.find_ele_by_xpath(element).click()

    #   修改密码功能菜单
    def function_menu(self):
        self.find_menu_element(self.menu_list[0]).click()
        self.find_menu_element('个人设置').click()
        self.find_menu_element('密码修改').click()
        # time.sleep(4)
        self.driver.implicitly_wait(4)

    #   修改密码
    def modify_password_new(self, list, element='//*[@id="_pagesa00000041unieap_form_Button_0_unieap_input"]'):
        self.input_old_password(list[0])
        self.input_new_password(list[1])
        self.input_confirm_password(list[2])
        self.click_button(element)

    #   错误提示框
    def error_messages_frame(self,
                             xpath='/html/body/div[5]/div[2]/div[3]/div[1]/div/table/tbody/tr/td/table/tbody/tr/td[2]',
                             id='unieap_form_Button_1_unieap_input'):
        messages_frame = self.find_ele_by_xpath(xpath)
        text = messages_frame.text
        time.sleep(3)
        self.find_ele_by_id(id).click()
        return text


if __name__ == '__main__':
    pass
