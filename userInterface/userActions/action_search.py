from userInterface import UserInteractionData
from .abs_user_action import AbsUserAction

class UserActionSearch(AbsUserAction): 

    @property
    def name(self) -> str:
        return "Search"

    @property
    def required_state(self) -> str:
        return ""

    @property
    def next_state(self) -> str:
        return "Search"
    
    @property
    def sort_priority(self) -> int:
        return -1
    
    def action(self) -> None:
        pass