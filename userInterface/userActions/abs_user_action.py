import abc

class AbsUserAction(abc.ABC):

    @abc.abstractproperty
    def name(self) -> str:
        pass

    @abc.abstractproperty
    def list_priority(self) -> int:
        pass

    @abc.abstractclassmethod
    def is_usable(self, _interaction_dict : dict) -> bool:
        pass

    @abc.abstractclassmethod
    def execute_action(self, _interaction_dict : dict) -> None:
        pass