from .fake_category import FakeCategory
from .fake_product import FakeProduct
from .fake_transaction import FakeTransaction

from dataClasses import UniqueData

from warehouse import AbsWarehouse

from typing import Callable

class FakeWarehouseFiller():

    @staticmethod
    def fill_warehouse(warehouse: AbsWarehouse, category_count: int, product_count: int, transaction_count: int):
        
        _category_list = FakeWarehouseFiller._fill_warehouse(
            warehouse,
            category_count,
            FakeCategory().generate_fake_item,
            None
            )
        
        _product_list = FakeWarehouseFiller._fill_warehouse(
            warehouse,
            product_count,
            FakeProduct().generate_fake_item_from_category_list,
            _category_list
            )
        
        _transaction_list = FakeWarehouseFiller._fill_warehouse(
            warehouse,
            transaction_count,
            FakeTransaction().generate_fake_item_from_product_list,
            _product_list
            )

    def _fill_warehouse(warehouse: AbsWarehouse, count: int, func: Callable[[],list[UniqueData]], params: any) -> list[UniqueData]:
        _data_list = []
        for _ in range(count):
            for _unique_data in func(params):
                _data_list.append(_unique_data)
                warehouse.update_item(_unique_data)
        return _data_list