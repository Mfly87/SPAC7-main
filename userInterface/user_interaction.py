from .user_action_factory import UserActionFactory
from .user_choice_selector import UserChoiceSelector

from warehouse import AbsWarehouse

class UserInteraction():

    def __init__(self, warehouse : AbsWarehouse) -> None:
        self._interaction_dict : dict = dict()
        self._interaction_dict |= {"warehouse": warehouse}        

    def start_interation(self):
        self.interaction_loop()
    
    def interaction_loop(self):
        self._interaction_dict["end_interaction"] = False

        _action_factory = UserActionFactory()
        _choice_factory = UserChoiceSelector()
        
        while (True):
            _action_list = _action_factory.create_list_of_all()
            _valid_action_list = []
            for _action in _action_list:
                if _action.is_usable(self._interaction_dict):
                    _valid_action_list.append(_action)
                
            _index = _choice_factory.get_user_choice_from_objects(_valid_action_list, lambda x : x.name, null_choice = "Abort")
            
            if _index < 0:
                return
            
            _action = _valid_action_list[_index]
            _action.execute_action(self._interaction_dict)

            if self._interaction_dict.get("end_interaction", False):
                return
