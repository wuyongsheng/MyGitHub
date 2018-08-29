#! user/bin/python
#----------------------------------
'''                                                           
代码说明： 
编写日期：
设计  者：
'''
#----------------------------------
from retail.test_case.models.myunit import Myunittest
import random
import unittest
import time
from selenium import webdriver
import sys
from selenium.common import exceptions
from retail.test_case.models.is_element_exist import Isnot_element_exist
from selenium.webdriver.common.action_chains import ActionChains

# 随机一个字符串
# list = ["a", "handsome",'xiaochao']
# print (random.choice(list))
# print(random.randint(1,3))
# m=0
# i = random.choice(list)
# if i =='a':
#     print(i)
#     m=1
# print(m)
# for i in range(3):
#     list.append(i)
# class mytest(Myunittest):
#     def test(self):
#         list = ["a", "handsome"]
#         for i in list:
#             self.assertEqual('a',i)
#
# if __name__=='__main__':
#     unittest.main()

#
# import time
# t = "50612/05/18 18:46:40"
# #先转换为时间数组,然后转换为其他格式
# timeStruct = time.strptime(t, "%Y-%m-%d %H:%M:%S")
# strTime = time.strftime("%Y/%m/%d %H:%M:%S", timeStruct)
# print(strTime)
#


# timeStamp = 15349194090
# localTime = time.localtime(timeStamp)
# strTime = time.strftime("%Y-%m-%d %H:%M:%S", localTime)
# print(strTime)


driver = webdriver.Firefox()
driver.get('http://11.11.164.134:9081/rmms/modules/ep.rmms.portal/login/login.jsp')
time.sleep(4)
driver.find_element_by_id('username').send_keys('rmln')
driver.find_element_by_id('password').send_keys('qwert1234!@#$')
driver.find_element_by_id('loginSubmitButton').click()
time.sleep(4)
# # menu_list = ['权限管理','会员档案','积分消费查询']
driver.find_element_by_link_text('积分消费查询').click()
driver.find_element_by_link_text('积分查询').click()
time.sleep(4)

#driver.find_element_by_xpath("//*[@id='_pagef_0000000080gasStationName']/div[2]/a").click()
search = driver.find_element_by_xpath("//*[@class = 'u-form-textbox-icon u-form-textbox-icon-normal u-a-common icon-choose']")
ActionChains(driver).move_to_element(search).perform()
search.click()
time.sleep(3)
#'/html/body/section/section/section/section[2]/section/section/div/div/div[2]/div/div/div/div/div[3]/div[1]/div[1]/div[2]/div/div/form/table/tbody/tr[1]/td[6]/div[1]/div[2]/a'
text_driver = driver.find_element_by_xpath('//*[@class="u-xdlg-mt"]')
text = text_driver.text
print(text)
#driver.switch_to.frame('dlg_0filterForm')
#driver.find_element_by_xpath("//*[@id='dlg_0condition_unieap_input']").send_keys('EAEK')
time.sleep(3)
#driver.find_element_by_css_selector('#dlg_0condition_unieap_input').send_keys('EAEK')
# a=driver.find_element_by_xpath("//button[@id='dlg_0unieap_form_Button_4_unieap_input']")
# text = a.text
# print(text)
# a.click()
ele1 = driver.find_elements_by_xpath("//div[@class='u-xgrid-cell']")
for text in ele1:
    print(text.text)

time.sleep(4)
ele2 = driver.find_elements_by_xpath("//span[@class='node-label']")
for text in ele2:
    print(text.text)
js = 'window.scrollTo(0,10)'
driver.execute_script(js)
#driver.switch_to.parent_frame()
# element = driver.find_elements_by_xpath("//*[@class='u-titlepane-titlenode']")
# for ele in element:
#     print(ele.text)
# js = "$('input[id=_pagef_0000000080startPayTime_unieap_input]').attr('readonly','')"
# driver.execute_script(js)
#driver.find_element_by_id('_pagef_0000000080startPayTime_unieap_input').send_keys('2018-08-24 13:47:05')
# driver.find_element_by_link_text('查询').click()
# close = driver.find_element_by_id('unieap_form_Button_4_unieap_input')
# print(close.text)
# close.click()
# time.sleep(3)
# driver.find_element_by_class_name('/html/body/section/section/section/section[2]/section/section/div/div/div[2]/div/div/div/div/div[3]/div[1]/div[1]/div[2]/div/div/form/table/tbody/tr[1]/td[6]/div[1]/div[2]/a').click()
# 'u-titlepane-titlenode'
# 'u-titlepane-titlenode'
# for i in range(1,7):
#     driver.find_element_by_id('').send_keys('')
#     driver.find_element_by_link_text('查询')
#     flag = Isnot_element_exist(driver, '//*[@class="u-xdlg"]')
#     if flag:
#         unittest.TestCase.assertTrue(flag,'这个输入项非必填项')


# txt = driver.find_element_by_link_text('查询').click()
# print(txt)
# try:
#     driver.find_elements_by_xpath('//*[@class="u-xdlg-mtc"]')
#     print('存在输入框')
# except exceptions.NoSuchElementException :
#     print("不存在输入框")
