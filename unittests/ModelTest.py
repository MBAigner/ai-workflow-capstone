import unittest
import model
import os


class ModelTest(unittest.TestCase):

    def test_01_train(self):
        model.countries = ["germany"]
        model.model_train(data_dir=model.TRAIN_PATH, test=False)
        self.assertTrue(os.path.exists("../models/sl-eire-0_4.joblib"))

    def test_02_train(self):
        model.countries = ["france"]
        model.model_train(data_dir=model.TRAIN_PATH, test=True)
        self.assertTrue(os.path.exists("../models/test-france-0_4.joblib"))

    def test_03_load(self):
        pass
        # TODO
        self.assertTrue("predict" in dir("model"))
        self.assertTrue("fit" in dir("model"))

    def test_04_predict(self):
        pass
        # TODO
        example_queries = [None]
        for query in example_queries:
            result = model_predict(query) #"TODO")
            y_pred = result["y_pred"]
            self.assertTrue(y_pred in [0,1,2])#TODO

    def test_05_predict(self):
        pass
        # TODO
        example_queries = [None]
        for query in example_queries:
            result = model_predict(query) #"TODO")
            y_pred = result["y_pred"]
            self.assertTrue(y_pred in [0,1,2])#TODO


if __name__ == "__main__":
    unittest.main()
