from warehouse import WarehouseOOP
from dataFaker import FakeWarehouseFiller
from dataClasses.dataTypes import Category, Product, Transaction

class TestWarehouseFiller():

    def test_inventory_creation(self):
        _category_count = 5
        _product_count = 10
        _transaction_count = 20

        sut = FakeWarehouseFiller.create_inventory_dict(_category_count, _product_count, _transaction_count)
        
        assert len(sut[Category.__name__]) == _category_count
        assert len(sut[Product.__name__]) == _product_count
        assert len(sut[Transaction.__name__]) == _transaction_count

    def test_filling_warehouse(self):
        _category_count = 5
        _product_count = 10
        _transaction_count = 20

        wh = WarehouseOOP()
        FakeWarehouseFiller.fill_warehouse(wh, _category_count, _product_count, _transaction_count)

        _sum = _category_count + _product_count + _transaction_count
        assert wh.object_count == _sum

