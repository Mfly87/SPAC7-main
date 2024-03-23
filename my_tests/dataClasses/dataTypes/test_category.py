from parameterized import parameterized

from dataClasses.dataTypes import Category
from dataClasses import DataClassFactory

from dataFaker import FakeCategory

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