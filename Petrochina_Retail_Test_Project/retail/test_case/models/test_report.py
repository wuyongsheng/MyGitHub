#----------------------------------
'''                                                           
代码说明：生成测试报告
编写日期：
设计  者：
'''
#----------------------------------
import HTMLTestRunner
import time
from retail.config import globalconfig

def Test_Report():
    currTime = time.strftime('%Y-%m-%d %H_%M_%S')

    filename = globalconfig.report_path+r'\report'+currTime+'.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner\
        (stream=fp, title='Retail sys测试报告',
                                           description='处理器:Intel(R) Core(TM) '
                                                       'i5-6200U CPU @ 2030GHz 2.40 GHz '
                                            '内存:8G 系统类型: 64位 版本: windows 10 家庭中文版')
    return runner, fp, filename
if __name__ == '__main__':
    Test_Report()