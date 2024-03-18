import abc

class UniqueData(abc.ABC):
    def __init__(self, id : str) -> None:
        super().__init__()

        self._id = id

    @property
    def id(self):
        return self._id

    @abc.abstractclassmethod
    def to_string(self):
        pass