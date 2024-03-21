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
    