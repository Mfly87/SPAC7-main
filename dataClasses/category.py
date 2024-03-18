class Category():
    def __init__(self, id : str, name : str, description : str) -> None:
        self._id : str = id
        self._name : str = name
        self._description : str = description

    @property
    def id(self) -> str:
        return self._id
    
    @property
    def name(self) -> str:
        return self._name
    
    @property
    def description(self) -> str:
        return self._description