from com.scripts.script_03 import *
from com.scripts.script_02 import *
from com.scripts.script_01 import *

import HTMLTestRunner

class Suite(unittest.TestCase):

    def test_main(self):
        logging.info('Inside test suite')
        self.suite = unittest.TestSuite([unittest.defaultTestLoader.loadTestsFromTestCase(Script03_Men),
                                         unittest.defaultTestLoader.loadTestsFromTestCase(Script02_Sports),
                                         unittest.defaultTestLoader.loadTestsFromTestCase(Script02_Sports),
                                         unittest.defaultTestLoader.loadTestsFromTestCase(Script01_SignIn)])

        outputfile = open("D:\CBT_Automation\Python\Workspace_Python_2\Framework_Jabong\Report\HTML_Report\TestReport.html", "w")
        runner = HTMLTestRunner.HTMLTestRunner(stream=outputfile,title='Execution Report',description='Suite Run')
        runner.run(self.suite)