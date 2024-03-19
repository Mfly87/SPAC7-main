import abc

class UniqueData(abc.ABC):
    def __init__(self, id : str) -> None:
        super().__init__()

        self._id = id

    @property
    def id(self) -> str:
        return self._id
    
    @abc.abstractclassmethod
    def to_string(self) -> str:
        pass

    @abc.abstractclassmethod
    def to_dict(self) -> dict[str,str]:
        pass

    def matches_search(self, search_string : str) -> bool:
        if (search_string in self.id):
            return True
        return False