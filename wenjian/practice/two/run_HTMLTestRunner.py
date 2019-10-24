import unittest
import HTMLTestRunner
# from practice.one.run_test_HTMLTestRunner import SuiteTestCalc,SuiteTestPow
from practice.two.TestSuite import SuiteTestcase





class RunTest(object):
    def test_run(self):
        filename = r"C:\software\Pycharm\PyCharm Community Edition 2019.1.3\wenjian\practice\two\t.html"
        with open(filename, 'wb') as fp:
            runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Report_title', description='Report_description')
            my_test_suite = unittest.TestSuite()
            my_test_suite.addTests([
                unittest.defaultTestLoader.loadTestsFromTestCase(SuiteTestcase)])
            # my_test_suite.addTest(SuiteTestcase("test_screenshot"))
            # my_test_suite.addTest(SuiteTestcase("test03_SogouScreenShot_data"))
            runner.run(my_test_suite)

if __name__ == '__main__':
    # unittest.main()
    RunTest().test_run()
