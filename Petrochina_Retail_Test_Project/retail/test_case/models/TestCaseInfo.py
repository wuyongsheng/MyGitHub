#! user/bin/python
#----------------------------------
'''                                                           
代码说明：
编写日期：
设计  者：
'''
#----------------------------------
class TestCaseInfo(object):

    def __init__(self,id,name,owner,result,starttime,endtime,duration,errorinfo):
        self.id = id
        self.name = name
        self.owner = owner
        self.result = result
        self.starttime = starttime
        self.endtime = endtime
        self.duration = duration
        self.errinfo = errorinfo

