import unittest
from unittests import *
from unittests.ModelTest import ModelTest
from unittests.ApiTest import ApiTest
from unittests.LogTest import LogTest
import model
import logger

suite = unittest.TestSuite()

model = unittest.TestLoader().loadTestsFromTestCase(ModelTest)
log = unittest.TestLoader().loadTestsFromTestCase(LogTest)
api = unittest.TestLoader().loadTestsFromTestCase(ApiTest)

suite.addTests(model)
suite.addTests(log)
suite.addTests(api)


