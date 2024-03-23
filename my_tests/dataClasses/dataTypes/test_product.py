from parameterized import parameterized

from dataClasses.dataTypes import Product
from dataClasses import DataClassFactory

from dataFaker import FakeCategory, FakeProduct

class TestProduct():

    param_string_guard = [
        [None, False],
        ["", False],
        [" ", False],
        ["abc", True],
        [123, True],
    ]

    param_int_guard = [
        [None, False],
        [-1, False],
        [0, True],
        [1, True],
        [3.14, False],
    ]

    @parameterized.expand(param_string_guard)
    def test_id_is_guarded(self, id, is_valid):
        sut = Product(id, "abc", "abc", "abc", 123, 123)
        assert sut.is_valid() == is_valid
        if is_valid:
            assert isinstance(sut.id, str)

    @parameterized.expand(param_string_guard)
    def test_name_is_guarded(self, name, is_valid):
        sut = Product("abc", name, "abc", "abc", 123, 123)
        assert sut.is_valid() == is_valid
        if is_valid:
            assert isinstance(sut.name, str)

    @parameterized.expand(param_string_guard)
    def test_description_is_guarded(self, description, is_valid):
        sut = Product("abc", "abc", description, "abc", 123, 123)
        assert sut.is_valid() == is_valid
        if is_valid:
            assert isinstance(sut.description, str)

    @parameterized.expand(param_string_guard)
    def test_category_id_is_guarded(self, category_id, is_valid):
        sut = Product("abc", "abc", "abc", category_id, 123, 123)
        assert sut.is_valid() == is_valid
        if is_valid:
            assert isinstance(sut.category_id, str)

    @parameterized.expand(param_int_guard)
    def test_price_is_guarded(self, price, is_valid):
        sut = Product("abc", "abc", "abc", "abc", price, 123)
        assert sut.is_valid() == is_valid
        if is_valid:
            assert isinstance(sut.price, int)

    @parameterized.expand(param_int_guard)
    def test_quantity_is_guarded(self, quantity, is_valid):
        sut = Product("abc", "abc", "abc", "abc", 123, quantity)
        assert sut.is_valid() == is_valid
        if is_valid:
            assert isinstance(sut.quantity, int)