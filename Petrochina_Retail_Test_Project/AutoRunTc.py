#! user/bin/python
'''
Code description： auto run test case
Create time：
Developer：
'''

import unittest
from retail.test_case.models.testreport import *
from retail.test_case.models.sendmail import SendMail
from retail.test_case.models.sendmail import getReceiverInfo
from retail.test_case.LoginTc import Login_TC
from retail.test_case.ModifyPwTc import ModifyPw_TC
from retail.test_case.MemeberQueryTc import MemberQuery_TC
from retail.test_case.PointQueryTc import PointQuery_TC
from retail.test_case.CompanyQueryTc import CompanyQuery_TC
from retail.test_case.ActiveRuleTc import ActiveRule_TC
from retail.test_case.CreateRuleTc import CreateRule_TC
 # 登录模块测试用例场景
class RunTcScript(object):
    """

    """
    def __init__(self):
        self.suite = unittest.TestSuite()
        # 2.---------------------------------
        # self.suite = addTc('login_TC.py')
        # 2.---------------------------------
    # 登录模块测试用例
    def load_login_tc(self,testcase):
        """

        :param testcase:
        :return:
        """
        self.suite.addTest(Login_TC(testcase))
    # 修改密码测试用例
    def load_modifypw_tc(self,testcase):
        """

        :param testcase:
        :return:
        """
        self.suite.addTest(ModifyPw_TC(testcase))
    # 会员档案查询测试用例
    def load_memberquery_tc(self,testcase):
        """

        :param testcase:
        :return:
        """
        self.suite.addTest(MemberQuery_TC(testcase))
    # 积分消费查询测试用例
    def load_pointquery_tc(self,testcase):
        """

        :param testcase:
        :return:
        """
        self.suite.addTest(PointQuery_TC(testcase))
    # 积分消费查询-积分查询-单位选择页面测试用例
    def load_companyquery_tc(self, testcase):
        """

        :param testcase:
        :return:
        """
        self.suite.addTest(CompanyQuery_TC(testcase))

    # 积分规则/活动申请测试用例
    def load_activerule_tc(self, testcase):
        """

        :param testcase:
        :return:
        """
        self.suite.addTest(ActiveRule_TC(testcase))
    # 添加规则测试用例
    def load_createrule_tc(self, testcase):
        """

        :param testcase:
        :return:
        """
        self.suite.addTest(CreateRule_TC(testcase))
if __name__ =='__main__':
    # 1.2.3
    suite_tc = RunTcScript()
    # login test cases
    suite_tc.load_login_tc('test_login_success_correct_username_password') # testcase 1 ： 登录成功
    # suite_tc.load_login_tc('test_login_failed_incorrect_username') # testcase 2 : 用户名错误 密码正确
    # suite_tc.load_login_tc('test_login_failed_incorrect_password') # testcase 3 : 用户名正确 密码错误
    # suite_tc.load_login_tc('test_login_failed_username_password_blank') # testcase 4: 用户名位空或全部位空
    # suite_tc.load_login_tc('test_login_failed_password_blank') # testcase 5：密码为空
    # suite_tc.load_login_tc('test_login_failed_unpw_incorrect') # testcase 6：用户名和密码都错误
    # suite_tc.load_login_tc('test_login') # testcase 7：循环test
    # modify password test cases
    # suite_tc.load_modifypw_tc('test_menu_is_display') # testcase 8：遍历主菜单
    # suite_tc.load_modifypw_tc('test_modify_password_len') # testcase 9: 修改密码 密码长度校验
    # suite_tc.load_modifypw_tc('test_modify_password_strebgth') # testcase 10: 修改密码 密码强度校验
    # suite_tc.load_modifypw_tc('test_modify_password_incorrect') # testcase 11: 修改密码 新密码和确认密码不一样
    # suite_tc.load_modifypw_tc('test_modify_password_difference') # testcase 12：新密码和旧密码不同
    # suite_tc.load_modifypw_tc('test_modify_password_all_blank') # testcase 13: 修改密码 所有密码都为空
    # suite_tc.load_modifypw_tc('test_modify_password') # testcase 14: 循环测试密码修改功能
    # suite_tc.load_modifypw_tc('test_modifypw') # testcase 15 ：循环（优化）
    # memeber record query ui check
    # suite_tc.load_memberquery_tc('test_member_check_ui') # testcase 16: 校验会员档案查询页面元素
    # suite_tc.load_memberquery_tc('test_member_type') # testcase 17: 验证会员类型下拉列表
    # suite_tc.load_memberquery_tc('test_member_level') # testcase 18: 验证会员级别下拉列表
    # suite_tc.load_memberquery_tc('test_member_query_failed') # testcase 19: 验证默认查询
    # suite_tc.load_memberquery_tc('test_alone_query_1') # testcase 20: 单一查询(会员编号，会员姓名，手机号码)
    # suite_tc.load_memberquery_tc('test_alone_query_2') # testcase 21: 单一查询(会员类型）
    # suite_tc.load_memberquery_tc('test_alone_query_3') # testcase 22: 单一查询（会员级别）
    # suite_tc.load_memberquery_tc('test_reset') # testcase 23：验证重置功能

    # point consume query
    # suite_tc.load_pointquery_tc('test_point_query_page_check') # testcase 24: 页面检查
    # suite_tc.load_pointquery_tc('test_changePage') # testcase 25
    # suite_tc.load_pointquery_tc('test_point_required_field') # testcase 26: 必填项校验
    # suite_tc.load_pointquery_tc('test_inputitem_check')

    # conpany query
    # suite_tc.load_companyquery_tc('Test_Jump') # testcase 27: 页面跳转校验
    # suite_tc.load_companyquery_tc('Test_Default_Query') # testcase 28: 默认查询
    # suite_tc.load_companyquery_tc('Test_Alone_Query') # testcase 29：单位选择页面查询

    # active rule
    # suite_tc.load_activerule_tc('test_default_input') # 30
    # suite_tc.load_activerule_tc('test_default_rule') # 31
    # suite_tc.load_activerule_tc('test_page_jump') # 32
    # suite_tc.load_activerule_tc('test_rule_message') # 33
    # suite_tc.load_activerule_tc('test_activity_massage') # 34
    # suite_tc.load_activerule_tc('test_activity_jump') # 35

    # create rule
    # suite_tc.load_createrule_tc('test_default_append') # 36
    # suite_tc.load_createrule_tc('test_success_addrule')# 37

    # 3.输出到测试报告--------------------------------
    # runner, fp, filename = testreport()
    # runner.run(suite_tc.suite)
    # 3.--------------------------------------------
    # fp.close()
    # read_msg=getReceiverInfo(r'D:\Petrochina_Retail_Test_Project\retail\data\mail_receiver.txt')
    # sendmail = SendMail(read_msg, 'smtp.qq.com', '281754043@qq.com', 'gifhhsbgqyovbhhc', '281754043@qq.com')
    # sendmail.send_email(filename)
    # 1.不输出到测试报告
    runner = unittest.TextTestRunner(verbosity=2)# 输出详细信息
    runner.run(suite_tc.suite)
    #fp.close()

    # 2. 输出测试报告 BeautifulReport---------------
    # 导入模块时需要使用绝对路径 否则报错
    # suite = addTc(rule='LoginTc.py')
    # runTc(suite)
    # 2 -------------------------------------------

