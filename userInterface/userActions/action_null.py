from userInterface import UserInteractionData
from .abs_user_action import AbsUserAction

class UserActionNull(AbsUserAction):
        
    @property
    def name(self) -> str:
        return "Null"

    @property
    def required_state(self) -> str:
        return "Null"

    @property
    def next_state(self) -> str:
        return ""
    
    @property
    def sort_priority(self) -> int:
        return -1
    
    def action(self) -> None:
        print("Performed null action")