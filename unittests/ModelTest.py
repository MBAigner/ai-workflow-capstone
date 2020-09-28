import unittest
import model
import os
import logger

DEBUG = False  # for incomplete test runs
if DEBUG:
    model.DATA_DIR = "../data"
    model.TRAIN_PATH = model.DATA_DIR + "/cs-train"
    model.MODEL_DIR = "../models"
    logger.LOG_PATH = "../logs"


class ModelTest(unittest.TestCase):

    def test_01_train(self):
        model.countries = ["germany"]
        model.model_train(data_dir=model.TRAIN_PATH, test=True)
        self.assertTrue(os.path.exists(model.MODEL_DIR + "/test-germany-0_4.joblib"))

    def test_02_train(self):
        model.countries = ["france"]
        model.model_train(data_dir=model.TRAIN_PATH, test=True)
        self.assertTrue(os.path.exists(model.MODEL_DIR + "/test-france-0_4.joblib"))

    def test_03_load(self):
        all_data, all_models = model.model_load("sl", data_dir=model.TRAIN_PATH)
        model_uk = all_models["united_kingdom"]
        self.assertTrue("predict" in dir(model_uk))
        self.assertTrue("fit" in dir(model_uk))

    def test_04_predict(self):
        result = model.model_predict("united_kingdom", "2017", "12", "03", test=True)
        self.assertTrue("y_pred" in result)

    def test_05_predict(self):
        result = model.model_predict("all", "2017", "12", "03", test=True)
        print(result)
        self.assertTrue("y_pred" in result)


if __name__ == "__main__":
    unittest.main()
