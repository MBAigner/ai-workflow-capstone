import unittest
import os


class LogTest(unittest.TestCase):

    def test_01_predict_log(self):
        pass
        # TODO
        self.assertTrue(os.path.exists("SAVED_MODEL"))

    def test_02_train_log(self):
        pass
        # TODO
        self.assertTrue(os.path.exists("SAVED_MODEL"))


if __name__ == "__main__":
    unittest.main()
