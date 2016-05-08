from com.scripts.script_01 import *
from com.scripts.script_03 import *
from com.scripts.script_02 import *
#import HTMLTestRunner

class Suite(unittest.TestCase):

    def test_main(self):
        logging.info('Inside test suite')
        suite = unittest.TestSuite().addTests([unittest.defaultTestLoader.loadTestsFromTestCase(Men),
                             unittest.defaultTestLoader.loadTestsFromTestCase(Sports),
                             unittest.defaultTestLoader.loadTestsFromTestCase(Women),
                             unittest.defaultTestLoader.loadTestsFromTestCase(Kids),
                             unittest.defaultTestLoader.loadTestsFromTestCase(SignIn)])

        unittest.TestSuite()

        # outfile = open("D:\CBT_Automation\Python\Workspace_Python\Report\Framework_Jabong\HTML_Report\TestReport.html", "w")
        # runner = HTMLTestRunner.HTMLTestRunner(
        #     stream = outfile,
        #     title = 'Execution Report',
        #     description = 'Suite Run'
        # )
        # runner.run(suite)

import unittest
if __name__=="__main__":
    unittest.main