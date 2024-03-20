import abc

class AbsWarehouse(abc.ABC):

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