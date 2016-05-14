# import unittest
# from com.generic_lib.initilization import *
# from selenium import webdriver
# # from selenium.webdriver.support.events import EventFiringWebDriver
# # from selenium.webdriver.support.events import AbstractEventListener
# #
# # class ScreenshotListener(AbstractEventListener, Initilization):
# #
# #     def __init__(self, test_method_name):
# #         self.test_method_name = test_method_name
# #
# #     def on_exception(self, exception, driver):
# #         dir = os.path.dirname(__file__)
# #         path = dir[:len(dir)-15]
# #         screenshot_name = self.test_method_name
# #         now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
# #         time.sleep(3)
# #         driver.get_screenshot_as_file(screenshot_name + "-" + now + ".jpg")
# #         print("Screenshot saved as '%s'" % screenshot_name)
#
#
#
# class Listener(unittest.TestResult, Initilization):
#
#     def test_fail(self):
#         self.assertEqual(1, 0, "broken")
#
#     # def on_failure(self):
#     #
#     #     unittest.TextTestRunner.run()
#
#
#
#
#
#
#
#
# # class TestResultX( unittest.TestResult ):
# #     def startTest( self, test ):
# #         print( '# blip')
# #         unittest.TestResult.startTest( self, test )
# #     def stopTest( self, test ):
# #         print( '# blop')
# #         unittest.TestResult.stopTest( self, test )
# #     def startTestRun( self ):
# #         print( '# blep')
# #         unittest.TestResult.startTestRun( self )
# #     def stopTestRun( self ):
# #         print( '# blap')
# #         unittest.TestResult.stopTestRun( self )
# #
# # class TestCaseX( unittest.TestCase ):
# #     def test_nonsense(self):
# #         print( '# wotcha' )
# #         self.assertTrue( False )
# #
# #     def run( self, test_result=None ):
# #         print( '# spoons starting...')
# #
# #         test_result = TestResultX()
# #         unittest.TestCase.run( self, test_result )
# #
# #         print( '# ...spoons ended, tr %s' % ( test_result,  ) )
# #
# # unittest.main()
#
#
#
