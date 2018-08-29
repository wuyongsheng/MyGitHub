#----------------------------------
'''                                                           
代码说明：判断一个元素是否存在
编写日期：2018.08.15
设计  者：linux超
'''
#----------------------------------
from selenium import webdriver
from selenium.common import exceptions

def Is_Element_Exist(driver, element_list):
    try:
        driver.find_element_by_xpath(element_list)
        return True
    except exceptions.NoSuchElementException:
        driver.find_element_by_id(element_list)
        return True
    except:
        return False

def Isnot_element_exist(driver, element):
    try:
        driver.find_element_by_xpath(element)
        return True
    except exceptions.NoSuchElementException as e:
        print(e)
        return False





if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.get('http://11.11.164.134:9081/rmms/modules/ep.rmms.portal/login/login.jsp')
    element_list = ['/html/body/div[1]/div[2]/table/tbody/tr[1]/td[1]/div','password']
    for element in range(len(element_list)):
        if Is_Element_Exist(driver,element_list[element]):
            print('存在')
        else:
            print('不存在')