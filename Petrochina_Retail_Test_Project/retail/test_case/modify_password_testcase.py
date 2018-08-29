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
from .models.login_function import Login_function_public

class Primary_Menu_Test_Cases(Myunittest):
    # #   实例化登录页面和主菜单
    # def init_menupage_loginpage(self):
    #     menu = Primary_Menu(self.driver)
    #     login = Login_Page(self.driver)
    #     return menu,login

    # ............................................................................................#
    #   遍历所有菜单
    def test_menu_is_display(self):
        # menu,login = self.init_menupage_loginpage()
        # login.login_function() # 登录
        Login_function_public(self.driver)
        menu = Primary_Menu(self.driver)
        time.sleep(4)
        for menu_item in menu.menu_list: # 循环遍历并断言菜单是否存在
            try:
                menu.find_menu_element(menu_item).isdisplayed()
            except AttributeError as e:
                print(e)

    # ............................................................................................#
    #   测试修改密码 长度校验
    def test_modify_password_len(self):
        Login_function_public(self.driver)
        menu = Primary_Menu(self.driver)
        time.sleep(4)
        menu.function_menu() # 查找修改密码页面
        menu.modify_password_new(menu.password_list[0]) # 修改密码
        try:
            text = menu.error_messages_frame()
            self.assertEqual(' 密码长度至少 4 位！',text,' 密码长度至少 4 位！') # 密码长度不满足时断言提示信息
        except:
            pass

    # ............................................................................................#
    #   测试修改密码 强度校验
    def test_modify_password_strebgth(self):
        Login_function_public(self.driver)
        menu = Primary_Menu(self.driver)
        time.sleep(4)
        menu.function_menu() # 查找修改密码页面
        menu.modify_password_new(menu.password_list[1]) # 修改密码
        try:
            text = menu.error_messages_frame()
            self.assertEqual(' 密码强度不够，请重新输入密码！', text, ' 密码强度不够，请重新输入密码！') # 密码强度不满足时断言提示信息
        except:
            pass

    # ............................................................................................#
    #   测试修改密码 新密码和旧密码不同
    def test_modify_password_difference(self):
        Login_function_public(self.driver)
        menu = Primary_Menu(self.driver)
        time.sleep(4)
        menu.function_menu() # 查找修改密码页面
        menu.modify_password_new(menu.password_list[2]) # 修改密码
        try:
            text = menu.error_messages_frame()
            self.assertEqual(' 两次输入的新密码不同！', text, ' 两次输入的新密码不同！') # 新密码和确认码不同时断言提示信息
        except:
            pass

    # ............................................................................................#
    #   测试修改密码 所有密码都为空
    def test_modify_password_all_blank(self):
        Login_function_public(self.driver)
        menu = Primary_Menu(self.driver)
        time.sleep(4)
        menu.function_menu() # 查找修改密码页面
        menu.modify_password_new(menu.password_list[3]) # 修改密码
        try:
            text = menu.error_messages_frame()
            print(text,':密码修改失败')
            self.assertEqual(' 该输入项的值不能为空！', text, ' 该输入项的值不能为空！') # 所有密码均为空时断言提示信息
        except:
            pass

    # ............................................................................................#
    #   修改密码用例整合再一个循环里面
    def test_modify_password(self):
        Login_function_public(self.driver)
        menu = Primary_Menu(self.driver)
        time.sleep(4)
        menu.function_menu() # 查找修改密码页面
        i = 1 # 动态提示框
        for list in range(len(menu.password_list)):
            menu.modify_password_new(menu.password_list[list])
            id = 'unieap_form_Button_'+str(i)+'_unieap_input' # 每弹出一次提示框 提示框的 id都会改变
            try:
                text = menu.error_messages_frame(id) # 这里只判断是否有提示框弹出，如有说明修改失败，没有或者其他提示框默认为修改成功
                i = i +1
                print(text, ':密码修改失败') # 打印 提示信息
            except:
                pass

    # ............................................................................................#
if __name__=='__main__':
    pass