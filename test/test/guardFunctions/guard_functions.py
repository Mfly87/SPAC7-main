from parameterized import parameterized

import dataClasses.guardFunctions.str_func as str_func
'''
@parameterized.expand([
    [None, None],
    ["", None],
    [" ", None],
    ["abc", str],
    [12345, str],
])
def test_func(value, expected_type):
    _value = sf.str_non_empty(value)
    assert type(_value) is expected_type
'''