from warehouse import WarehouseOOP
from dataFaker import FakeWarehouseFiller

class TestWarehouseFiller():

    def test_warehouse_filler(self):
        _category_count = 5
        _product_count = 10
        _transaction_count = 20

        wh = WarehouseOOP()
        FakeWarehouseFiller.fill_warehouse(wh, _category_count, _product_count, _transaction_count)

        _sum = _category_count + _product_count + _transaction_count
        assert wh.object_count == _sum
