# ----------------------------------
'''                                                           
代码说明：base page
编写日期：2018.08.13
设计  者：linux超
'''


# ----------------------------------
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Base_Page(object):
    def __init__(self, driver):
        self.driver = driver

    def find_ele_by_id(self, id=''):
        return self.driver.find_element_by_id(id)

    def find_ele_by_class_name(self, cls=''):
        return self.driver.find_element_by_class_name(cls)

    def find_ele_by_xpath(self, xpath=''):
        return self.driver.find_element_by_xpath(xpath)

    def find_ele_by_link_text(self, linktext=''):
        return self.driver.find_element_by_link_text(linktext)

    # *loc 代表任意数量的位置参数
    def find_element(self,*loc):
        try:
            element = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(*loc))
            return element
        except:
            print('%s 页面找不到元素 %s'%(self,loc))

    def script(self,src):
        self.driver.excute_script(src)

if __name__ == '__main__':
    pass
