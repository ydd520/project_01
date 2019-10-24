# -*- coding: utf-8 -*-
from selenium import webdriver
import time,os
from practice.two.FileUtil import creareDir
import traceback
from practice.one.Log import Log
from practice.two.testdata import data

class TestCase(object):
    url = 'http://www.sogou.com'
    print(u"打开浏览器")
    driver = webdriver.Firefox(executable_path='C:\Python3.6\Python36\driver\geckodriver.exe')
    picDir = creareDir()
    # def __init__(self):
    #     self.url = 'http://www.sogou.com'
    #     print(u"打开浏览器")
    #     self.driver = webdriver.Firefox(executable_path= 'C:\Python3.6\Python36\driver\geckodriver.exe')
    #     self.picDir = creareDir()

    def tackScreenShot(driver,savePath,picName):

        picPath = os.path.join(savePath, str(picName)+ ".png")
        try:
            print(u'########开始截屏#############')
            print(u'########截屏路径为%s#############' %picPath)
            driver.get_screenshot_as_file(picPath)
        except Exception as e:
            print(traceback.print_exc())

    def SogouScreenShot_ddt(self,testdata,expectdata):
        print(u'进入case########SogouScreenShot#############')
        TestCase.driver.get(TestCase.url)
        try:
            TestCase.driver.find_element_by_id('query').send_keys(testdata)
            TestCase.driver.find_element_by_id('stb').click()
            time.sleep(3)
            assert u'事在人为' in TestCase.driver.page_source,expectdata
        except AssertionError as e:
            TestCase.tackScreenShot(TestCase.driver, TestCase.picDir, e)
        except Exception as e:
            print(traceback.print_exc())
            TestCase.tackScreenShot(TestCase.driver, TestCase.picDir, e)
        print(TestCase.picDir)

    @data(path='data.json', pathName='test')
    def SogouScreenShot_data(testdata):
        print(u'进入case########SogouScreenShot#############')
        TestCase.driver.get(TestCase.url)
        try:
            TestCase.driver.find_element_by_id('query').send_keys(testdata['csdn'])
            TestCase.driver.find_element_by_id('stb').click()
            time.sleep(3)
            assert u'事在人为' in TestCase.driver.page_source,testdata['expect']
        except AssertionError as e:
            TestCase.tackScreenShot(TestCase.driver, TestCase.picDir, e)
        except Exception as e:
            print(traceback.print_exc())
            TestCase.tackScreenShot(TestCase.driver, TestCase.picDir, e)
        print(TestCase.picDir)

    # def Screenshot(self):
    #     print(u'进入case########Screenshot#############')
    #     TestCase.driver.get(TestCase.url)
    #     try:
    #         result = TestCase.driver.get_screenshot_as_file(r"C:\test\screenPicture.png")
    #         time.sleep(3)
    #         print(result)
    #     except IOError as e:
    #         print(e)

    def Screenshot(self):
        print(u'进入case########Screenshot#############')
        TestCase.driver.get(TestCase.url)
        try:
            # result = TestCase.driver.get_screenshot_as_file(r"C:\test\screenPicture.png")
            TestCase.tackScreenShot(TestCase.driver, TestCase.picDir, 'Screenshot')
            time.sleep(3)
            # print(result)
        except IOError as e:
            print(e)

    def quit(self):
        print(u'########退出浏览器#############')
        TestCase.driver.quit()