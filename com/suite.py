from com.scripts.script_01 import *
from com.scripts.script_03 import *
from com.scripts.script_02 import *

class Suite(unittest.TestCase):

    def test_main(self):
        logging.info('Inside test suite')
        self.suite = unittest.TestSuite().addTests([unittest.defaultTestLoader.loadTestsFromTestCase(Men),
                             unittest.defaultTestLoader.loadTestsFromTestCase(Sports),
                             unittest.defaultTestLoader.loadTestsFromTestCase(Women),
                             unittest.defaultTestLoader.loadTestsFromTestCase(Kids),
                             unittest.defaultTestLoader.loadTestsFromTestCase(SignIn)])

        runner = unittest.TestSuite()

import unittest
if __name__=="__main__":
    unittest.main