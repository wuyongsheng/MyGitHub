# ----------------------------------
'''                                                           
代码说明：主菜单页(修改密码的功能放在一起了）
编写日期：2018.08.14
设计  者：linux超
'''
# ----------------------------------
from retail.test_case.page_obj.base_page import Base_Page
import time
from selenium.webdriver.common.by import By

class Primary_Menu(Base_Page):

    """密码数据"""
    password_list = \
        [['a', 'a', 'a'],
        ['a', 'qwert', 'qwert'],
        ['a', 'qwert1234!@#$', 'qwert1234!@#'],
        ['', '', '']]

    """主菜单"""
    menu_list = \
        [(By.LINK_TEXT,'权限管理'),
        (By.LINK_TEXT,'会员档案'),
        (By.LINK_TEXT,'积分消费查询'),
        (By.LINK_TEXT,'功能演示'),
        (By.LINK_TEXT,'待办工作'),
        (By.LINK_TEXT,'报表'),
        (By.LINK_TEXT,'积分规则/活动查询'),
        (By.LINK_TEXT,'积分规则/活动申请')]

    """权限管理下拉菜单"""
    menu_personal = \
        (By.LINK_TEXT,'个人设置')
    menu_modifypassword = \
        (By.LINK_TEXT,'密码修改')

    """密码修改"""
    old_password = \
        (By.ID, '_pagesa00000041old_pwd_unieap_input')
    new_password = \
        (By.ID, '_pagesa00000041new_pwd1_unieap_input')
    commit_password = \
        (By.ID, '_pagesa00000041new_pwd2_unieap_input')

    """错误提示框及确定"""
    error_message = \
        (By.XPATH,'/html/body/div[5]/div[2]/div[3]/div[1]/div/table/tbody/tr/td/table/tbody/tr/td[2]')
    commit_btn = \
        (By.ID,'unieap_form_Button_1_unieap_input')
    close_btn = \
        (By.XPATH,"//*[@class='u-xdlg-mtc']/div[2]/span")

    """密码说明"""
    readme = \
        (By.ID,'_pagesa00000041unieap_form_Text_4')

    """保存"""
    save_btn = \
        (By.XPATH,"//*[@id='_pagesa00000041unieap_form_Button_0_unieap_input']")

    #   主菜单
    def find_menu_element(self,*menu_list):
        return self.find_element_re(*menu_list)

    #   旧密码输入框
    def input_old_password(self, old_password=''):
        self.find_element_re(*self.old_password).send_keys('')
        self.find_element_re(*self.old_password).send_keys(old_password)

    #   新密码输入框
    def input_new_password(self, new_password=''):
        self.find_element_re(*self.new_password).send_keys('')
        self.find_element_re(*self.new_password).send_keys(new_password)

    #   确认密码输入框
    def input_confirm_password(self, confirm_password=''):
        self.find_element_re(*self.commit_password).send_keys('')
        self.find_element_re(*self.commit_password).send_keys(confirm_password)

    #   保存
    def click_button(self):
        self.driver.implicitly_wait(5)
        clickbutton = self.find_element_re(*self.save_btn)
        clickbutton.click()

    #   修改密码功能菜单
    def function_menu(self):
        self.find_element_re(*self.menu_list[0]).click()
        self.find_element_re(*self.menu_personal).click()
        self.find_element_re(*self.menu_modifypassword).click()
        self.driver.implicitly_wait(2)

    #   修改密码
    def modify_password_new(self, list):
        self.input_old_password(list[0])
        self.input_new_password(list[1])
        self.input_confirm_password(list[2])
        self.click_button()

    #   错误提示框
    def error_messages_frame(self, commit_btn = (By.ID,'unieap_form_Button_1_unieap_input')):
        """

        :type commit_btn: 元祖
        """
        messages_frame = self.find_element_re(*self.error_message)
        text = messages_frame.text
        element = self.find_element_re(*commit_btn)
        time.sleep(2)
        element.click()
        return text

if __name__ == '__main__':
    pass
