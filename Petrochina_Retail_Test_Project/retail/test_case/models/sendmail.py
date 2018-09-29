'''
Code description：send email
Create time：
Developer：
'''

import smtplib
from email.mime.text import MIMEText
from email.header import Header
import os
from retail.config import conf
from retail.test_case.models.log import Logger

log = Logger(__name__)
#   邮件发送接口
class SendMail(object):
    '''
    邮件配置信息
    '''
    def __init__(self,
                 receiver,
                 subject='Retail 系统测试报告',
                 server='smtp.qq.com',
                 fromuser='281754043@qq.com',
                 frompassword='gifhhsbgqyovbhhc',
                 sender='281754043@qq.com'):
        """

        :param receiver:
        :param subject:
        :param server:
        :param fromuser:
        :param frompassword:
        :param sender:
        """

        self._server = server
        self._fromuser = fromuser
        self._frompassword = frompassword
        self._sender = sender
        self._receiver = receiver
        self._subject = subject

    def sendEmail(self, fileName):
        """

        :param filename:
        :return:
        """
        #   打开报告文件读取文件内容
        try:
            f = open(os.path.join(conf.reportPath, fileName), 'rb')
            fileMsg = f.read()
        except Exception:
            log.logger.exception('open or read file [%s] failed,No such file or directory: %s' %(fileName, conf.reportPath))
            log.logger.info('open and read file [%s] successed!' %fileName)
        else:
            f.close()
            #   邮件主题
            subject = 'Python test report' #
            #   邮件设置
            msg = MIMEText(fileMsg, 'html', 'utf-8')
            msg['subject'] = Header(subject, 'utf-8')
            msg['from'] = self._sender
        #   连接服务器，登录服务器，发送邮件
            try:
                smtp = smtplib.SMTP()
                smtp.connect(self._server)
                smtp.login(self._fromuser, self._frompassword)
            except Exception:
                log.logger.exception('connect [%s] server failed or username and password incorrect!' %smtp)
            else:
                log.logger.info('email server [%s] login success!' %smtp)
                try:
                    smtp.sendmail(self._sender, self._receiver, msg.as_string())
                except Exception:
                    log.logger.exception('send email failed!')
                else:
                    log.logger.info('send email successed!')


#   从文件中读取邮件接收人信息
def getReceiverInfo(fileName):
    '''
    :param filename: 读取接收邮件人信息
    :return: 接收邮件人信息
    '''
    try:
        openFile = open(os.path.join(conf.dataPath, fileName))
    except Exception:
        log.logger.exception('open or read file [%s] failed,No such file or directory: %s' %(fileName, conf.dataPath))
    else:
        log.logger.info('open file [%s] successed!' %fileName)
        for line in openFile:
            msg = [i.strip() for i in line.split(',')]
            log.logger.info('reading [%s] and got receiver value is [%s]' %(fileName, msg))
            return msg

if __name__ == '__main__':
    readMsg=getReceiverInfo('mail_receiver.txt')
    sendmail = SendMail(readMsg)
    sendmail.sendEmail('2018-09-21 17_44_04.html')
