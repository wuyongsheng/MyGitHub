'''
代码说明：通过邮件发送测试报告
编写日期：2018.07.17
设置者：linux超
'''

import smtplib
from email.mime.text import MIMEText
from email.header import Header

#   邮件发送接口
class send_mail_init_info(object):
    '''
    邮件配置信息
    '''
    def __init__(self, receiver, subject='Retail 系统测试报告', server='smtp.qq.com',
                 fromuser='281754043@qq.com', frompassword='gifhhsbgqyovbhhc',
                 sender='281754043@qq.com'):
        self._server = server
        self._fromuser = fromuser
        self._frompassword = frompassword
        self._sender = sender
        self._receiver = receiver
        self._subject = subject

    def send_email(self, filename):
        #   打开报告文件读取文件内容
        f = open(filename, 'rb')
        file_msg = f.read()
        f.close()

        #   邮件主题
        subject = 'Python test report' #+ filename
        #   邮件设置
        msg = MIMEText(file_msg, 'html', 'utf-8')
        msg['subject'] = Header(subject, 'utf-8')
        msg['from'] = self._sender
        #   连接服务器，登录服务器，发送邮件
        smtp = smtplib.SMTP()
        smtp.connect(self._server)
        smtp.login(self._fromuser, self._sender)
        try:
            smtp.sendmail(self._sender, self._receiver, msg.as_string())
        except Exception as e:
            print('send failed', e)
        else:
            print('send success！')

        smtp.quit()

#   从文件中读取邮件接收人信息
def read_SendToUserinfo_file(filename):
    '''
    :param filename: 读取接收邮件人信息
    :return: 接收邮件人信息
    '''
    open_file = open(filename)
    for line in open_file:
        msg = [i.strip() for i in line.split(',')]
        print(msg)
        return msg

if __name__ == '__main__':
    read_msg=read_SendToUserinfo_file(r'D:\Petrochina_Retail_Test_Project\retail\data\mail_receiver.txt')
    sendmail = send_mail_init_info(read_msg, 'smtp.qq.com', '281754043@qq.com', 'gifhhsbgqyovbhhc', '281754043@qq.com')
    sendmail.send_email(r'D:\Petrochina_Retail_Test_Project\retail\report\report2018-08-15 08_38_45.html')
