from parameterized import parameterized

import dataClasses.guardFunctions.int_func as int_func

class TestIntGuard():
    
    @parameterized.expand([
        [None, None],
        ["123", int],
        [-1, int],
        [0, int],
        [1, int],
        [3.14, None],
    ])
    def test_int_is_int(self, value, expected_type):
        _value = int_func.int_is_int(value)
        if expected_type is None:
            assert _value is None
        else:
            assert type(_value) is expected_type

    @parameterized.expand([
        [None, None],
        ["123", int],
        [-1, None],
        [0, int],
        [1, int],
        [3.14, None],
    ])
    def test_int_is_int(self, value, expected_type):
        _value = int_func.int_zero_or_greater(value)
        if expected_type is None:
            assert _value is None
        else:
            assert type(_value) is expected_type
