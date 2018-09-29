'''
Code description：积分消费查询/加油站名称选择页 testcase
Create time：
Developer：
'''

import time
from retail.test_case.models.myunit import MyunitTest
from retail.test_case.page_obj.company_page import CompanyQuery

class CompanyQuery_TC(MyunitTest):

    """积分消费查询/加油站名称选择页测试用例"""

    def Test_Jump(self):
        """加油站名称/单位选择页面跳转正确"""
        menu = CompanyQuery(self.driver)
        self.login.loginFunc()
        menu.integrateMenu()
        menu.clickOilStation()
        flag = menu.isElementExist(menu.companyIfarm)
        if flag:
            title = menu.getTitle
            self.assertIn('单位选择', title, '页面跳转失败')
            self.assertTrue(flag, '页面跳转失败')
        else:
            print(*menu.oilStationBtn+'按钮无效')

    def Test_Default_Query(self):
        """加油站名称/单位选择页面默认查询成功"""
        menu = CompanyQuery(self.driver)
        self.login.loginFunc()
        menu.integrateMenu()
        menu.clickOilStation()
        time.sleep(2)
        menu.cQueryResetBtn(menu.queryReset[0])
        time.sleep(2)
        value_list = menu.getValues(*menu.valueTable)
        self.assertTrue(value_list, msg='查询失败') # 断言是否存在数据

    def Test_Alone_Query(self):
        """加油站名称/单位选择页面单一条件查询成功"""
        menu = CompanyQuery(self.driver)
        self.login.loginFunc()
        menu.integrateMenu()
        menu.clickOilStation()
        time.sleep(2)
        for value in menu.testValues:
            for va in value:
                list_num = []
                list_name = []
                menu.inputQueryValue(menu.queryBox, va)
                menu.cQueryResetBtn(menu.queryReset[0])
                time.sleep(3)
                try:
                    value_list = menu.getValues(*menu.valueTable)
                except Exception:
                    raise ('输入的查询条件无效')
                else:
                    # 对数据 做处理： 加油站编码和名称分开
                    for index in range(len(value_list)):
                        if (index == 0) or (index % 2 ==0):
                            list_num.append(value_list[index])
                        elif (index % 2 != 0):
                            list_name.append(value_list[index])
                    if list_name:
                        for num in range(len(list_num)):
                            oil_num = list_num[num]
                            oil_name = list_name[num]
                            num_name = oil_num+oil_name
                            self.assertIn(va, num_name, '查询结果与输入条件不匹配')
                    else:
                        print("无数据")

if __name__ == '__main':
    pass

