'''
Code description：积分规则/活动申请/添加规则模块 testcase
Create time：
Developer：
'''

import time
from retail.test_case.models.myunit import MyunitTest
from retail.test_case.page_obj.createrule_page import CreateRule

class CreateRule_TC(MyunitTest):

    """积分规则/活动申请/添加规则模块测试用例"""

    def test_default_append(self):
        """累计活动,默认添加规则失败"""
        menu = CreateRule(self.driver)
        self.login.loginFunc()
        menu.addRuleMenu()
        menu.cBtn(menu.typeBtn)
        time.sleep(2)
        menu.selectItem(menu.typeItem[1])
        menu.inputGroupValue(menu.eleList, menu.valueList)
        menu.cBtn(menu.addruleBtn)
        menu.cBtn(menu.sBtn)
        time.sleep(2)
        flag = menu.isElementExist(menu.msg_Info)
        self.assertTrue(flag, '必填项未输入，无弹窗提示')
        if flag:
            message = menu.getValue(*menu.msg_Info)
            self.assertEqual(message, '该输入项的值不能为空！', '提示信息错误')

    def test_success_addrule(self):
        """累计活动,只填写必填项,创建规则成功"""
        menu = CreateRule(self.driver)
        self.login.loginFunc()
        menu.addRuleMenu()
        menu.cBtn(menu.typeBtn)
        time.sleep(2)
        menu.selectItem(menu.typeItem[1])
        menu.inputGroupValue(menu.eleList, menu.valueList)
        menu.cBtn(menu.addruleBtn)
        # 输入必填项
        menu.inputGroupValue(menu.elesList, menu.valList)
        # 其他必填项正确选择
        # menu.pickItem(menu.ruleLevel, menu.levelItem)
        # 未完成
if __name__=='__main__':
    pass