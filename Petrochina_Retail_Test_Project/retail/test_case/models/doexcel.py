'''
Code description：read excel.xlsx, get values
Create time：
Developer：
'''

import xlrd
import os
import logging
from retail.config import conf
from retail.test_case.models.log import Logger

log = Logger(__name__, CmdLevel=logging.INFO, FileLevel=logging.INFO)

class ReadExcel(object):

    def __init__(self,fileName='elementDate.xlsx',sheetName='elementsInfo'):
        """

        :param fileName:
        :param sheetName:
        """
        try:
            self.dataFile = os.path.join(conf.dataPath, fileName)
            self.workBook = xlrd.open_workbook(self.dataFile)
            self.sheetName = self.workBook.sheet_by_name(sheetName)
        except Exception:
            log.logger.exception('init class ReadExcel fail', exc_info=True)
            raise
        else:
            log.logger.info('initing class ReadExcel')

    def readExcel(self,rownum,colnum):
        """

        :param rownum:
        :param colnum:
        :return:
        """
        try:
            value = self.sheetName.cell(rownum,colnum).value
        except Exception:
            log.logger.exception('read value from excel file fail', exc_info=True)
            raise
        else:
            log.logger.info('reading value [%s] from excel file [%s] completed' %(value, self.dataFile))
            return value

if __name__ == '__main__':
    cellValue = ReadExcel().readExcel(1,3)
    print((cellValue))