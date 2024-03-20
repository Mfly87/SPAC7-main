from .abs_warehouse import AbsWarehouse
from dataClasses.absDataTypes import UniqueData

class WarehouseOOP(AbsWarehouse):
    _storage : dict[str, UniqueData] = dict()

    @property
    def item_count(self):
        return len(self._storage.keys())

    def search_item(self, search_string : str) -> list[UniqueData]:
        _item_list: list[UniqueData] = []
        for _item in self._storage.values():
            if _item.matches_search(search_string):
                _item_list.append(_item)
        return _item_list

    def get_items(self, id_list : list[str]) -> list[UniqueData]:
        _item_list: UniqueData = []
        for _id in id_list:
            if _id in self._storage:
                _item = self._storage[_id]
                _item_list.append(_item)
        return _item_list

    def update_item(self, item : UniqueData) -> None:
        self._storage |= {item.id: item}

    def delete_item(self, item : UniqueData) -> None:
        del self._storage[item.id]