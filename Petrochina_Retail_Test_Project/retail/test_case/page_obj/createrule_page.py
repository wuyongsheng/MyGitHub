'''
Code description：创建规则 page
Create time：
Developer：
'''

from selenium.webdriver.common.by import By
import time
from retail.test_case.page_obj.activerule_page import ActiveRule, eleData

class CreateRule(ActiveRule):
    # 创建积分规则页面元素(必填输入项)
    elesList = \
        [(By.ID, eleData.readExcel(81, 3)), # 积分累计规则名称
        (By.ID, eleData.readExcel(82, 3)), # 规则起始日期
        (By.ID, eleData.readExcel(83, 3)), # 规则结束日期
        (By.ID, eleData.readExcel(84, 3)), # 有效起始时间
        (By.ID, eleData.readExcel(85, 3)), # 有效结束时间
        (By.ID, eleData.readExcel(86, 3))] # 积分系数

    # 创建积分规则页面元素(非必填项)
    rulDes = (By.XPATH, eleData.readExcel(87, 3)) # 积分累计规则描述
    minAmt = (By.ID, eleData.readExcel(88, 3)) # 最小金额
    maxAmt = (By.ID, eleData.readExcel(89, 3)) # 最大金额
    payNum = (By.ID, eleData.readExcel(90, 3)) # 活动消费次数
    sumAmt = (By.ID, eleData.readExcel(91, 3)) # 活动消费金额

    # 必填项测试数据
    valList = ['测试规则名称'+ time.strftime('%Y-%m-%d'),
                 '2018-09-11', '2018-09-12', '00:00:00', '23:59:59', '2']
    # 错误提示框
    msg_Info = (By.XPATH, eleData.readExcel(92, 3))
    # 保存
    sBtn = (By.LINK_TEXT, eleData.readExcel(93, 3))
    # 规则层级
    ruleLevel = (By.ID, eleData.readExcel(94, 3))

    levelItem = (By.LINK_TEXT, eleData.readExcel(95, 3))
    # 会员级别
    memberLevel = (By.ID, eleData.readExcel(96, 3))
    # 支付方式
    payMode = (By.ID, eleData.readExcel(97, 3))
    # 商品级别
    wareLevel = (By.ID, eleData.readExcel(98, 3))
    # 积分类型
    scoreType = (By.ID, eleData.readExcel(99, 3))
    # 累计类型
    addType = (By.ID, eleData.readExcel(100, 3))

    def pickItem(self,ruleLevel, levelItem):
        """

        :param ruleLevel:
        :param levelItem:
        :return:
        """
        self.cBtn(ruleLevel)
        self.selectItem(levelItem)



if __name__=='__main__':
    pass