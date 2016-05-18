from com.scripts.script_01 import *
import HTMLTestRunner


class Suite(unittest.TestCase):
    """HTML Report is working in Python 2, not in Python 3."""

    def test_main(self):
        logging.info('Inside test suite')
        self.suite = unittest.defaultTestLoader.loadTestsFromTestCase(Script01_SignIn)

        outfile = open(Initilization.path+"Report\HTML_Report\TestReport.html", "w")
        runner = HTMLTestRunner.HTMLTestRunner(stream = outfile, title = 'Execution Report', description = 'Suite_02 Run')
        runner.run(self.suite)

# import unittest
# if __name__=="__main__":
#     HTMLTestRunner.main