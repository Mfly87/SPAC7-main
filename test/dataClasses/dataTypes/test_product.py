from parameterized import parameterized

from dataClasses.dataTypes import Product
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

    @parameterized.expand(param_string_guard)
    def test_params_are_guarded(self, id, is_valid):
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


    
    
    def test_has_factory(self):
        _params = ["abc", "abc", "abc", "abc", 123, 123]
        _base = Product(*_params)
        _category_list = DataClassFactory.create_product(*_params)
        assert len(_category_list) == 1
        for _sut in _category_list:
            assert _base == _sut

    def test_factory_doesnt_create_defects(self):
        _category_list = DataClassFactory.create_product(None, None, None, None, None, None, None)
        assert len(_category_list) == 0

    def test_factory_can_copy_from_dict(self):
        _base = Product("abc", "abc", "abc", "abc", 123, 123)
        _dict = _base.to_dict()

        _category_list = DataClassFactory.create_product(**_dict)
        assert len(_category_list) == 1
        for _sut in _category_list:
            assert _base == _sut