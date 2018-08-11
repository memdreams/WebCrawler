# -*- coding:utf-8 -*-
"""
Basic automatic test script: basic_demo.py
"""
__author__ = "Jie"

import unittest
# use HTMLTestRunner make better result format
# from HTMLTestRunner import HTMLTestRunner

class TestStringMethods(unittest.TestCase):
    def setUp(self):
        print('init by setUp...')

    def tearDown(self):
        print('end by tearDown...')

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())
        self.assertTrue('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    # unittest.main()
    # load test cases
    test_cases = unittest.TestLoader().loadTestsFromTestCase(TestStringMethods)
    # use test suites and pack the test cases
    test_suite = unittest.TestSuite()
    test_suite.addTests(test_cases)
    # run test_suite and return the test results
    # test_result = unittest.TextTestRunner(verbosity=2).run(test_suite)
    # save the result to a file:
    with open('UnittestReport.txt', 'a') as f:
        test_result = unittest.TextTestRunner(stream=f, verbosity=2).run(test_suite)
    # with open ('HTMLReport.html', 'w') as f:
    #     runner = HTMLTestRunner(stream=f,
    #                             title='Basic StringFunc Test Report',
    #                             description='Generate by HTMLTestRunner',
    #                             verbosity=2
    #                             )
    #     runner.run(test_suite)
    # create test report
    print("testsRun:%s" % test_result.testsRun)
    print("failures:%s" % len(test_result.failures))
    print("errors:%s" % len(test_result.errors))
    print("skipped:%s" % len(test_result.skipped))
