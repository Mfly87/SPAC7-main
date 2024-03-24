from parameterized import parameterized
from dataClasses.dataTypes import Category
from dataClasses.absDataTypes import UniqueNamedData

from my_tests.dataClasses.absDataTypes.class_test_category import ForTestCategory

from datetime import datetime

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
    '''
    @parameterized.expand([
        [0, True, "Should be equal to self"],
        [1, True, "Should be equal to identical copy"],
        [2, False, "Should not be equal to variant"],
        [3, False, "Should not be equal to different class"],
    ])
    def test_eq_comparison(self, index, is_valid, message):       
        sut_list: UniqueNamedData = [
            Category("abc", "abc", "abc"),
            Category("abc", "abc", "abc"),
            Category("xyz", "xyz", "xyz"),
            ForTestCategory("xyz", "xyz", "xyz"),
        ]

        sut = sut_list[0] == sut_list[index]
        assert sut == is_valid, "%s == %s %s" % (sut_list[0].to_list(), sut_list[index].to_list(), message)
    '''
    @parameterized.expand([
        [Category("abc", "abc", "abc"), True],
        [Category("xyz", "xyz", "xyz"), False],
        [ForTestCategory("xyz", "xyz", "xyz"), False],
    ])
    def test_eq_comparison(self, other: UniqueNamedData, is_valid):       
        sut = Category("abc", "abc", "abc")
        are_equal = sut == other
        assert are_equal == is_valid, "%s == %s should be %s" % (sut.to_list(), other.to_list(), are_equal)

    def test_time_format(self):
        sut = Category("xyz", "xyz", "xyz")
        _date = datetime(1900,11,12)
        _str_from_date = _date.strftime(sut.date_format)
        
        assert _str_from_date == "1900-11-12"