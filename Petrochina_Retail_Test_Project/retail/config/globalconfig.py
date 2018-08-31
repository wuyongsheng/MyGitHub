#! user/bin/python
#----------------------------------
'''                                                           
代码说明：获取文件路径
编写日期：
设计  者：
'''
#----------------------------------
from retail.test_case.models.ReadConfigIni import ReadConfigIni
import os
# 获取当前路径
curr_path= \
    os.path.split(os.path.realpath(__file__))[0]

# 读配置文件获取项目路径
read_config = \
    ReadConfigIni(os.path.join(curr_path,'config.ini'))
project_path = \
    read_config.getConfigValue('project','project_path')

# 获取日志路径
log_path= \
    os.path.join(project_path,'retail','report','Log')

# 测试用例路径
testcase_path = \
    os.path.join(project_path,'retail','test_case')

# 获取报告路径
report_path= \
    os.path.join(project_path,'retail','report','TestReport')

# 获取测试数据路径
data_path= \
    os.path.join(project_path,'retail','data','TestData')
