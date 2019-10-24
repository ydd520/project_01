# -*- coding: utf-8 -*-
import unittest,time
import ddt
from practice.two.TestCase import TestCase
from practice.one.Log import Log

@ddt.ddt
class SuiteTestcase(unittest.TestCase):
    a = 1
    @classmethod
    def setUpClass(cls):
        #创建TestCase类的对象
        cls.t = TestCase()

    # @unittest.skip('skipping')
    def test01_screenshot(self):
        print('#########start######### test_screenshot')
        SuiteTestcase.t.Screenshot()

    @ddt.file_data("test_data_list.json")
    def test02_SogouScreenShot_ddt(self,value):
        print('#########start######### test_SogouScreenShot')
        testdata, expectdata = tuple(value.strip().split(","))
        print(testdata,expectdata)
        print(value)
        SuiteTestcase.t.SogouScreenShot_ddt(testdata,expectdata)

    def test03_SogouScreenShot_data(self):
        print('#########start######### test_SogouScreenShot')
        SuiteTestcase.t.SogouScreenShot_data()

    @classmethod
    def tearDownClass(cls):
        SuiteTestcase.t.quit()

# if __name__=='__main__':
#     suite = unittest.TestSuite()
#     suite.addTest(SuiteTestcase("test_screenshot"))
#     # suite.addTest(SuiteTestcase("test_SogouScreenShot"))
#     runner = unittest.TextTestRunner()
#     runner.run(suite)

