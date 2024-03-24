from .fake_category import FakeCategory
from .fake_product import FakeProduct
from .fake_transaction import FakeTransaction

from dataClasses import UniqueData
from dataClasses.dataTypes import Category, Product, Transaction

from warehouse import AbsWarehouse

from typing import Callable

class FakeWarehouseFiller():

    @staticmethod
    def fill_warehouse(warehouse: AbsWarehouse, category_count: int, product_count: int, transaction_count: int):
        _dict = FakeWarehouseFiller.create_inventory_dict(category_count, product_count, transaction_count)
        warehouse.set_inventory(_dict)

    @staticmethod
    def create_inventory_dict(category_count: int, product_count: int, transaction_count: int) -> dict[str,list[UniqueData]]:
        _ret_dict = dict()

        _ret_dict[Category.__name__] = FakeWarehouseFiller._generate_items(
            category_count,
            FakeCategory().generate_fake_item,
            []
            )
        
        _ret_dict[Product.__name__] = FakeWarehouseFiller._generate_items(
            product_count,
            FakeProduct().generate_fake_item_from_category_list,
            [_ret_dict[Category.__name__]]
            )
        
        _ret_dict[Transaction.__name__] = FakeWarehouseFiller._generate_items(
            transaction_count,
            FakeTransaction().generate_fake_item_from_product_list,
            [_ret_dict[Product.__name__]]
            )
        
        return _ret_dict

    @staticmethod
    def _generate_items(count: int, func: Callable[[],list[UniqueData]], params: list[any]) -> list[UniqueData]:
        _data_list = []
        for _ in range(count):
            for _unique_data in func(*params):
                _data_list.append(_unique_data)
        return _data_list