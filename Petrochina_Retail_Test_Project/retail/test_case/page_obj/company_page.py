'''
Code description：单位选择 page
Create time：
Developer：
'''

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import logging
from retail.test_case.page_obj.pointquery_page import PointConsume, eleData
from retail.test_case.models.log import Logger

log = Logger(__name__, CmdLevel=logging.INFO, FileLevel=logging.INFO)

class CompanyQuery(PointConsume):

    testValues = [['1', 'EA', 'EA10']]

    # 加油站名称
    oilStationBtn = (By.XPATH, eleData.readExcel(58, 3))

    # 查询条件
    queryBox = (By.XPATH, eleData.readExcel(59, 3))

    # 单位选择窗口
    companyIfarm = (By.XPATH, eleData.readExcel(60, 3))

    # 数据表
    valueTable = (By.XPATH, eleData.readExcel(61, 3))

    # 查询与重置按钮
    queryReset = \
        [(By.XPATH, eleData.readExcel(62, 3)),# 查询
         (By.XPATH, eleData.readExcel(63, 3))]# 重置

    # 点击加油站名称
    def clickOilStation(self):
        btn = self.findElement(*self.oilStationBtn)
        try:
            ActionChains(self.driver).move_to_element(btn).perform()
            btn.click()
        except Exception:
            log.logger.exception('the element not found, move_to requires a WebElement', exc_info=True)
            raise
        else:
            log.logger.info('found the element [%s] and mouse already removed and click on it ' %btn)
            self.driver.implicitly_wait(2)

    # 获取单位选择窗口title
    @property
    def getTitle(self):
        title = self.findElement(*self.companyIfarm).text
        log.logger.info(f"get the title of [{self.companyIfarm}] success")
        return title


if __name__ == '__main__':
    pass