import unittest
from model import *


class ModelTest(unittest.TestCase):

    def test_01_train(self):
        pass
        # TODO
        self.assertTrue(os.path.exists("SAVED_MODEL"))

    def test_02_load(self):
        pass
        # TODO
        self.assertTrue("predict" in dir("model"))
        self.assertTrue("fit" in dir("model"))

    def test_03_predict(self):
        pass
        # TODO
        example_queries = [None]
        for query in example_queries:
            result = model_predict(query) #"TODO")
            y_pred = result["y_pred"]
            self.assertTrue(y_pred in [0,1,2])#TODO

    def test_04_predict(self):
        pass
        # TODO
        example_queries = [None]
        for query in example_queries:
            result = model_predict(query) #"TODO")
            y_pred = result["y_pred"]
            self.assertTrue(y_pred in [0,1,2])#TODO


if __name__ == "__main__":
    unittest.main()
