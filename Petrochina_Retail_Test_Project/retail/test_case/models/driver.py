#----------------------------------
'''                                                           
代码说明：不同的项目可以调用不同的浏览器，并且加载不同的url
编写日期：2018.08.13
设计  者：linux超
'''
#----------------------------------

from selenium import webdriver
import time

class Web_Driver(object):

    # Firefox driver
    def firefox_driver(self):
        self.driver = webdriver.Firefox()
        return self.driver

    # chrom driver
    def chrome_driver(self):
        self.driver = webdriver.Chrome()
        return self.driver

    # Ie driver
    def ie_driver(self):
        self.driver = webdriver.Ie()
        return self.driver

    # load url
    def load_url(self, driver, url=''):
        driver.get(url)

if __name__ == '__main__':
    driver = Web_Driver()
    web_driver = driver.firefox_driver()
    driver.load_url(web_driver,'http://11.11.164.134:9081/rmms/modules/ep.rmms.portal/login/login.jsp')
    time.sleep(5)
    web_driver.quit()

