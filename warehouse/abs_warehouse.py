import abc
from dataClasses import UniqueData

class AbsWarehouse(abc.ABC):
    
    @abc.abstractclassmethod
    def clear_warehouse(self) -> None:
        pass

    @abc.abstractclassmethod
    def set_inventory(self, inventory_dict: dict[str, list[UniqueData]]) -> None:
        pass

    @abc.abstractclassmethod
    def search_item(self) -> list[UniqueData]:
        pass

    @abc.abstractclassmethod
    def get_items(self) -> UniqueData:
        pass

    @abc.abstractclassmethod
    def update_item(self) -> None:
        pass

    @abc.abstractclassmethod
    def delete_item(self) -> None:
        pass