#! user/bin/python
# ----------------------------------
'''                                                           
代码说明： 日志
编写日期：
设计  者：
'''
# ----------------------------------
import logging
import os
import time
from retail.config import globalconfig

class Logger(object):
    def __init__(self, logger, CmdLevel, FileLevel):
        """

        :param logger:
        :param CmdLevel:
        :param FileLevel:
        """
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)  # 设置日志输出的默认级别

        fmt = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')  # 日志输出格式
        #self.LogFileName = os.path.join("{0}.log".format(time.strftime("%Y-%m-%d")))  # 日志文件名称
        self.LogFileName = os.path.join(globalconfig.log_path, "{0}.log".format(time.strftime("%Y-%m-%d")))

        # 设置控制台输出
        sh = logging.StreamHandler()
        sh.setFormatter(fmt)
        sh.setLevel(CmdLevel)# 日志级别

        # 设置文件输出
        fh = logging.FileHandler(self.LogFileName)
        fh.setFormatter(fmt)
        fh.setLevel(FileLevel)# 日志级别

        self.logger.addHandler(sh)
        self.logger.addHandler(fh)

    def debug(self, message):
        self.logger.debug(message)

    def info(self,message):
        self.logger.info(message)

    def war(self,message):
        self.logger.warning(message)

    def err(self,message):
        self.logger.error(message)

    def cri(self,message):
        self.logger.critical(message)

if __name__ == '__main__':
    logger = Logger("fox",CmdLevel=logging.DEBUG, FileLevel=logging.DEBUG)
    logger.debug("debug")
