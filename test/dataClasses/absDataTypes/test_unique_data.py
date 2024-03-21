from parameterized import parameterized
from dataClasses.dataTypes import Category

# Uses Category as non-abstract class for example

class TestUniqueData():

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
        [0, True, "Should be equal to self"],
        [1, True, "Should be equal to identical copy"],
        [2, False, "Should not be equal to variant"],
    ])
    def test_eq_comparison(self, index, is_valid, message):
        sut_list = [
            Category("abc", "abc", "abc"),
            Category("abc", "abc", "abc"),
            Category("xyz", "xyz", "xyz"),
        ]

        sut = sut_list[0] == sut_list[index]
        assert sut == is_valid, message
