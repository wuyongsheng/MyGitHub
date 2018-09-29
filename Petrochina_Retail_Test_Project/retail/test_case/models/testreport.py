'''
Code description：test report
Create time：
Developer：
'''


import time
import logging
import unittest
from BeautifulReport import BeautifulReport
import HTMLTestRunner
from retail.config import conf
from retail.test_case.models.log import Logger

log = Logger(__name__, CmdLevel=logging.INFO, FileLevel=logging.INFO)
# 用HTMLTestRunner 实现的测试报告
def testreport():
    """

    :return:
    """
    currTime = time.strftime('%Y-%m-%d %H_%M_%S')
    fileName = conf.reportPath + r'\report' + currTime + '.html'
    try:
        fp = open(fileName, 'wb')
    except Exception :
        log.logger.exception('[%s] open error cause Failed to generate test report' %fileName)
    else:
        runner = HTMLTestRunner.HTMLTestRunner\
            (stream=fp, title='Retail sys测试报告',
                                               description='处理器:Intel(R) Core(TM) '
                                                           'i5-6200U CPU @ 2030GHz 2.40 GHz '
                                                '内存:8G 系统类型: 64位 版本: windows 10 家庭中文版')
        log.logger.info('successed to generate test report [%s]' %fileName)
        return runner, fp, fileName
#
def addTc(TCpath = conf.tcPath, rule = '*TC.py'):
    """

    :param TCpath: 测试用例存放路径
    :param rule: 匹配的测试用例文件
    :return:  测试套件
    """
    discover = unittest.defaultTestLoader.discover(TCpath, rule)

    return discover
# 用BeautifulReport模块实现测试报告
def runTc(discover):
    """

    :param discover: 测试套件
    :return:
    """
    currTime = time.strftime('%Y-%m-%d %H_%M_%S')
    fileName = currTime+'.html'
    try:
        result = BeautifulReport(discover)
        result.report(filename=fileName, description='测试报告', log_path=conf.reportPath)
    except Exception:
        log.logger.exception('Failed to generate test report', exc_info=True)
    else:
        log.logger.info('successed to generate test report [%s]' % fileName)
        return fileName

if __name__ == '__main__':
    testreport()
    suite = addTc(rule = '*TC.py')
    runTc(suite)
