from .abs_warehouse import AbsWarehouse
from dataClasses.absDataTypes import UniqueData, UniqueNamedData
from dataClasses.dataTypes import Product

import re

class WarehouseOOP(AbsWarehouse):
    _storage: dict[str, UniqueData] = dict()

    @property
    def item_count(self):
        _count = 0
        for _value in self._storage.values():
            if isinstance(_value, Product):
                _count += _value.quantity
        return _count
    
    @property
    def storage(self) -> dict[str, UniqueData]:
        return self._storage

    @property
    def object_count(self) -> int:
        return len(self._storage)
    
    def clear_warehouse(self):
        self.storage.clear()

    def set_inventory(self, inventory_dict: dict[str, list[UniqueData]]):
        self.clear_warehouse()

        for _item_list in inventory_dict.values():
            for _item in _item_list:
                self.update_item(_item)



    def search_item(self, search_string : str) -> list[UniqueData]:
        _item_list: list[UniqueData] = []
        for _item in self._storage.values():
            if WarehouseOOP.matches_search(_item, search_string):
                _item_list.append(_item)
        return _item_list


    def get_items(self, id_list : list[str]) -> list[UniqueData]:
        _item_list: UniqueData = []
        for _raw_id in id_list:
            _id = str(_raw_id).strip().lower()
            if _id in self._storage:
                _item = self._storage[_id]
                _item_list.append(_item)
        return _item_list

    def update_item(self, item : UniqueData) -> None:
        _id = item.id.lower()
        self._storage |= {_id: item}

    def delete_item(self, item : UniqueData) -> None:
        _id = item.id.lower()
        del self._storage[_id]


        

    @staticmethod
    def matches_search(obj: any, search_string: str) -> bool:
        if WarehouseOOP.matches_search_unique_data(obj, search_string):
            return True
        if WarehouseOOP.matches_search_unique_named_data(obj, search_string):
            return True
        return False

    @staticmethod
    def matches_search_unique_data(unique_data:UniqueData, search_string : str) -> bool:
        if not isinstance(unique_data, UniqueData):
            return False
        if re.search(search_string, unique_data.id, re.IGNORECASE):
            return True
        return False

    @staticmethod
    def matches_search_unique_named_data(unique_named_data:UniqueNamedData, search_string : str) -> bool:
        if not isinstance(unique_named_data, UniqueNamedData):
            return False
        if re.search(search_string, unique_named_data.name, re.IGNORECASE):
            return True
        if re.search(search_string, unique_named_data.description, re.IGNORECASE):
            return True
        return False