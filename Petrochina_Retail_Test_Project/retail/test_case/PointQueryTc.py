'''
Code description：积分消费查询/积分查询 testcase
Create time：
Developer：
'''

from retail.test_case.models.myunit import MyunitTest
from retail.test_case.page_obj.pointquery_page import PointConsume

class PointQuery_TC(MyunitTest):

    """积分消费查询/积分查询模块测试用例"""

    def test_point_query_page_check(self):
        """积分查询页面检查"""
        # 初始化积分消费查询页面
        menu = PointConsume(self.driver)
        self.login.loginFunc()
        menu.integrateMenu()  # 查找积分查询菜单
        elements = menu.find_elements_re(*menu.uiElements)
        ele_list = []
        for eles in elements:
            if eles.text != '':
                ele_list.append(eles.text)
        self.assertEqual('积分结果查询', ele_list[0])
        self.assertEqual('查询条件', ele_list[1])
        self.assertEqual('积分累计明细', ele_list[2])

    def test_point_required_field(self):
        """查询条件必填项校验"""
        menu = PointConsume(self.driver)
        self.login.loginFunc() # 登录
        menu.integrateMenu()
        for num in range(len(menu.inputIterm)):
            menu.inputQueryValue(menu.inputIterm[num], menu.valuesList[num])
            menu.cQueryResetBtn(menu.queryReset[0])
            flag1 = menu.isElementExist(menu.errFram)
            if flag1:
                self.assertTrue(flag1,'存在必填项未输入')
                menu.accept(*menu.errBtn)
            else:
                self.assertFalse(flag1, '无必填项需要输入')

    def test_inputitem_check(self):
        """会员编号, 月份, 省编码输入项校验"""
        menu = PointConsume(self.driver)
        self.login.loginFunc() # 登录
        menu.integrateMenu()
        for num in range(len(menu.checkList)):
            menu.inputQueryValue(menu.inputIterm[2], menu.checkList[num][0])
            menu.inputQueryValue(menu.inputIterm[3], menu.checkList[num][1])
            menu.inputQueryValue(menu.inputIterm[4], menu.checkList[num][2])
            menu.cQueryResetBtn(menu.queryReset[0])
            flag = menu.isElementExist(menu.errMsg)
            if flag:
                info = menu.getValue(*menu.errMsg)
                self.assertEqual('请求处理异常', info, '提示信息有误')
                menu.closeErrMsg(menu.closeBtn)
            else:
                self.assertFalse(flag, 'no err msg please file a bug!')
                continue
    def test_changePage(self):
        """页面跳转"""
        menu = PointConsume(self.driver)
        self.login.loginFunc()
        menu.integrateMenu()
        self.driver.implicitly_wait(5)
        menu.changePage()
        elements = menu.find_elements_re(*menu.uiElements)
        ele_list = []
        for eles in elements:
            if eles.text !='':
                ele_list.append(eles.text)
        self.assertEqual('积分结果查询', ele_list[0])
        self.assertEqual('查询条件', ele_list[1])
        self.assertEqual('交易记录明细', ele_list[2])


if __name__ == '__main__':
    pass
