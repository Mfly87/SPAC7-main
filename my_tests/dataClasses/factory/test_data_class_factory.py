from dataClasses.dataTypes import Category, Product, Transaction
from dataClasses import DataClassFactory, UniqueData

from datetime import datetime
from typing import Callable

import unittest

class TestDataClassFactory(unittest.TestCase):

    def _generic_class_creation_test(self, class_type, working_params, failing_params, dedicated_build_func):
        with self.subTest("working dedicated"):
            self._generic_dedicated_factory_test(class_type, dedicated_build_func, 1, working_params)
            
        with self.subTest("failing dedicated"):
            self._generic_dedicated_factory_test(class_type, dedicated_build_func, 0, failing_params)

        with self.subTest("working generic"):
            self._generic_factory_test(class_type, 1, working_params)

        with self.subTest("failing generic"):
            self._generic_factory_test(class_type, 0, failing_params)

    def _generic_dedicated_factory_test(self, class_type: UniqueData, dedicated_build_func: Callable[[any],list[UniqueData]], expected_count: int, params: list[any]):
        _base = class_type(*params)
        _category_list = dedicated_build_func(*params)
        assert len(_category_list) == expected_count
        for _sut in _category_list:
            assert _base == _sut
            
    def _generic_factory_test(self, class_type: UniqueData, expected_count: int, params: list[any]):
        _base: UniqueData = class_type(*params)
        _dict = _base.to_dict()
        _category_list = DataClassFactory.create_from_dict(**_dict)
        assert len(_category_list) == expected_count
        for _sut in _category_list:
            assert _base == _sut

    def test_category(self):
        self._generic_class_creation_test(
            Category,
            ["abc", "Apple", "Not the fruit"],
            [None, None, None], 
            DataClassFactory.create_category
        )

    def test_product(self):
        self._generic_class_creation_test(
            Product,
            ["abc", "abc", "abc", "abc", 123, 123],
            [None, None, None, None, None, None], 
            DataClassFactory.create_product
        )

    def test_transaction(self):
        self._generic_class_creation_test(
            Transaction,
            ["abc", "abc", datetime(1900,1,1), 123, "abc"],
            [None, None, None, None, None], 
            DataClassFactory.create_transaction
        )

