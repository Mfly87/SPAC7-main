from userInterface import UserInteractionData
from .abs_user_action import AbsUserAction

class UserActionNull(AbsUserAction):
        
    @property
    def name(self) -> str:
        return "Null"
    
    @property
    def sort_priority(self) -> int:
        return -1

    def is_usable(self) -> bool:
        return False
    
    def execute_action(self) -> None:
        pass