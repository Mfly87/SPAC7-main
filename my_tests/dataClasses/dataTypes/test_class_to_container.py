from dataClasses.dataTypes import Category, Product, Transaction
from dataClasses import DataClassFactory, UniqueData

from datetime import datetime
from typing import Callable

import unittest

class TestClassToContainer(unittest.TestCase):
    
    def _generic_test_setup(self, class_type, params: list[any], headers: list[str]):
        # "Class" parameter isn't needed to build class, but an expected part of output
        params.append(class_type.__name__)

        _class: UniqueData = class_type(*params)
        
        with self.subTest("to_list"):
            self._generic_to_list(_class, params)
            
        with self.subTest("get_headers"):
            self._generic_get_headers(_class, headers)
            
        with self.subTest("to_dict"):
            self._generic_to_dict(_class, params, headers)


    def _generic_to_list(self, test_class: UniqueData, params: list[any]):
        _list = test_class.to_list()
        for a, b in zip(_list, params):
            assert a == b; "%s should be equal to %s" % (a, b)

    def _generic_get_headers(self, test_class: UniqueData, headers: list[str]):
        _list = test_class.get_headers()
        for a, b in zip(_list, headers):
            assert a == b; "%s should be equal to %s" % (a, b)

    def _generic_to_dict(self, test_class: UniqueData, params: list[any], headers: list[str]):
        _dict = test_class.to_dict()

        for _key in _dict:
            assert _key in headers; "%s not in %s" % (_key, headers)
            assert _dict[_key] in params; "%s not in %s" % (_dict[_key], params)


    def test_category(self):
        self._generic_test_setup(
            Category,
            ["abc", "abc", "abc"],
            ["id", "name", "description", "class"]
        )

    def test_product(self):
        self._generic_test_setup(
            Product,
            ["abc", "abc", "abc", "abc", 123, 123],
            ["id","name","description","category_id","price","quantity","class"]
        )

    def test_transaction(self):
        self._generic_test_setup(
            Transaction,
            ["abc", "abc", "1900-01-01", 123, "abc"],
            ["id","product_id","date","quantity","transaction_type","class",]
        )