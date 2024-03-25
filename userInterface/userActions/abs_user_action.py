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


    
    def _get_unique_data_field_choice(self, unique_data: UniqueData) -> tuple[str,int]:
        _field_list = unique_data.get_headers()

        # Removing one from either end to avoid the ID and Class fields
        _field_list = _field_list[1:len(_field_list)-1]

        _field_index = UserChoiceSelector.get_user_choice_from_name_list(_field_list)
        _field_name = _field_list[_field_index]

        # We remove 1 initially to avoid the ID field
        _field_index += 1

        return _field_name, _field_index