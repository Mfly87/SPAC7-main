from .user_action_factory import UserActionFactory
from .user_choice_selector import UserChoiceSelector

class UserInteraction():
    
    def start_interation(self):
        self.interaction_loop()
    
    def interaction_loop(self):
        _action_factory = UserActionFactory()
        _choice_factory = UserChoiceSelector()
        
        while (True):
            _action_list = _action_factory.create_list_of_all()
            _index = _choice_factory.get_user_choice_from_objects(_action_list, lambda x : x.name, null_choice = "Abort")
            
            if _index < 0:
                return
            
            _action = _action_list[_index]
            _action.execute_action()
