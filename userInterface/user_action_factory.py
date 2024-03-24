from inspect import getmembers, isclass, isabstract

from .userActions import AbsUserAction
from . import userActions

from .user_interaction_data import UserInteractionData

class UserActionFactory():
    _actions = {}
        
    def __init__(self) -> None:
        self._load_user_action_classes()

    def _load_user_action_classes(self):
        classes = getmembers(userActions, lambda m: isclass(m) and not isabstract(m) )
        for name, _type in classes:
            if isclass(_type) and issubclass(_type, AbsUserAction):
                self._actions.update([[name, _type]])
    
    def get_all_possible_action_names(self) -> list[str]:
        _list = []
        for action_name in self._actions:
            _list.append(action_name)
        return _list
    
    def get_all_actions(self, user_interaction_data: UserInteractionData) -> list[AbsUserAction]:
        _list = self.get_all_possible_action_names()
        return self.create(_list, user_interaction_data)

    def create(self, action_name_list : list[str], user_interaction_data: UserInteractionData):
        _list : list[AbsUserAction] = []
        for action_name in action_name_list:
            if action_name in self._actions:
                action = self._actions[action_name](user_interaction_data)
                _list.append(action)
        return _list