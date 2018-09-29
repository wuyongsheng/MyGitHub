'''
Code description：会员档案查询 testcase
Create time：
Developer：
'''

import random
import time
from selenium.webdriver.common.action_chains import ActionChains
from retail.test_case.models.myunit import MyunitTest
from retail.test_case.page_obj.memeberquery_page import MemberQuery

class MemberQuery_TC(MyunitTest):

    """会员档案查询模块测试用例"""

    #@unittest.skip('dont run the test case')
    def test_member_check_ui(self):
        """会员档案查询页面显示正确"""
        menu = MemberQuery(self.driver) # 实例化会员查询页面
        self.login.loginFunc()
        menu.memberQueryMenu()  # 查找会员档案查询菜单
        elements = menu.find_elements_re(*menu.uiElements)
        ele_list = []
        for eles in elements:
            if eles.text !='':
                ele_list.append(eles.text)
        self.assertEqual('查询条件', ele_list[0])
        self.assertEqual('会员信息明细', ele_list[1])
        self.assertEqual('积分变化明细', ele_list[2])


    def test_member_type(self):
        """会员类型下拉列表项正确"""
        menu = MemberQuery(self.driver)  # 实例化会员查询页面
        self.login.loginFunc()# 登录
        menu.memberQueryMenu()  # 查找会员档案查询菜单
        menu.selectMemberType()
        list_type = []
        for member_type in menu.memberTypeNum:  # 循环遍历会员类型下拉列表
            text, memeber_type_level = menu.memberTypeLevelOption(*member_type)
            list_type.append(text)
        self.assertEqual('个人会员', list_type[0])
        self.assertEqual('企业会员', list_type[1])
        self.assertEqual('其它', list_type[2])

    def test_member_level(self):
        """会员级别下拉列表项正确"""
        menu = MemberQuery(self.driver)  # 实例化会员查询页面
        self.login.loginFunc()  # 登录
        menu.memberQueryMenu() # 查找会员档案查询菜单
        menu.selectMemberLevel()
        list_level = []
        for member_level in menu.memberLevelNum: # 循环遍历会员级别下拉列表
            text, memeber_type_level = menu.memberTypeLevelOption(*member_level)
            list_level.append(text)
        self.assertEqual('标准会员', list_level[0])
        self.assertEqual('黄金会员', list_level[1])
        self.assertEqual('铂金会员', list_level[2])
        self.assertEqual('钻石会员', list_level[3])

    # ............................................................................................#
    # 对页面的条件进行组合后单击查询按钮。这是一个大数据量的操作，因此不对返回数据做校验，只看本次组合的条件在页面是否可正常使用。
    # 如果查询失败，系统会有弹出框提示失败原因，这个应该很好理解的。
    # 我们抓取这个框是否在一定的时间内出现，如果出现则判定本次查询失败，记录用例结果。
    # ............................................................................................#

    def test_member_query_failed(self):
        """默认条件查询成功"""
        menu = MemberQuery(self.driver)  # 实例化会员档案查询页面
        self.login.loginFunc()  # 登录
        menu.memberQueryMenu()  # 找到会员查询页面
        menu.cQueryResetBtn(*menu.queryResetBtn[0])  # 点击[查询]
        flag = menu.isElementExist(menu.qFailerr)  # 断言错误提示框
        self.assertFalse(flag, msg='查询失败')  # flag为false时，断言成功， 无提示框，说明默认查询成功

    def test_alone_query_1(self):
        """按会员编号,会员姓名,手机号码单一条件查询"""
        menu = MemberQuery(self.driver)  # 实例化会员档案查询页面
        self.login.loginFunc()  # 登录
        menu.memberQueryMenu()  # 找到会员档案查询页面
        for num_name_phone in menu.memberNumNamePhone:
            menu.reset()  # 重置
            for value in menu.valuesList:
                menu.iQueryCondition(num_name_phone,value)
                menu.cQueryResetBtn(*menu.queryResetBtn[0]) # 点击[查询]
                time.sleep(3)
                flag = menu.isElementExist(menu.qFailerr)
                if flag:
                    self.assertTrue(flag, '提示框不存在，查询成功')
                    menu.accept(*menu.confirmBtn)
                else:
                    self.assertFalse(flag, '提示框存在，查询失败')

    def test_alone_query_2(self):
        """按会员类型单一查询"""
        menu = MemberQuery(self.driver) # 实例化会员档案查询页面
        self.login.loginFunc() # 登录
        menu.memberQueryMenu() # 找到会员档案查询页面
        for me_type in menu.memberTypeNum:
            menu.selectMemberType() # 点击[会员类型]
            text, member_type_level = menu.memberTypeLevelOption(*me_type) # 遍历每一个下拉选项
            ActionChains(self.driver).move_to_element(member_type_level).perform() # 鼠标移动到下拉选项上
            member_type_level.click() # 选中下拉选项
            menu.cQueryResetBtn(*menu.queryResetBtn[0])  # 点击[查询]
            time.sleep(3)
            flag = menu.isElementExist(menu.qFailerr) # 判断查询成功
            self.assertFalse(flag, '提示框存在，查询失败')

    def test_alone_query_3(self):
        """按会员级别单一查询"""
        menu = MemberQuery(self.driver)  # 实例化会员档案查询页面
        self.login.loginFunc()  # 登录
        menu.memberQueryMenu()  # 找到会员档案查询页面
        for me_level in menu.memberLevelNum:
            menu.selectMemberLevel() # 点击[会员级别]
            text, member_level = menu.memberTypeLevelOption(*me_level)  # 遍历每一个下拉选项
            ActionChains(self.driver).move_to_element(member_level).perform()  # 鼠标移动到下拉选项上
            member_level.click()  # 选中下拉选项
            menu.cQueryResetBtn(*menu.queryResetBtn[0])  # 点击[查询]
            time.sleep(3)
            flag = menu.isElementExist(menu.qFailerr)  # 判断查询成功
            self.assertFalse(flag, '提示框存在，查询成功')

    def test_reset(self):
        """重置功能校验"""
        menu = MemberQuery(self.driver) # 实例化会员档案查询页面
        self.login.loginFunc() # 登录
        menu.memberQueryMenu() # 找到会员档案查询页面
        # 3个条件输入框随机输入数据
        for inputBox in menu.memberNumNamePhone:
            menu.iQueryCondition(inputBox,random.choice(menu.valuesList))
        #会员类型下拉列表中随机选择一项
        menu.selectMemberType()
        text_type, member_type = menu.memberTypeLevelOption(*(random.choice(menu.memberTypeNum)))
        ActionChains(self.driver).move_to_element(member_type).perform()  # 鼠标移动到下拉选项上
        member_type.click()

        # menu.selectMemberLevel()
        # text_level, member_level = menu.memberTypeLevelOption(*(random.choice(menu.member_level_num)))
        # #ActionChains(self.driver).move_to_element(member_level).perform()
        # member_level.click()


        # 点击【重置】
        menu.cQueryResetBtn(*menu.queryResetBtn[1])
        # 获取前3个输入框的内容
        text_list = []
        for input_box in menu.memberNumNamePhone:
            text = menu.getInputboxValue(*input_box)
            text_list.append(text)
        # 获取会员类型
        type_type_text = menu.getInputboxValue(*menu.memberTypeBtn)
        text_list.append(type_type_text)

        # type_level_text = menu.getInputboxValue(*menu.member_level_btn)
        # text_list.append(type_level_text)

        # 断言每一个条件框是否为空 为空就通过
        for get_attr in text_list:
            self.assertEqual('',get_attr)

if __name__ == '__main__':
    pass
