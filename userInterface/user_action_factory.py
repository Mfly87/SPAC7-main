from inspect import getmembers, isclass, isabstract

from .userActions import AbsUserAction
from . import userActions

class UserActionFactory():
    _actions = {}
        
    def __init__(self) -> None:
        self._loadProducts()

    def _loadProducts(self):
        classes = getmembers(userActions, lambda m: isclass(m) and not isabstract(m) )
        
        for name, _type in classes:
            if isclass(_type) and issubclass(_type, AbsUserAction):
                self._actions.update([[name, _type]])
    
    def get_list_of_possible_actions(self) -> list[str]:
        _list = []
        for action_name in self._actions:
            _list.append(action_name)
        return _list
    
    def get_all_actions(self) -> list[AbsUserAction]:
        _list = self.get_list_of_possible_actions()
        return self.create(_list)

    def create(self, action_name_list : list[str]):
        _list : list[AbsUserAction] = []
        for action_name in action_name_list:
            if action_name in self._actions:
                action = self._actions[action_name]()
                _list.append(action)

        _list = sorted(_list, key = lambda x: x.list_priority)
        return _list