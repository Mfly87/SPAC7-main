from parameterized import parameterized

from datetime import datetime

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
        [-1, False],
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


    
    
    def test_has_factory(self):
        _params = ["abc", "abc", datetime(1900,1,1), 123, "abc"]
        _base = Transaction(*_params)
        _category_list = DataClassFactory.create_transaction(*_params)
        assert len(_category_list) == 1
        for _sut in _category_list:
            assert _base == _sut

    def test_factory_doesnt_create_defects(self):
        _category_list = DataClassFactory.create_transaction(None, None, None, None, None)
        assert len(_category_list) == 0

    def test_factory_can_copy_from_dict(self):
        _base = Transaction("abc", "abc", datetime(1900,1,1), 123, "abc")
        _dict = _base.to_dict()

        _category_list = DataClassFactory.create_transaction(**_dict)
        assert len(_category_list) == 1
        for _sut in _category_list:
            assert _base == _sut