'''
Code description：权限管理/个人设置/密码修改 testcase
Create time：
Developer：
'''

import time
from retail.test_case.models.myunit import MyunitTest
from retail.test_case.page_obj.modifypw_page import PrimaryMenu
from retail.test_case.models.strhandle import strhandle

class ModifyPw_TC(MyunitTest):

    """权限管理/个人设置/密码修改模块测试用例"""

    def test_menu_is_display(self):
        """主菜单校验"""
        self.login.loginFunc()
        menu = PrimaryMenu(self.driver)
        time.sleep(4)
        num = 0
        for menu_item in menu.menuList: # 循环遍历并断言菜单是否正确
            self.assertEqual(menu.menuList[num][1],(menu.findMenu(*menu_item).text),'菜单不存在')
            num=num+1

    def test_modify_password_len(self):
        """旧密码非空,新密码长度小于4位,确认密码非空,修改密码失败,弹窗提示"""
        self.login.loginFunc()
        menu = PrimaryMenu(self.driver)
        menu.modifyPwMenu() # 查找修改密码页面
        menu.modifyPw(menu.pwdList[0]) # 修改密码
        text = menu.errorDialog(menu.closeBtn)
        self.assertIn('密码长度至少 4 位！', text, '提示信息错误') # 密码长度不满足时断言提示信息

    def test_modify_password_strebgth(self):
        """旧密码非空,新密码长度大于4且强度不够,确认密码非空,修改密码失败,弹窗提示"""
        self.login.loginFunc()
        menu = PrimaryMenu(self.driver)
        menu.modifyPwMenu() # 查找修改密码页面
        menu.modifyPw(menu.pwdList[1]) # 修改密码
        text = menu.errorDialog(menu.closeBtn)
        self.assertIn('密码强度不够，请重新输入密码！', text, ' 密码强度不够，请重新输入密码！') # 密码强度不满足时断言提示信息

    def test_modify_password_incorrect(self):
        """旧密码不正确非空,新密码等于确认密码且满足条件,修改密码失败,弹窗提示"""
        self.login.loginFunc()
        menu = PrimaryMenu(self.driver)
        menu.modifyPwMenu() # 查找修改密码页面
        menu.modifyPw(menu.pwdList[2]) # 修改密码
        text = menu.errorDialog(menu.closeBtn)
        self.assertIn('旧密码输入错误！', text, '旧密码输入错误！') # 新密码和确认码不同时断言提示信息

    def test_modify_password_difference(self):
        """旧密码非空,新密码不等于确认密码且新密码满足条件,修改密码失败,弹窗提示"""
        self.login.loginFunc()
        menu = PrimaryMenu(self.driver)
        menu.modifyPwMenu() # 查找修改密码页面
        menu.modifyPw(menu.pwdList[3]) # 修改密码
        text = menu.errorDialog(menu.closeBtn)
        self.assertIn('两次输入的新密码不同！', text, '两次输入的新密码不同！') # 新密码和确认码不同时断言提示信息

    def test_modify_password_all_blank(self):
        """旧密码,新密码,确认密码任意为空,修改密码失败,弹窗提示"""
        self.login.loginFunc()
        menu = PrimaryMenu(self.driver)
        menu.modifyPwMenu() # 查找修改密码页面
        menu.modifyPw(menu.pwdList[4]) # 修改密码
        text = menu.errorDialog(menu.closeBtn)
        self.assertIn('该输入项的值不能为空！', text, ' 该输入项的值不能为空！') # 所有密码均为空时断言提示信息

    def test_modify_password(self):
        """循环校验提示信息"""
        self.login.loginFunc()
        menu = PrimaryMenu(self.driver)
        menu.modifyPwMenu() # 查找修改密码页面
        error_list = []
        for list in range(len(menu.pwdList)):
            menu.modifyPw(menu.pwdList[list])
            if menu.isElementExist(menu.errMessage):
                text = menu.errorDialog(menu.closeBtn) # 这里只判断是否有提示框弹出，如有说明修改失败，没有或者其他提示框默认为修改成功
                error_list.append(text)
            else:
                self.assertTrue(menu.isElementExist(*menu.errMessage), 'error fram not exist, please open bug')
        self.assertEqual('密码长度至少 4 位！',error_list[0],'log infomation error!')
        self.assertEqual('密码强度不够，请重新输入密码！', error_list[1], 'log infomation error!')
        self.assertEqual('旧密码输入错误！', error_list[2], 'log infomation error!')
        self.assertEqual('两次输入的新密码不同！', error_list[3], 'log infomation error!')
        self.assertEqual('该输入项的值不能为空！', error_list[4], 'log infomation error!')

    def test_modifypw(self):
        """循环测试修改密码功能"""
        self.login.loginFunc()# 登录
        menu = PrimaryMenu(self.driver)
        menu.modifyPwMenu()  # 查找修改密码页面
        for item in menu.pwdList:
            menu.modifyPw(item)
            if menu.isElementExist(menu.errMessage):  # 如果存在提示框 再断言提示信息是否正确
                if item[0] != '' and len(item[1]) < 4  and item[2] !='': # 新密码长度校验
                    text = menu.errorDialog(menu.closeBtn)
                    try:
                        self.assertEqual('密码长度至少 4 位！',text,'the message incorrect!')
                    except Exception:
                        menu.saveScreenShot('fail_密码长度.png')
                        raise
                elif item[0] != '' and len(item[1]) >= 4 and item[2] !='': # 新密码强度校验 ['a', 'qwert', 'qwert'],
                    lowercase, uppercase, number, other=strhandle(item[1])
                    if lowercase > 0 and uppercase > 0 and number == 0 and other == 0: # 小写 大写
                        text = menu.errorDialog(menu.closeBtn)
                        self.assertIn('密码强度不够，请重新输入密码！', text, ' 密码强度不够，请重新输入密码！')
                    elif uppercase > 0 and other > 0 and number == 0 and lowercase == 0: # 大写 特殊字符
                        text = menu.errorDialog(menu.closeBtn)
                        self.assertIn('密码强度不够，请重新输入密码！', text, ' 密码强度不够，请重新输入密码！')
                    elif lowercase >0 and other > 0 and number == 0 and uppercase == 0: # 小写 特殊字符
                        text = menu.errorDialog(menu.closeBtn)
                        self.assertIn('密码强度不够，请重新输入密码！', text, ' 密码强度不够，请重新输入密码！')
                    elif lowercase == 0 and other == 0 and number > 0 and uppercase > 0:  # 大写 数字
                        text = menu.errorDialog(menu.closeBtn)
                        self.assertIn('密码强度不够，请重新输入密码！', text, ' 密码强度不够，请重新输入密码！')
                    elif lowercase > 0 and other == 0 and number > 0 and uppercase == 0:  # 小写 数字
                        text = menu.errorDialog(menu.closeBtn)
                        self.assertIn('密码强度不够，请重新输入密码！', text, ' 密码强度不够，请重新输入密码！')
                    elif lowercase > 0 and other == 0 and number == 0 and uppercase == 0:
                        text = menu.errorDialog(menu.closeBtn)
                        self.assertIn('密码强度不够，请重新输入密码！', text, ' 密码强度不够，请重新输入密码！')
                    elif lowercase == 0 and other > 0 and number == 0 and uppercase == 0:
                        text = menu.errorDialog(menu.closeBtn)
                        self.assertIn('密码强度不够，请重新输入密码！', text, ' 密码强度不够，请重新输入密码！')
                    elif lowercase == 0 and other == 0 and number > 0 and uppercase == 0:
                        text = menu.errorDialog(menu.closeBtn)
                        self.assertIn('密码强度不够，请重新输入密码！', text, ' 密码强度不够，请重新输入密码！')
                    elif lowercase == 0 and other == 0 and number == 0 and uppercase > 0:
                        text = menu.errorDialog(menu.closeBtn)
                        self.assertIn('密码强度不够，请重新输入密码！', text, ' 密码强度不够，请重新输入密码！')
                    elif item[0] != 'qwert1234!@#' and item[1] == item[2]:# >= 4
                        lowercase, uppercase, number, other = strhandle(item[1])
                        if (lowercase > 0 and uppercase > 0 and number > 0) or (
                                    lowercase > 0 and uppercase > 0 and other > 0) or (
                                    number > 0 and other > 0 and lowercase > 0) or (
                                    number > 0 and other > 0 and uppercase > 0):
                            text = menu.errorDialog(menu.closeBtn)
                            self.assertIn('旧密码输入错误！', text, '旧密码输入错误！')  # 新密码和确认码不同时断言提示信息
                    elif item[0] == 'qwert1234!@#$' and item[1] != item[2]:# and item[1] >= 4:
                        lowercase, uppercase, number, other = strhandle(item[1])
                        if (lowercase > 0 and uppercase > 0 and number > 0) or (
                                            lowercase > 0 and uppercase > 0 and other > 0) or (
                                            number > 0 and other > 0 and lowercase > 0) or (
                                            number > 0 and other > 0 and uppercase > 0):
                            text = menu.errorDialog(menu.closeBtn)
                            self.assertIn('两次输入的新密码不同！', text, ' 两次输入的新密码不同！')
                    else:
                        print('test value incorrect! please check it')
                elif item[0] == '' or item[1] =='' or item[2] =='': # 输入项为空校验
                    text = menu.errorDialog(menu.closeBtn)
                    self.assertIn('该输入项的值不能为空！', text, ' 该输入项的值不能为空！')  # 所有密码均为空时断言提示信息
            else:
                self.assertTrue(menu.isElementExist(menu.errMessage), 'error fram not exist, please check the test value or file bug')

if __name__=='__main__':
    pass