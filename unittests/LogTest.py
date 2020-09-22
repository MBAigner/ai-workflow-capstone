import unittest
import os
import model
import logger


class LogTest(unittest.TestCase):

    DEBUG = False
    if DEBUG:
        model.DATA_DIR = "../data"
        model.TRAIN_PATH = model.DATA_DIR + "/cs-train"
        model.MODEL_DIR = "../models"
        logger.LOG_PATH = "../logs"

    def test_01_predict_log(self):
        model.model_predict("eire", "2018", "8", "15", test=True)
        self.assertTrue(os.path.exists(logger.LOG_PATH + "/predict_log.csv"))

    def test_02_train_log(self):
        model.model_train(data_dir=model.TRAIN_PATH, test=True)
        self.assertTrue(os.path.exists(logger.LOG_PATH + "/train_log.csv"))


if __name__ == "__main__":
    unittest.main()
