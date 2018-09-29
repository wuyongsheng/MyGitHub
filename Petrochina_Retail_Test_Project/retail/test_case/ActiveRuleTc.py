'''
Code description：积分规则/活动申请模块 testcase
Create time：
Developer：
'''

import time
from retail.test_case.models.myunit import MyunitTest
from retail.test_case.page_obj.activerule_page import ActiveRule

class ActiveRule_TC(MyunitTest):

    """积分规则/活动申请模块测试用例"""

    def test_default_rule(self):
        """默认添加规则失败,弹窗提示"""
        menu = ActiveRule(self.driver)
        self.login.loginFunc()
        menu.addRuleMenu()
        menu.cBtn(menu.addruleBtn)
        flag = menu.isElementExist(menu.msgInfo)
        self.assertTrue(flag, '存在必填项未输入, 且无错误提示信息')
        if flag:
            msgInfo = menu.getValue(*menu.msgInfo)
            self.assertEqual(msgInfo, '请选择申请类型！', '错误提示信息错误')

    def test_default_input(self):
        """不同申请类型对应不同的输入项"""
        menu = ActiveRule(self.driver)
        self.login.loginFunc()
        menu.addRuleMenu()
        menu.cBtn(menu.typeBtn)
        for ele in menu.typeItem:
            menu.selectItem(ele)
            time.sleep(2)
            flag = menu.isElementExist(menu.eleList[1])
            if flag:
                self.assertTrue(flag, '与需求设计不符,其他项目不存在')
            else:
                self.assertFalse(flag, '与需求设计不符,除申请原因，申请类型其他项仍存在')
            menu.cBtn(menu.typeBtn)

    def test_page_jump(self):
        """选择积分累计规则,其他项正确填写,可以添加规则"""
        menu = ActiveRule(self.driver)
        self.login.loginFunc()
        menu.addRuleMenu()
        menu.inputValue(menu.eleList[0], menu.reason)
        menu.cBtn(menu.typeBtn)
        time.sleep(2)
        menu.selectItem(menu.typeItem[0])
        menu.cBtn(menu.addruleBtn)
        flag = menu.isElementExist(menu.createRule)
        self.assertTrue(flag, '页面跳转失败')
        if flag:
            pageTitle = menu.getValue(*menu.createRule)
            self.assertIn('创建积分规则', pageTitle, '页面跳转错误')
        else:
            menu.saveScreenShot('page_jump.png')

    def test_rule_message(self):
        """选择积分累计规则,缺省必填项,添加规则失败,弹窗提示"""
        menu = ActiveRule(self.driver)
        self.login.loginFunc()
        menu.addRuleMenu()
        menu.cBtn(menu.typeBtn)
        time.sleep(2)
        menu.selectItem(menu.typeItem[0])
        menu.cBtn(menu.addruleBtn)
        flag = menu.isElementExist(menu.msgInfo)
        try:
            self.assertTrue(flag, '存在必填项未输入, 且无错误提示信息')
        except Exception:
            menu.saveScreenShot('fail_rule_message.png')
            raise
        else:
            msgInfo = menu.getValue(*menu.msgInfo)
            self.assertEqual(msgInfo, '存在必填项未输入!', '错误提示信息错误')

    def test_activity_massage(self):
        """选择积分累计活动,缺省必填项,添加规则失败,弹窗提示"""
        menu = ActiveRule(self.driver)
        self.login.loginFunc()
        menu.addRuleMenu()
        menu.cBtn(menu.typeBtn)
        time.sleep(2)
        menu.selectItem(menu.typeItem[1])
        menu.cBtn(menu.addruleBtn)
        flag = menu.isElementExist(menu.msgInfo)
        self.assertTrue(flag, '存在必填项未输入, 且无错误提示信息')
        if flag:
            msgInfo = menu.getValue(*menu.msgInfo)
            self.assertEqual(msgInfo, '存在必填项未输入!', '错误提示信息错误')

    def test_activity_jump(self):
        """选择积分累计活动,正确填写必填项,可以添加规则"""
        menu = ActiveRule(self.driver)
        self.login.loginFunc()
        menu.addRuleMenu()
        menu.cBtn(menu.typeBtn)
        time.sleep(2)
        menu.selectItem(menu.typeItem[1])
        menu.inputGroupValue(menu.eleList, menu.valueList)
        menu.cBtn(menu.addruleBtn)
        flag = menu.isElementExist(menu.createRule)
        self.assertTrue(flag, '页面跳转失败')
        if flag:
            pageTitle = menu.getValue(*menu.createRule)
            self.assertIn('创建积分规则', pageTitle, '页面跳转错误')
        else:
            menu.saveScreenShot('activity_jump.png')

if __name__ == '__main__':
    pass