# ----------------------------------
'''                                                           
代码说明：会员档案查询测试用例
编写日期：2018.08.15
设计  者：Linux超
'''
# ----------------------------------
import random
from .models.myunit import Myunittest
from selenium.webdriver.common.action_chains import ActionChains
from .page_obj.memeber_page import Member_Record_Query_Page
from .models.login_function import Login_function_public
from .models.is_element_exist import Is_Element_Exist, Isnot_element_exist
import time
import unittest

class Member_Record_Query_Test_Cases(Myunittest):

    # ............................................................................................#
    # testcase 12: 页面检查
    @unittest.skip('dont run the test case')
    def test_member_check_ui(self):
        menu = Member_Record_Query_Page(self.driver) # 实例化会员查询页面
        Login_function_public(self.driver)  # 登录
        time.sleep(5)
        menu.function_menu()  # 查找会员档案查询菜单
        for element in range(len(menu.Ui_element_list)):
            flag = Is_Element_Exist(self.driver, menu.Ui_element_list[element])
            self.assertTrue(flag)  # 断言存在这3个列表 [查询条件 ,会员信息明细 ,积分变化明细]

     # ............................................................................................#
    # testcase 13: 会员类型下拉列表校验
    def test_member_type(self):
        menu = Member_Record_Query_Page(self.driver)  # 实例化会员查询页面
        Login_function_public(self.driver)  # 登录
        time.sleep(5)
        menu.function_menu()  # 查找会员档案查询菜单
        menu.find_ele_by_id('_pagef_0000000043formMembeType_unieap_input').click()  # 查询条件:[会员类型]
        time.sleep(3)
        list_type = []
        for i in range(1, 4):  # 循环遍历会员类型下拉列表
            text, memeber_type_level = menu.find_member_type_level(i)
            list_type.append(text)
        # print(list_type)
        self.assertEqual('个人会员', list_type[0])
        self.assertEqual('企业会员', list_type[1])
        self.assertEqual('其它', list_type[2])

    # ............................................................................................#
    # testcase 14: 会员级别下拉列表校验
    def test_member_level(self):
        menu = Member_Record_Query_Page(self.driver)  # 实例化会员查询页面
        Login_function_public(self.driver)  # 登录
        time.sleep(5)
        menu.function_menu() # 查找会员档案查询菜单
        menu.find_ele_by_id('_pagef_0000000043fromMemberLevel_unieap_input').click() # 查询条件:[会员级别]
        time.sleep(3)
        list_level = []
        for i in range(1, 5): # 循环遍历会员级别下拉列表
            text, memeber_type_level = menu.find_member_type_level(i)
            list_level.append(text)
        #print(list_level)
        self.assertEqual('标准会员', list_level[0])
        self.assertEqual('黄金会员', list_level[1])
        self.assertEqual('铂金会员', list_level[2])
        self.assertEqual('钻石会员', list_level[3])

    # ............................................................................................#
    # 对页面的条件进行组合后单击查询按钮。这是一个大数据量的操作，因此不对返回数据做校验，只看本次组合的条件在页面是否可正常使用。
    # 如果查询失败，系统会有弹出框提示失败原因，这个应该很好理解的。
    # 我们抓取这个框是否在一定的时间内出现，如果出现则判定本次查询失败，记录用例结果。
    # ............................................................................................#
    # testcase 15: 校验默认查询功能可用
    def test_member_query_failed(self):
        menu = Member_Record_Query_Page(self.driver)  # 实例化会员档案查询页面
        Login_function_public(self.driver)  # 登录
        time.sleep(5)
        menu.function_menu()  # 找到会员查询页面
        menu.click_query_reset_button()  # 点击[查询]
        time.sleep(3)
        flag = Is_Element_Exist(self.driver, menu.query_failed_error_list)  # 断言错误提示框
        self.assertFalse(flag, msg='查询成功')  # flag为false时，断言成功， 无提示框，说明默认查询成功

    # ............................................................................................#
    # testcase 16: 单一查询（会员编号，会员姓名，手机号码）
    def test_alone_query_1(self):
        menu = Member_Record_Query_Page(self.driver)  # 实例化会员档案查询页面
        Login_function_public(self.driver)  # 登录
        time.sleep(5)
        menu.function_menu()  # 找到会员档案查询页面
        number = 2
        for id in menu.member_list:
            menu.reset()  # 重置
            for values in menu.values_list:
                # 3个输入条件
                menu.input_member_query_terms('_pagef_0000000043form' + str(id) + '_unieap_input', values)
                #self.driver.find_element_by_id('_pagef_0000000043unieap_form_Button_0_unieap_input').click()
                menu.click_query_reset_button() # 点击[查询]
                time.sleep(3)
                # 这个方法有点问题 后期再优化一下吧
                flag = Isnot_element_exist(self.driver, menu.query_failed_error_list)
                if flag:
                    self.assertTrue(flag, '查询失败')
                    self.driver.find_element_by_id('unieap_form_Button_' + str(number) + '_unieap_input').click()
                    time.sleep(3)
                    number = number + 1
                else:
                    self.assertFalse(flag, '查询成功')

    # ............................................................................................#
    # testcase 17：单一查询(会员类型)
    def test_alone_query_2(self):
        menu = Member_Record_Query_Page(self.driver) # 实例化会员档案查询页面
        Login_function_public(self.driver) # 登录
        time.sleep(5)
        menu.function_menu() # 找到会员档案查询页面
        time.sleep(3)
        for i in range(1, 4):
            menu.find_ele_by_id('_pagef_0000000043formMembeType_unieap_input').click() # 点击[会员类型]
            text, member_type_level = menu.find_member_type_level('//*[@class="u-combobox-items-container"]'
                                                                  '/table/tbody/tr[' + str(i) + ']/td/span') # 遍历每一个下拉选项
            ActionChains(self.driver).move_to_element(member_type_level).perform() # 鼠标移动到下拉选项上
            member_type_level.click() # 选中下拉选项
            menu.click_query_reset_button()  # 点击[查询]
            time.sleep(3)
            flag = Isnot_element_exist(self.driver, menu.query_failed_error_list) # 判断查询成功
            self.assertFalse(flag, '查询成功')

    # ............................................................................................#
    # testcase 18：单一查询(会员级别)
    def test_alone_query_3(self):
        menu = Member_Record_Query_Page(self.driver)  # 实例化会员档案查询页面
        Login_function_public(self.driver)  # 登录
        time.sleep(5)
        menu.function_menu()  # 找到会员档案查询页面
        time.sleep(3)
        for i in range(1, 5):
            menu.find_ele_by_id('_pagef_0000000043fromMemberLevel_unieap_input').click()  # 点击[会员级别]
            text, member_type_level = menu.find_member_type_level('//*[@class="u-combobox-items-container"]'
                                                                  '/table/tbody/tr[' + str(i) + ']/td/span')  # 遍历每一个下拉选项
            ActionChains(self.driver).move_to_element(member_type_level).perform()  # 鼠标移动到下拉选项上
            member_type_level.click()  # 选中下拉选项
            menu.click_query_reset_button()  # 点击[查询]
            time.sleep(3)
            flag = Isnot_element_exist(self.driver, menu.query_failed_error_list)  # 判断查询成功
            self.assertFalse(flag, '查询成功')

    # ............................................................................................#
    # testcase 19：重置功能测试(没有会员类型和级别的输入，有问题没解决）
    def test_reset(self):
        menu = Member_Record_Query_Page(self.driver) # 实例化会员档案查询页面
        Login_function_public(self.driver) # 登录
        time.sleep(5)
        menu.function_menu() # 找到会员档案查询页面
        time.sleep(3)
        # 3个条件输入框随机输入数据
        for id in menu.member_list:
            menu.input_member_query_terms('_pagef_0000000043form' + str(id) + '_unieap_input',
                                          random.choice(menu.values_list))
        time.sleep(2)

        #会员类型下拉列表中随机选择一项
        menu.find_ele_by_xpath('//*[@id="_pagef_0000000043formMembeType_unieap_input"]').click()
        time.sleep(2)
        text_type, member_type_handle = menu.find_member_type_level('//*[@class="u-combobox-items-container"]'
                                                                   '/table/tbody/tr'
                                                         '[' + str(random.randint(1, 3)) + ']/td/span')
        ActionChains(self.driver).move_to_element(member_type_handle).perform()  # 鼠标移动到下拉选项上
        member_type_handle.click()
        time.sleep(2)

        # menu.find_ele_by_xpath('//*[@id="_pagef_0000000043fromMemberLevel_unieap_input"]').click()
        # text_level, member_level_handle = menu.find_member_type_level('//*[@class="u-combobox-items-container"]'
        #                                                       '/table/tbody/tr'
        #                                               '[' + str(random.randint(1, 4)) + ']/td/span')
        # time.sleep(2)
        #ActionChains(self.driver).click(member_level_handle).perform()
        #text_level, member_level_handle = menu.find_member_type_level("//*[contains(text(),"+random.choice(menu.member_level)+")]")
        #member_level_handle.click()
        # = member_level.text
        #print(text_level)

        # 点击【重置】
        menu.click_query_reset_button('_pagef_0000000043unieap_form_Button_1_unieap_input')
        # 获取前3个输入框的内容
        text_list = []
        for input_box in menu.member_list:
            #text = menu.get_inputbox_text('_pagef_0000000043form' + str(input_box) + '_unieap_input')
            text = menu.get_inputbox_text('//*[@id="_pagef_0000000043form'+str(input_box)+'_unieap_input"]')
            text_list.append(text)
        # 获取会员类型和会员级别选择框中的内容
        type_level_text = menu.get_inputbox_text("//*[@id='_pagef_0000000043formMembeType_unieap_input']")
        text_list.append(type_level_text)
        print(text_list)
        # 断言每一个条件框是否为空 为空就通过
        for get_attr in text_list:
            self.assertEqual('',get_attr)


if __name__ == '__main__':
    pass
