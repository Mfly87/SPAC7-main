from .user_action_factory import UserActionFactory
from .user_choice_selector import UserChoiceSelector
from .user_interaction_data import UserInteractionData
from .userActions.abs_user_action import AbsUserAction

from warehouse import AbsWarehouse
from .user_interaction_data import UserInteractionData

from typing import Callable

class UserInteraction():

    def __init__(self, warehouse : AbsWarehouse) -> None:
        self._user_interaction_data = UserInteractionData(warehouse)
        self._action_factory = UserActionFactory()

    @property
    def user_interaction_data(self) -> UserInteractionData:
        return self._user_interaction_data
    
    @property
    def action_factory(self) -> UserActionFactory:
        return self._action_factory

    def start_interation(self):
        self.interaction_loop()
    
    def interaction_loop(self):        
        while (True):
            _user_action = self._get_user_action()
            if _user_action is None:
                return
            
            _user_action.execute_action()

            if self.user_interaction_data.end_interaction:
                return

    def _get_user_action(self) -> AbsUserAction | None:
        _action_list = self._get_action_list()
        _action_to_name_func: Callable[[AbsUserAction],str] = lambda x : x.name
        _index = UserChoiceSelector.get_user_choice_from_objects(
            _action_list, 
            _action_to_name_func
            )
        
        if _index < 0:
            return None
        
        return _action_list[_index]        

    def _get_action_list(self) -> list[AbsUserAction]:
        _action_list: list[AbsUserAction] = []
        for _action in self.action_factory.get_all_actions(self.user_interaction_data):
            if _action.is_usable():
                _action_list.append(_action)
        
        _action_list = sorted(_action_list, key = lambda x: (x.sort_priority, x.name))
        return _action_list