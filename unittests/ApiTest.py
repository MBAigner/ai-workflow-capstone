import unittest
import model
from model import *
import logger
import requests


DEBUG = False  # for incomplete test runs
if DEBUG:
    model.DATA_DIR = "../data"
    model.TRAIN_PATH = model.DATA_DIR + "/cs-train"
    model.MODEL_DIR = "../models"
    logger.LOG_PATH = "../logs"


class ApiTest(unittest.TestCase):

    def test_01_log(self):
        request = {"type": "predict"}
        r = requests.post("http://0.0.0.0:8080/logs",
                          json=request)
        header = "country;y_pred;y_proba;target_date;runtime;version;source"
        self.assertTrue(header in r.text)

    def test_02_log(self):
        request = {"type": "train"}
        r = requests.post("http://0.0.0.0:8080/logs",
                          json=request)
        header = "tag;dates;rmse;runtime;version;version_note;source"
        self.assertTrue(header in r.text)

    def test_03_log(self):
        request = {}
        r = requests.post("http://0.0.0.0:8080/logs",
                          json=request)
        self.assertTrue("error_message" in r.text)

    def test_04_train(self):
        request = {"test": False,
                   "country": "eire"}
        r = requests.post("http://0.0.0.0:8080/train",
                          json=request)
        self.assertTrue(os.path.exists(model.MODEL_DIR + "/sl-eire-0_4.joblib"))

    def test_05_train(self):
        request = {"test": True,
                   "country": "eire"}
        r = requests.post("http://0.0.0.0:8080/train",
                          json=request)
        self.assertTrue(os.path.exists(model.MODEL_DIR + "/test-eire-0_4.joblib"))

    def test_06_train(self):
        request = {"test": True,
                   "country": "nonsense"}
        r = requests.post("http://0.0.0.0:8080/train",
                          json=request)
        self.assertTrue("error_message" in r.text)

    def test_07_train(self):
        request = {"test": False,
                   "country": "all"}
        r = requests.post("http://0.0.0.0:8080/train",
                          json=request)
        self.assertTrue(os.path.exists(model.MODEL_DIR + "/sl-france-0_4.joblib"))

    def test_08_predict(self):
        request = {"date": "12.12.2017",
                   "country": "united_kingdom"}
        r = requests.post("http://0.0.0.0:8080/predict",
                          json=request)
        self.assertTrue("prediction" in r.text)

    def test_09_predict(self):
        request = {"date": "12.12.2017",
                   "country": "nonsense"}
        r = requests.post("http://0.0.0.0:8080/predict",
                          json=request)
        self.assertTrue("error_message" in r.text)


if __name__ == "__main__":
    unittest.main()
