import unittest
from model import *
import requests


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
        self.assertTrue(os.path.exists("../models/sl-eire-0_4.joblib"))

    def test_05_train(self):
        request = {"test": True,
                   "country": "eire"}
        r = requests.post("http://0.0.0.0:8080/train",
                          json=request)
        self.assertTrue(os.path.exists("../models/test-eire-0_4.joblib"))

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
        self.assertTrue(os.path.exists("../models/sl-france-0_4.joblib"))


if __name__ == "__main__":
    unittest.main()
