import unittest
import os
import model


class LogTest(unittest.TestCase):

    def test_01_predict_log(self):
        model.model_predict("eire", "2018", "8", "15")
        self.assertTrue(os.path.exists("../logs/predict_log.csv"))

    def test_02_train_log(self):
        model.model_train(data_dir=model.TRAIN_PATH)
        self.assertTrue(os.path.exists("../logs/train_log.csv"))


if __name__ == "__main__":
    unittest.main()
