import unittest
from unittests import *
from unittests.ModelTest import ModelTest
from unittests.ApiTest import ApiTest
from unittests.LogTest import LogTest
import model
import logger

suite = unittest.TestSuite()

modeltest = unittest.TestLoader().loadTestsFromTestCase(ModelTest)
logtest = unittest.TestLoader().loadTestsFromTestCase(LogTest)
apitest = unittest.TestLoader().loadTestsFromTestCase(ApiTest)

suite.addTests(modeltest)
suite.addTests(logtest)
suite.addTests(apitest)


