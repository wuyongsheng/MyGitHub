'''
Code description： string handle
Create time：
Developer：
'''

import logging
from retail.test_case.models.log import Logger

log = Logger(__name__, CmdLevel=logging.INFO, FileLevel=logging.INFO)
def strhandle(str):
    """

    :param str:
    :return:
    """
    #初始化字符、数字、空格、特殊字符的计数
    try:
        lowerCase = 0
        upperCase = 0
        number = 0
        other = 0
        for stritem in str:
         #如果在字符串中有小写字母，那么小写字母的数量+1
            if stritem.islower():
                lowerCase += 1
            #如果在字符串中有数字，那么数字的数量+1
            elif stritem.isdigit():
                number += 1
            elif stritem.isupper():# 大写字母
                upperCase +=1
            #如果在字符串中有空格，那么空格的数量+1
            else:
                other += 1
        return lowerCase, upperCase, number, other
    except Exception as e:
        log.logger.exception('string handle error , please check!', exc_info=True)
        raise e


if __name__=='__main__':
    list = ['qwert','erwer']
    lowercase, uppercase, number, other = strhandle(list[0])
    print ("该字符串中的小写字母有：%d" %lowercase)
    print ("该字符串中的大写写字母有：%d" %uppercase)
    print ("该字符串中的数字有：%d" %number)
    print ("该字符串中的特殊字符有：%d" %other)