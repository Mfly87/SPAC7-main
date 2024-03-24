from .user_action_factory import UserActionFactory
from .user_choice_selector import UserChoiceSelector
from userActions import AbsUserAction

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
        _choice_factory = UserChoiceSelector()
        
        while (True):
            _action_list = self._get_usable_actions()
            _action_to_name_func: Callable[[AbsUserAction],str] = lambda x : x.name
            _index = _choice_factory.get_user_choice_from_objects(
                _action_list, 
                _action_to_name_func,
                null_choice = "Cancel"
                )
            
            if _index < 0:
                return
            
            _action = _action_list[_index]
            _action.execute_action(self.user_interaction_data)

            if self.user_interaction_data.end_interaction:
                return

    def _get_usable_actions(self) -> list[AbsUserAction]:
        _action_list = []
        for _action in self.action_factory.get_all_actions():
            if _action.is_usable(self.user_interaction_data):
                _action_list.append(_action)
        return _action_list