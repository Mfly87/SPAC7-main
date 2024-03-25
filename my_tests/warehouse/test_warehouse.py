from faker import Faker

from warehouse import WarehouseOOP
from dataFaker import FakeWarehouseFiller

from dataClasses.dataTypes import Category, Product, Transaction

class TestWarehouseFiller():

    def test_warehouse_search(self):
        _category_count = 100
        _product_count = 100
        _transaction_count = 100

        Faker.seed(0)

        wh = WarehouseOOP()
        FakeWarehouseFiller.fill_warehouse(wh, _category_count, _product_count, _transaction_count)

        _search_list = wh.search_table("0009")
        
        _category_list = [i for i in _search_list if isinstance(i, Category)]
        _product_list = [i for i in _search_list if isinstance(i, Product)]
        _transaction_list = [i for i in _search_list if isinstance(i, Transaction)]

        assert 11 == len(_category_list)
        assert 11 == len(_product_list)
        assert 11 == len(_transaction_list)

