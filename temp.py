from dataClasses.dataTypes import Category

_a = Category("abc","abc","abc")
_b = Category("xyz","xyz","xyz")


_list_a = _a.to_list()
_list_b = _b.to_list()

for a, b in zip(_list_a, _list_b):
    if a != b:
        print("False")