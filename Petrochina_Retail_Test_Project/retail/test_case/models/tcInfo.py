'''
Code description：test case info
Create time：
Developer：
'''

class TcInfo(object):

    def __init__(self,
                 id='',
                 name='',
                 owner='',
                 result='',
                 startTime='',
                 endTime='',
                 duration='',
                 errorInfo=''):
        """

        :param id:
        :param name:
        :param owner:
        :param result:
        :param starttime:
        :param endtime:
        :param duration:
        :param errorinfo:
        """
        self.id = id
        self.name = name
        self.owner = owner
        self.result = result
        self.starttime = startTime
        self.endtime = endTime
        self.duration = duration
        self.errinfo = errorInfo

