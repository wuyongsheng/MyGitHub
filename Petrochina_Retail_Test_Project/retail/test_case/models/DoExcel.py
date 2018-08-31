#! user/bin/python
#----------------------------------
'''                                                           
代码说明： 读excel文件
编写日期：
设计  者：
'''
#----------------------------------
import xlrd
import os
from retail.config import globalconfig

class ReadExcel(object):

    def __init__(self,filename,sheetname):
        datafile = os.path.join(globalconfig.data_path,filename)
        self.workbook = xlrd.open_workbook(datafile)
        self.sheetname = self.workbook.sheet_by_name(sheetname)

    def read_excel(self,rownum,colnum):
        value = self.sheetname.cell(rownum,colnum).value
        return value

if __name__ == '__main__':
    cellvalue = ReadExcel('Data.xlsx','Sheet1').read_excel(1,0)
    print(int(cellvalue))