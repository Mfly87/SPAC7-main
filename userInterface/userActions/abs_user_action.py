from userInterface import UserInteractionData
import abc

class AbsUserAction(abc.ABC):
    def __init__(self, user_interaction_data: UserInteractionData) -> None:
        self._user_interaction_data = user_interaction_data

    @property
    def user_interaction_data(self):
        return self._user_interaction_data

    @abc.abstractproperty
    def name(self) -> str:
        pass

    @abc.abstractproperty
    def required_state(self) -> str:
        pass

    def is_usable(self) -> bool:
        return self.user_interaction_data.state == self.required_state

    @abc.abstractproperty
    def next_state(self) -> str:
        pass
    
    @abc.abstractproperty
    def sort_priority(self) -> int:
        pass
    
    def execute_action(self):
        self.action()
        self.user_interaction_data.state = self.next_state    

    @abc.abstractclassmethod
    def action(self) -> None:
        pass