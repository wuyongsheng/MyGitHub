# ----------------------------------
'''                                                           
代码说明：
编写日期：
设计  者：
'''
# ----------------------------------
from retail.test_case.models.is_element_exist import Isnot_element_exist
from retail.test_case.models.myunit import Myunittest
from .page_obj.point_consume_page import Point_Consume
from retail.test_case.models.login_function import Login_function_public
import random
import time

class Point_Query_Test_Cases(Myunittest):
    # testcase 20:页面检查
    def test_point_query_page_check(self):
        # 初始化积分消费查询页面
        menu = Point_Consume(self.driver)
        Login_function_public(self.driver)  # 登录
        menu.function_menu()  # 查找积分查询菜单
        elements = self.driver.find_elements_by_xpath("//*[@class='u-titlepane-titlenode']")
        ele_list = []
        for eles in elements:
            print(eles.text)
            ele_list.append(eles.text)
        self.assertEqual('积分结果查询', ele_list[0])
        self.assertEqual('查询条件', ele_list[1])
        self.assertEqual('积分累计明细', ele_list[2])
    # testcase 21:必填项校验
    def test_point_required_field(self):
        menu = Point_Consume(self.driver)
        Login_function_public(self.driver) # 登录
        time.sleep(3)
        menu.function_menu()
        menu.input_query_text('_pagef_0000000080startPayTime_unieap_input','2018-08-22 13:47:05')
        menu.input_query_text('_pagef_0000000080endPayTime_unieap_input','2018-08-24 13:47:05')
        menu.find_consume_source("//*[@class='u-combobox-items-container']/table/tbody/tr["+str(random.randint(1,6))+"]/td/span")
        menu.input_query_text('_pagef_0000000080memberNo_unieap_input','1')

        menu.click_query_reset_button('查询')

        flag1 = Isnot_element_exist(self.driver, '//*[@class="u-xdlg"]')
        if flag1:
            self.assertTrue(flag1,'存在必填项未输入')
            menu.close_error_massage('unieap_form_Button_4_unieap_input')
            print('存在提示框')
            menu.input_query_text('_pagef_0000000080pointsMonth_unieap_input','1')
            menu.click_query_reset_button('查询')
            flag2 = Isnot_element_exist(self.driver, '//*[@class="u-xdlg"]')
            if flag2:
                menu.close_error_massage('unieap_form_Button_5_unieap_input')
                self.assertTrue(flag2, '存在必填项未输入')
                menu.input_query_text('_pagef_0000000080provinceCode_unieap_input', 'M000')
                menu.click_query_reset_button('查询')
                flag3 =Isnot_element_exist(self.driver,'//*[@class="u-xdlg"]')
                if flag3:
                    menu.close_error_massage('unieap_form_Button_6_unieap_input')
                    self.assertTrue(flag3, '存在必填项未输入')
                else:
                    self.assertFalse(flag3, '无必填项需要输入')
            else:
                self.assertFalse(flag2, '无必填项需要输入')
        else:
            self.assertFalse(flag1,'无必填项需要输入')
            print('不存在提示框')

    # textcase 22：单位选择页面


if __name__ == '__main__':
    pass
