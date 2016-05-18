from com.scripts.script_03 import *
from com.scripts.script_02 import *
from com.scripts.script_01 import *
import unittest
import HTMLTestRunner

class Suite(unittest.TestCase):

    def test_main(self):
        logging.info('Inside test suite')
        self.suite = unittest.TestSuite([unittest.defaultTestLoader.loadTestsFromTestCase(Script01_SignIn),
                                         unittest.defaultTestLoader.loadTestsFromTestCase(Script02_Sports),
                                         unittest.defaultTestLoader.loadTestsFromTestCase(Script03_Men)])

        outputfile = open(Initilization.path+"Report\HTML_Report\TestReport"+"-" + Initilization.now + ".html", "w")
        runner = HTMLTestRunner.HTMLTestRunner(stream=outputfile, verbosity=2,title='Execution Report',description='Suite Run')
        runner.run(self.suite)