from parameterized import parameterized
from dataClasses.dataTypes import Category

# Uses Category as non-abstract class for example

class TestUniqueNamedData():

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