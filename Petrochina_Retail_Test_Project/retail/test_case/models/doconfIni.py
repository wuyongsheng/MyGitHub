'''
Code description：read conf file
Create time：
Developer：
'''

import logging
import configparser
from retail.config.conf import *
from retail.test_case.models.log import Logger

log = Logger(__name__, CmdLevel=logging.INFO, FileLevel=logging.INFO)
class DoConfIni(object):

    def __init__(self):
        """

        :param filename:
        """
        self.cf = configparser.ConfigParser()

    def getConfValue(self,filename,section,name):
        """

        :param config:
        :param name:
        :return:
        """
        try:
            self.cf.read(filename)
            value = self.cf.get(section,name)
        except Exception as e:
            log.logger.exception('read file [%s] for [%s] failed , did not get the value' %(filename,section))
            raise e
        else:
            log.logger.info('read excel value [%s] successed! ' %value)
            return value

    def writeConfValue(self,filename, section, name, value):
        """

        :param section: section
        :param name: value name
        :param value:  value
        :return: none
        """
        try:
            self.cf.add_section(section)
            self.cf.set(section, name, value)
            self.cf.write(open(filename, 'w'))
        except Exception :
            log.logger.exception('section %s has been exist!' %section)
            raise configparser.DuplicateSectionError(section)
        else:
            log.logger.info('write section'+section+'with value '+value+' successed!')

if __name__ == '__main__':
    file_path = currPath
    print(file_path)
    read_config = DoConfIni()

    value = read_config.getConfValue(os.path.join(currPath,'config.ini'),'project','project_path')
    print(value)

    read_config.writeConfValue(os.path.join(currPath,'config.ini'),'tesesection', 'name', 'hello word')
