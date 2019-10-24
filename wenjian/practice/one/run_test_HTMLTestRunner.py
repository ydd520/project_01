import HTMLTestRunner
import unittest
import math

class Calc(object):
    def add(self,x,y,*d):
        result = x + y
        for i in d:
            result += i
        return result

    def sub(self,x,y,*d):
        result = x - y
        for i in d:
            result -= i
        return result

class SuiteTestCalc(unittest.TestCase):
    def setUp(self):
        self.c = Calc()

    @unittest.skip("skipping")
    def test_Sub(self):
        print('sub')
        self.assertEqual(self.c.sub(100,34,6),60,'求差错误！')
    def testAdd(self):
        print('add')
        self.assertEqual(self.c.add(1,32,56),89,'求和错误！')

class SuiteTestPow(unittest.TestCase):
    def setUp(self):
        self.seq = range(10)
    def test_Pow(self):
        print('Pow')
        self.assertEqual(pow(6,3),216,'求幂结果错误!')


# class RunTest:
#
#     def run_test(self):
#         suite1 = unittest.TestLoader().loadTestsFromTestCase(SuiteTestCalc)
#         suite2 = unittest.TestLoader().loadTestsFromTestCase(SuiteTestPow)
#         suite = unittest.TestSuite([suite1, suite2])
#         filename = r"C:\tt\t.html"
#         # fp = open(filename,'wb')
#         # runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Report_title', description='Report_description')
#         # runner.run(suite)
#         with open(filename, 'wb') as fp:
#             runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Report_title', description='Report_description')
#             runner.run(suite)



# if __name__ == '__main__':
#     RunTest().run_test()
#     # suite1 =unittest.TestLoader().loadTestsFromTestCase(SuiteTestCalc)
#     # suite2 = unittest.TestLoader().loadTestsFromTestCase(SuiteTestPow)
#     # suite = unittest.TestSuite([suite1,suite2])
#     # filename = r"C:\tt\t.html"
#     # # fp = open(filename,'wb')
#     # # runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Report_title', description='Report_description')
#     # # runner.run(suite)
#     # with open(filename, 'wb') as fp:
#     #     runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Report_title',description='Report_description')
#     #     runner.run(suite)
#     run_test()














