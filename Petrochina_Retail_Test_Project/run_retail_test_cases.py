#! user/bin/python
#----------------------------------
'''                                                           
代码说明： 主函数 组织测试用例 并运行测试用例
编写日期： 2018.08.13
设计  者： linux超
'''
#----------------------------------

import unittest
from retail.test_case.models.test_report import Test_Report
from retail.test_case.models.send_mail import send_mail_init_info
from retail.test_case.models.send_mail import read_SendToUserinfo_file
from retail.test_case.login_module_testcase import Login_Test_Cases
from retail.test_case.modify_password_testcase import Primary_Menu_Test_Cases
from retail.test_case.memeber_query_testcases import Member_Record_Query_Test_Cases
from retail.test_case.point_query_testcase import Point_Query_Test_Cases
#   登录模块测试用例场景
class Run_Test_Cases_Scenario(object):
    def __init__(self):
        self.suite = unittest.TestSuite()
    # 登录模块测试用例
    def load_login_test_cases(self,testcase):
        self.suite.addTest(Login_Test_Cases(testcase))
    # 修改密码测试用例
    def load_modify_test_cases(self,testcase):
        self.suite.addTest(Primary_Menu_Test_Cases(testcase))
    # 会员档案查询测试用例
    def load_member_test_cases(self,testcase):
        self.suite.addTest(Member_Record_Query_Test_Cases(testcase))
    # 积分消费查询测试用例
    def load_point_consume_test_cases(self,testcase):
        self.suite.addTest(Point_Query_Test_Cases(testcase))

if __name__ =='__main__':
    #suite = unittest.TestSuite()
    suite_test_case = Run_Test_Cases_Scenario()
    #   login test cases
    # suite_test_case.load_login_test_cases('test_login_success_correct_username_password') # testcase 1 ： 登录成功
    # suite_test_case.load_login_test_cases('test_login_failed_incorrect_username') # testcase 2 : 用户名错误 密码正确
    # suite_test_case.load_login_test_cases('test_login_failed_incorrect_password') # testcase 3 : 用户名正确 密码错误
    # suite_test_case.load_login_test_cases('test_login_failed_username_password_blank') # testcase 4: 用户名位空或全部位空
    # suite_test_case.load_login_test_cases('test_login_failed_password_blank') # testcase 5：密码为空
    #   modify password test cases
    # suite_test_case.load_modify_test_cases('test_menu_is_display') # testcase 6：遍历主菜单
    # suite_test_case.load_modify_test_cases('test_modify_password_len') # testcase 7: 修改密码 密码长度校验
    # suite_test_case.load_modify_test_cases('test_modify_password_strebgth') # testcase 8: 修改密码 密码强度校验
    # suite_test_case.load_modify_test_cases('test_modify_password_difference') # testcase 9: 修改密码 新密码和确认密码不一样
    # suite_test_case.load_modify_test_cases('test_modify_password_all_blank') # testcase 10: 修改密码 所有密码都为空
    # suite_test_case.load_modify_test_cases('test_modify_password') # testcase 11: 循环测试密码修改功能
    #   memeber record query ui check
    # suite_test_case.load_member_test_cases('test_member_check_ui') # testcase 12: 校验会员档案查询页面元素
    suite_test_case.load_member_test_cases('test_member_type') # testcase 13: 验证会员类型下拉列表
    # suite_test_case.load_member_test_cases('test_member_level') # testcase 14: 验证会员级别下拉列表
    #suite_test_case.load_member_test_cases('test_member_query_failed') # testcase 15: 验证默认查询
    #suite_test_case.load_member_test_cases('test_alone_query_1') # testcase 16: 单一查询(会员编号，会员姓名，手机号码)
    #suite_test_case.load_member_test_cases('test_alone_query_2') # testcase 17: 单一查询(会员类型）
    #suite_test_case.load_member_test_cases('test_alone_query_3') # testcase 18: 单一查询（会员级别）
    #suite_test_case.load_member_test_cases('test_reset') # testcase 19：验证重置功能

    #   point consume query
    #suite_test_case.load_point_consume_test_cases('test_point_query_page_check') # testcase 20: 页面检查
    #suite_test_case.load_point_consume_test_cases('test_point_required_field') # testcase 21: 必填项校验
    # runner, fp, filename = Test_Report()
    # runner.run(suite_test_case.suite)
    # fp.close()
    # read_msg=get_receiverinfo(r'D:\Petrochina_Retail_Test_Project\retail\data\mail_receiver.txt')
    # sendmail = send_mail(read_msg, 'smtp.qq.com', '281754043@qq.com', 'gifhhsbgqyovbhhc', '281754043@qq.com')
    # sendmail.send_email(filename)
    runner = unittest.TextTestRunner(verbosity=2)# 输出详细信息
    runner.run(suite_test_case.suite)
    #fp.close()

