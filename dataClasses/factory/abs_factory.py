import abc

from ..absDataTypes import UniqueData

class AbsFactory(abc.ABC):

    def create_variant(self, ud: UniqueData, ud_variations_dict: dict[str,str]) -> list[UniqueData]:
        _dict = ud.to_dict()
        for _key in ud_variations_dict:
            _changed_value = ud_variations_dict[_key]
            _dict |= {_key: _changed_value}
        return self.create_from_dict(_dict)

    def _ud_to_valid_list(self, ud: UniqueData) -> list[UniqueData]:
        _dict = ud.__dict__
        for _value in _dict.values():
            if _value is None:
                return []
        return [ud]
    
    @abc.abstractclassmethod
    def create(self) -> list[UniqueData]:
        ...

        