#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import json
from lib.httpl import http_post
from lib.testdata import random_data


""" This is written to work with nosetest, the print statmetnts
in the libs will be supressed when if a test passes when nosetest
is running. When it fails the print statments will be usefull for
seeting the output data to find the issue"""


class TestGenClass(unittest.TestCase):
    pass


def dynamic_gen(test_assert):
    def dynamic_test_method(self):
        shared = {
            "api": "post",
            "host": "httpbin.org"
        }
        result_code, http_data = http_post(
            shared.get('host'),
            api=shared.get('api'),
            payload={"hex": test_assert}
        )
        data = json.loads(http_data)
        self.assertEqual(int(result_code), 200)
        self.assertEqual(
            unicode(test_assert),
            json.loads(data.get('data')).get('hex')
        )

    return dynamic_test_method

testmap = random_data(10)
for name, parms in testmap.iteritems():
    data = dynamic_gen(parms["hex"])
    data.__name__ = "test_{0}".format(name)
    data.__doc__ = "test_{0}".format(name)
    setattr(TestGenClass, data.__name__, data)
    del data

if __name__ == "__main__":
    unittest.main()
