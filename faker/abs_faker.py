import abc

class AbsFaker(abc.ABC):
    _product_id : int

    @abc.abstractproperty
    def headers(self):
        pass

    @abc.abstractclassmethod
    def get_entry_line(self):
        pass

    