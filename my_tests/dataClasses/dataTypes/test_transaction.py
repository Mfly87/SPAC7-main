from parameterized import parameterized

from datetime import datetime, date

from dataClasses.dataTypes import Transaction
from dataClasses import DataClassFactory

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
        [-1, True],
        [0, True],
        [1, True],
        [3.14, False],
    ]

    param_date_guard = [
        [None, False],
        [123, False],
        ["1900-01-01", True],
        ["01-01-1900", False],
        [datetime(1900,1,1), True],
        [date(1900,1,1), True],
    ]

    
    @parameterized.expand(param_string_guard)
    def test_id_is_guarded(self, id, is_valid):
        sut = Transaction(id, "abc", datetime(1900,1,1), 123, "abc")
        assert sut.is_valid() == is_valid
        if is_valid:
            assert isinstance(sut.id, str)

    @parameterized.expand(param_string_guard)
    def test_product_id_is_guarded(self, product_id, is_valid):
        sut = Transaction("abc", product_id, datetime(1900,1,1), 123, "abc")
        assert sut.is_valid() == is_valid
        if is_valid:
            assert isinstance(sut.product_id, str)

    @parameterized.expand(param_date_guard)
    def test_date_is_guarded(self, date, is_valid):
        sut = Transaction("abc", "abc", date, 123, "abc")
        assert sut.is_valid() == is_valid
        if is_valid:
            assert isinstance(sut.date, datetime)

    @parameterized.expand(param_int_guard)
    def test_quantity_is_guarded(self, quantity, is_valid):
        sut = Transaction("abc", "abc", datetime(1900,1,1), quantity, "abc")
        assert sut.is_valid() == is_valid
        if is_valid:
            assert isinstance(sut.quantity, int)

    @parameterized.expand(param_string_guard)
    def test_type_is_guarded(self, type, is_valid):
        sut = Transaction("abc", "abc", datetime(1900,1,1), 123, type)
        assert sut.is_valid() == is_valid
        if is_valid:
            assert isinstance(sut.type, str)