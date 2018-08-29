#----------------------------------
'''                                                           
代码说明：公共登录方法
编写日期：2018.08.15
设计  者：Linux超
'''
#----------------------------------

from selenium import webdriver

def Login_function_public(driver, userid='username', passwordid='password', username='rmln', password='qwert1234!@#$'):
    driver.find_element_by_id(userid).send_keys(username)
    driver.find_element_by_id(passwordid).send_keys(password)
    driver.find_element_by_id('loginSubmitButton').click()

if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.get('http://11.11.164.134:9081/rmms/modules/ep.rmms.portal/login/login.jsp')
    Login_function_public(driver)
