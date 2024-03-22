import abc

from dataClasses.absDataTypes import UniqueData
from dataClasses.dataTypes import Product

class AbsWarehouse(abc.ABC):
    _storage : dict[str, UniqueData] = dict()

    @property
    def item_count(self):
        _count = 0
        for _value in self._storage.values():
            if isinstance(_value, Product):
                _count += _value.quantity
        return _count
    
    @property
    def object_count(self):
        return len(self._storage)

    @property
    def object_count(self):
        return len(self._storage)
    
    @abc.abstractclassmethod
    def search_item(self):
        pass

    @abc.abstractclassmethod
    def get_items(self):
        pass

    @abc.abstractclassmethod
    def update_item(self):
        pass

    @abc.abstractclassmethod
    def delete_item(self):
        pass