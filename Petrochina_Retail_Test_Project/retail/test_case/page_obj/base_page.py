'''
Code description： base page 封装一些公共方法
Create time：
Developer：
'''
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os
import logging
import sys
from retail.test_case.models.log import Logger
from retail.config import conf
from retail.test_case.models.doexcel import ReadExcel

eleData = ReadExcel() # 存储系统所有的元素数据
testLoginData = ReadExcel('elementDate.xlsx', 'userNamePw') # 登录模块测试数据
modifyPwData = ReadExcel('elementDate.xlsx', 'modifyPw') # 修改密码模块测试数据
queryData = ReadExcel('elementDate.xlsx', 'queryData')
log = Logger(__name__, CmdLevel=logging.INFO, FileLevel=logging.INFO)

class BasePage(object):

    """主菜单"""
    menuList = \
        [(By.LINK_TEXT, eleData.readExcel(7, 3)), # 权限管理
        (By.LINK_TEXT, eleData.readExcel(8, 3)), # 会员档案
        (By.LINK_TEXT, eleData.readExcel(9, 3)), # 积分消费查询
        (By.LINK_TEXT, eleData.readExcel(10, 3)), # 功能演示
        (By.LINK_TEXT, eleData.readExcel(11, 3)), # 待办工作
        (By.LINK_TEXT, eleData.readExcel(12, 3)), # 报表
        (By.LINK_TEXT, eleData.readExcel(13, 3)), # 积分规则/活动查询
        (By.LINK_TEXT, eleData.readExcel(14, 3))] # 积分规则/活动申请

    def __init__(self, driver,url='http://11.11.164.134:9081/rmms/modules/ep.rmms.portal/login/login.jsp'):
        """

        :param driver:
        :param url:
        """
        self.driver = driver
        self.base_url = url
    def _open(self,url):
        """

        :param url:
        :return:
        """
        try:
            self.driver.get(url)
            self.driver.implicitly_wait(10)
        except Exception as e:
            log.logger.exception(e, exc_info=True)
            raise ValueError('%s address access error, please check！' %url)
        else:
            log.logger.info('%s is accessing address %s at line[46]' %(sys._getframe().f_code.co_name,url))

    def open(self):
        """

        :return:
        """

        self._open(self.base_url)
        log.logger.info('%s loading successed!' %self.base_url)
        return self.base_url

    # *loc 代表任意数量的位置参数
    def findElement(self, *loc):
        """
        查找单一元素
        :param loc:
        :return:
        """
        try:
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(loc))
            # log.logger.info('The page of %s had already find the element %s'%(self,loc))
            # return self.driver.find_element(*loc)
        except Exception as e:
            log.logger.exception('finding element timeout!, details' ,exc_info=True)
            raise e
        else:
            log.logger.info('The page of %s had already find the element %s' % (self, loc))
            return self.driver.find_element(*loc)

    def findElements(self, *loc):
        """
        查找一组元素
        :param loc:
        :return:
        """
        try:
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(loc))
            # log.logger.info('The page of %s had already find the element %s' % (self, loc))
            # return self.driver.find_elements(*loc)
        except Exception as e:
            log.logger.exception('finding element timeout!, details', exc_info=True)
            raise e
        else:
            log.logger.info('The page of %s had already find the element %s' % (self, loc))
            return self.driver.find_elements(*loc)

    def inputValue(self, inputBox, value):
        """
        后期修改其他页面直接调用这个函数
        :param inputBox:
        :param value:
        :return:
        """
        inputB = self.findElement(*inputBox)
        try:
            inputB.clear()
            inputB.send_keys(value)
        except Exception as e:
            log.logger.exception('typing value error!', exc_info=True)
            raise e
        else:
            log.logger.info('inputValue:[%s] is receiveing value [%s]' % (inputBox, value))

    # 获取元素数据
    def getValue(self, *loc):
        """

        :param loc:
        :return:
        """
        element = self.findElement(*loc)
        try:
            value = element.text
            #return value
        except Exception:
            #element = self.find_element_re(*loc) # 2018.09.21 for log
            value = element.get_attribute('value')
            log.logger.info('reading the element [%s] value [%s]' % (loc, value))
            return value
        except:
            log.logger.exception('read value failed', exc_info=True)
            raise Exception
        else:
            log.logger.info('reading the element [%s] value [%s]' % (loc,value))
            return value

    def getValues(self, *loc):
        """

        :param loc:
        :return:
        """
        value_list = []
        try:
            for element in self.findElements(*loc):
                value = element.text
                value_list.append(value)
        except Exception as e:
            log.logger.exception('read value failed', exc_info=True)
            raise e
        else:
            log.logger.info('reading the element [%s] value [%s]'% (loc,value_list))
            return value_list

    # 执行js脚本
    def jScript(self,src):
        """

        :param src:
        :return:
        """
        try:
            self.driver.excute_script(src)
        except Exception as e:
            log.logger.exception('execute js script [%s] failed ' %src)
            raise e
        else:
            log.logger.info('execute js script [%s] successed ' %src)


    # 判断元素是否存在
    def isElementExist(self, element):
        """

        :param element:
        :return:
        """
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(element))
        except:
            # log.logger.exception('The element [%s] not exist', exc_info=True)
            return False
        else:
            # log.logger.info('The element [%s] have existed!' %element)
            return True
    # 截图
    def saveScreenShot(self, filename):
        """

        :param filename:
        :return:
        """
        list_value = []

        list = filename.split('.')
        for value in list:
            list_value.append(value)
        if list_value[1] == 'png' or list_value[1] == 'jpg' or list_value[1] == 'PNG' or list_value[1] == 'JPG':
            if 'fail' in list_value[0].split('_'):
                try:
                    self.driver.save_screenshot(os.path.join(conf.failImagePath, filename))
                except Exception:
                    log.logger.exception('save screenshot failed !', exc_info=True)
                else:
                    log.logger.info('the file [%s]  save screenshot successed under [%s]' % (filename, conf.failImagePath))
            elif 'pass' in list_value[0]:
                try:
                    self.driver.save_screenshot(os.path.join(conf.passImagePath, filename))
                except Exception:
                    log.logger.exception('save screenshot failed !', exc_info=True)
                else:
                    log.logger.info(
                        'the file [%s]  save screenshot successed under [%s]' % (filename, conf.passImagePath))
            else:
                log.logger.info('save screenshot failed due to [%s] format incorrect' %filename)
        else:
            log.logger.info('the file name of [%s] format incorrect cause save screenshot failed, please check!' % filename)

    # 接受错误提示框
    def accept(self, *loc):
        """

        :return:
        """
        self.findElement(*loc).click()
        log.logger.info('closed the error information fram successed!')

if __name__ == '__main__':
    pass
