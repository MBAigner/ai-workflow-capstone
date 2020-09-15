import unittest
from unittests import *
from unittests.ModelTest import ModelTest
from unittests.ApiTest import ApiTest
from unittests.LogTest import LogTest

suite = unittest.TestSuite()

model = unittest.TestLoader().loadTestsFromTestCase(ModelTest)
log = unittest.TestLoader().loadTestsFromTestCase(LogTest)
api = unittest.TestLoader().loadTestsFromTestCase(ApiTest)

suite.addTests(model)
suite.addTests(log)
suite.addTests(api)


