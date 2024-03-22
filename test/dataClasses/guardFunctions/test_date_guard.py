from parameterized import parameterized
from datetime import datetime, date
import dataClasses.guardFunctions.date_func as date_func

from dataClasses.dataTypes import Category

class TestIntGuard():
    
    @parameterized.expand([
        [None, None],
        [123, None],
        ["1900-01-01", datetime],
        ["01-01-1900", None],
        [datetime(1900,1,1), datetime],
        [date(1900,1,1), datetime],
    ])
    def test_int_is_int(self, value, expected_type):
        _obj = Category("abc", "abc", "abc")

        _value = date_func.date_is_date(value, _obj.date_format)
        if expected_type is None:
            assert _value is None
        else:
            assert type(_value) is expected_type