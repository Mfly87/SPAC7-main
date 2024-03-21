from parameterized import parameterized

import dataClasses.guardFunctions.str_func as sf

@parameterized.expand([
    [None, None],
    ["", None],
    [" ", None],
    ["abc", str],
    [12345, str],
])
def test_func(value, expected_type):
    _value = sf.str_non_empty(value)

    if expected_type is None:
        assert _value is None
    else:
        assert type(_value) is expected_type
