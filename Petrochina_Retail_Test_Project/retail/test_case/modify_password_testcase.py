#----------------------------------
'''                                                           
代码说明： 主菜单列表及修改密码测试用例
编写日期：2018.08.14
设计  者：linux超
'''
#----------------------------------
from .models.myunit import Myunittest
from .page_obj.primary_page import Primary_Menu
import time
from selenium.webdriver.common.by import By

class Primary_Menu_Test_Cases(Myunittest):

    # ............................................................................................#
    #   遍历所有菜单
    def test_menu_is_display(self):
        self.login.login_function()
        menu = Primary_Menu(self.driver)
        time.sleep(4)
        num = 0
        for menu_item in menu.menu_list: # 循环遍历并断言菜单是否正确
            #self.assertEqual(menu.menu_list[num][1], (menu.find_element_re(*menu_item).text), '菜单不存在')
            self.assertEqual(menu.menu_list[num][1],(menu.find_menu_element(*menu_item).text),'菜单不存在')
            num=num+1

    # ............................................................................................#
    #   测试修改密码 长度校验
    def test_modify_password_len(self):
        self.login.login_function()
        menu = Primary_Menu(self.driver)
        menu.function_menu() # 查找修改密码页面
        menu.modify_password_new(menu.password_list[0]) # 修改密码
        text = menu.error_messages_frame()
        self.assertIn('密码长度至少 4 位！', text, '提示信息错误') # 密码长度不满足时断言提示信息

    # ............................................................................................#
    #   测试修改密码 强度校验
    def test_modify_password_strebgth(self):
        self.login.login_function()
        menu = Primary_Menu(self.driver)
        menu.function_menu() # 查找修改密码页面
        menu.modify_password_new(menu.password_list[1]) # 修改密码
        text = menu.error_messages_frame()
        self.assertIn('密码强度不够，请重新输入密码！', text, ' 密码强度不够，请重新输入密码！') # 密码强度不满足时断言提示信息

    # ............................................................................................#
    #   测试修改密码 新密码和旧密码不同
    def test_modify_password_difference(self):
        self.login.login_function()
        menu = Primary_Menu(self.driver)
        menu.function_menu() # 查找修改密码页面
        menu.modify_password_new(menu.password_list[2]) # 修改密码
        text = menu.error_messages_frame()
        self.assertIn('两次输入的新密码不同！', text, ' 两次输入的新密码不同！') # 新密码和确认码不同时断言提示信息

    # ............................................................................................#
    #   测试修改密码 所有密码都为空
    def test_modify_password_all_blank(self):
        self.login.login_function()
        menu = Primary_Menu(self.driver)
        menu.function_menu() # 查找修改密码页面
        menu.modify_password_new(menu.password_list[3]) # 修改密码
        text = menu.error_messages_frame()
        self.assertIn('该输入项的值不能为空！', text, ' 该输入项的值不能为空！') # 所有密码均为空时断言提示信息

    # ............................................................................................#
    #   修改密码用例整合再一个循环里面
    def test_modify_password(self):
        self.login.login_function()
        menu = Primary_Menu(self.driver)
        menu.function_menu() # 查找修改密码页面
        i = 1 # 动态提示框
        error_list = []
        for list in range(len(menu.password_list)):
            menu.modify_password_new(menu.password_list[list])
            by_id =(By.ID, 'unieap_form_Button_'+str(i)+'_unieap_input') # 每弹出一次提示框 提示框的 id都会改变
            text = menu.error_messages_frame(by_id) # 这里只判断是否有提示框弹出，如有说明修改失败，没有或者其他提示框默认为修改成功
            i=i+1
            error_list.append(text)
        self.assertEqual('密码长度至少 4 位！',error_list[0],'')
        self.assertEqual(' 密码强度不够，请重新输入密码！', error_list[0], '')
        self.assertEqual(' 旧密码输入错误！', error_list[0], '')
        self.assertEqual(' 该输入项的值不能为空！', error_list[0], '')
    # ............................................................................................#
if __name__=='__main__':
    pass