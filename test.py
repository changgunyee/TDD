from WasRun import WasRun
import unittest

class TestCaseTest(unittest.TestCase):
    def setUp(self) -> None:
        self.test=WasRun("testMethod")

    def testSetUp(self):
        self.test.run()
        print(self.test.log)
        assert(" setUp testMethod " == self.test.log)


    def testRunning(self):
        self.test.run()
        assert(self.test.wasRun)

if __name__ == '__main__':
    unittest.main()