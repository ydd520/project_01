#encoding = utf -8
from practice.two.DateUtil import currentDate,currentTime
import os

'''
创建目录
存放异常截图
'''


def creareDir():
    #获取当前文件所在的文件路劲
    currentPath = os.path.dirname(os.path.abspath(__file__))
    #路劲和文件名拼接
    dateDir = os.path.join(currentPath,currentDate())
    # print(dateDir)
    if not os.path.exists(dateDir):
        os.mkdir(dateDir)
    timeDir = os.path.join(dateDir,currentTime())
    if not os.path.exists(timeDir):
        os.mkdir(timeDir)
    return timeDir


if __name__ == '__main__':
    creareDir()


































