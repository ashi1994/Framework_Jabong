from com.scripts.script_02 import *
import HTMLTestRunner


class Suite(unittest.TestCase):
    """HTML Report is working in Python 2, not in Python 3."""

    def test_main(self):
        logging.info('Inside test suite')
        self.suite = unittest.TestSuite([unittest.defaultTestLoader.loadTestsFromTestCase(SignIn)])

        #unittest.TextTestRunner(verbosity=2).run(self.suite)

        outfile = open("D:\CBT_Automation\Python\Workspace_Python_2\Framework_Jabong\Report\HTML_Report\TestReport.html", "w")
        runner = HTMLTestRunner.HTMLTestRunner(
            stream = outfile,
            title = 'Execution Report',
            description = 'Suite Run'
        )
        runner.run(self.suite)

# import unittest
# if __name__=="__main__":
#     HTMLTestRunner.main