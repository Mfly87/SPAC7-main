from parameterized import parameterized

from dataClasses.dataTypes import Category
from dataClasses import DataClassFactory

class TestCategory():

    @parameterized.expand([
        [None, False],
        ["", False],
        [" ", False],
        ["abc", True],
        [123, True],
    ])
    def test_id_is_guarded(self, id, is_valid):
        sut = Category(id, "Apple", "Not the fruit")
        assert sut.is_valid() == is_valid
        if is_valid:
            assert isinstance(sut.id, str)

    @parameterized.expand([
        [None, False],
        ["", False],
        [" ", False],
        ["Apple", True],
        [12345, True],
    ])
    def test_name_is_guarded(self, name, is_valid):
        sut = Category("abc", name, "Not the fruit")
        assert sut.is_valid() == is_valid
        if is_valid:
            assert isinstance(sut.id, str)
    
    @parameterized.expand([
        [None, False],
        ["", False],
        [" ", False],
        ["Not the fruit", True],
        [12345, True],
    ])
    def test_description_is_guarded(self, description, is_valid):
        sut = Category("abc", "Apple", description)
        assert sut.is_valid() == is_valid
        if is_valid:
            assert isinstance(sut.id, str)

    def test_to_dict(self):
        _id = "abc"
        _name = "Apple"
        _description = "Not the fruit"

        sut = Category(_id, _name, _description)
        _dict = sut.to_dict()

        assert _dict["class"] == "Category"
        assert _dict["id"] == _id
        assert _dict["name"] == _name
        assert _dict["description"] == _description

    def test_has_factory(self):
        _params = ["abc", "Apple", "Not the fruit"]
        _base = Category(*_params)
        _category_list = DataClassFactory.create_category(*_params)
        assert len(_category_list) == 1
        for _sut in _category_list:
            assert _base == _sut

    def test_factory_doesnt_create_defects(self):
        _category_list = DataClassFactory.create_category(None, None, None)
        assert len(_category_list) == 0

    def test_factory_can_copy_from_dict(self):
        _base = Category("abc", "Apple", "Not the fruit")
        _dict = _base.to_dict()

        _category_list = DataClassFactory.create_category(**_dict)
        assert len(_category_list) == 1
        for _sut in _category_list:
            assert isinstance(_sut, Category)

            assert _base.id == _sut.id
            assert _base.name == _sut.name
            assert _base.description == _sut.description
