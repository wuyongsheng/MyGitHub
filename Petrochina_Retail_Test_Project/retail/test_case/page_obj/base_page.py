# ----------------------------------
'''                                                           
代码说明：base page
编写日期：2018.08.13
设计  者：linux超
'''


# ----------------------------------
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import exceptions

class Base_Page(object):
    def __init__(self, driver,url='http://11.11.164.134:9081/rmms/modules/ep.rmms.portal/login/login.jsp'):

        self.driver = driver
        self.base_url = url

    def find_ele_by_id(self, id=''):
        return self.driver.find_element_by_id(id)

    def find_ele_by_class_name(self, cls=''):
        return self.driver.find_element_by_class_name(cls)

    def find_ele_by_xpath(self, xpath=''):
        return self.driver.find_element_by_xpath(xpath)

    def find_ele_by_link_text(self, linktext=''):
        return self.driver.find_element_by_link_text(linktext)

    def _open(self,url):
        self.driver.get(url)
        self.driver.implicitly_wait(10)

    def open(self):
        try:
            self._open(self.base_url)
            return self.base_url
        except Exception:
            raise ValueError("url load failed ",self.base_url)

    # *loc 代表任意数量的位置参数
    def find_element_re(self, *loc):
        try:
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
        except:
            #print('%s 页面找不到元素 %s'%(self,loc))
            raise ValueError('%s 页面找不到元素 %s'%(self,loc))
    # 执行js脚本
    def script(self,src):
        self.driver.excute_script(src)

    # 判断元素是否存在
    def Isnot_element_exist(self, *element):
        try:
            self.find_element_re(*element)
            return True
        except exceptions.NoSuchElementException :
            return False

if __name__ == '__main__':
    pass
