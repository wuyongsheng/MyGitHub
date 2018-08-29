#! user/bin/python
#----------------------------------
'''                                                           
代码说明：
编写日期：
设计  者：
'''
#----------------------------------
from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
driver.get('https://www.haixinglian.com/member/login.html')
time.sleep(2)

locator = (By.XPATH,"//*[@class='col-lg-4 header-right']/span[2]/a")
def find_element_re(*loc):
    try:
        WebDriverWait(driver,10).until(EC.visibility_of_element_located(loc))
        return driver.find_element(*loc)
    except:
        print('not found element')
        print('页面找不到元素 %s' % (loc))

ele = find_element_re(*locator)
print(ele.text)
ele.click()

