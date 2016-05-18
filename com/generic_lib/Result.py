
# import unittest
# class TestResultX(unittest.TestResult):
#     def startTest(self, test):
#         print('# blip')
#         unittest.TestResult.startTest(self, test)
#
#     def stopTest(self, test):
#         print('# blop')
#         unittest.TestResult.stopTest(self, test)
#
#     def startTestRun(self):
#         print('# blep')
#         unittest.TestResult.startTestRun(self)
#
#     def stopTestRun(self):
#         print('# blap')
#         unittest.TestResult.stopTestRun(self)
#
# class TestCaseX( unittest.TestCase ):
#     def test_nonsense(self):
#         print( '# wotcha' )
#         self.assertTrue( False )
#
#     def run( self, test_result=None ):
#         print( '# spoons starting...')
#
#         test_result = TestResultX()
#         unittest.TestCase.run( self, test_result )
#
#         print( '# ...spoons ended, tr %s' % ( test_result,  ) )
#
# unittest.main()

from selenium.common.exceptions import *
from com.generic_lib.initilization import *
import traceback

class NoSuchElementException(WebDriverException):
    logging.error('NoSuchElementException raised in method - ' + test_method_name)
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    self.driver.save_screenshot(
        Initilization.path + "Report\Screenshots\\" + test_method_name + "-" + now + ".png")
    traceback.print_exc()
    raise WebDriverException