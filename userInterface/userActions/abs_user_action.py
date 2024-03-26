from dataClasses import UniqueData
from userInterface import UserInteractionData
import abc

from userInterface.user_choice_selector import UserChoiceSelector

class AbsUserAction(abc.ABC):
    def __init__(self, user_interaction_data: UserInteractionData) -> None:
        self._user_interaction_data = user_interaction_data

    @property
    def uid(self):
        return self._user_interaction_data

    @abc.abstractclassmethod
    def name(self) -> str:
        pass
    
    @abc.abstractclassmethod
    def sort_priority(self) -> int:
        pass

    @abc.abstractclassmethod
    def is_usable(self) -> bool:
        pass
    
    @abc.abstractclassmethod
    def execute_action(self) -> None:
        pass   

    #@abc.abstractclassmethod
    def action(self) -> None:
        pass