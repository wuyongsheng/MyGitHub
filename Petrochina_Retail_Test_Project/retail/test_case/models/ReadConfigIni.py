#! user/bin/python
#----------------------------------
'''                                                           
代码说明：读ini配置文件
编写日期：
设计  者：
'''
#----------------------------------
import configparser
import os
from retail.config import globalconfig

class ReadConfigIni(object):

    def __init__(self,filename):
        self.cf = configparser.ConfigParser()
        self.cf.read(filename)

    def getConfigValue(self,config,name):
        value = self.cf.get(config,name)
        return value

if __name__ == '__main__':
    #fil_path = os.path.split(os.path.realpath(__file__))[0]
    file_path = globalconfig.curr_path
    print(file_path)
    read_config = ReadConfigIni(os.path.join(file_path,'config.ini'))
    value = read_config.getConfigValue('project','project_path')
    print(value)