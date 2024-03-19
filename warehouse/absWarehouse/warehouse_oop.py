from typing import TypeVar, Generic, Callable, TypeAlias
from .abs_warehouse import AbsWarehouse

T = TypeVar("T")

class WarehouseOOP(AbsWarehouse, Generic[T]):
    _storage : dict[str,T] = dict()

    def __init__(self, get_id_func: Callable[[T],str], search_func: Callable[[T,str],bool]) -> None:
        self._get_id_func = get_id_func
        self._search_func = search_func

    def search_item(self, search_string : str) -> list[T]:
        _item_list: list[T] = []
        for _item in self._storage.values():
            if self._search_func(_item, search_string):
                _item_list.append(_item)
        return _item_list

    def get_items(self, id_list : list[str]) -> list[T]:
        _item_list = []
        for _id in id_list:
            if _id in self._storage:
                _item_list.append(self._storage[_id])
        return _item_list

    def update_item(self, item : T) -> None:
        _id = self._get_id_func(item)
        self._storage |= {_id: item}

    def delete_item(self, item : T) -> None:
        _id = self._get_id_func(item)
        del self._storage[_id]