from userInterface import UserInteractionData
from .abs_user_action import AbsUserAction

class UserActionCancel(AbsUserAction):
        
    @property
    def name(self) -> str:
        return "Cancel"

    @property
    def required_state(self) -> str:
        return ""

    @property
    def next_state(self) -> str:
        return ""
    
    @property
    def sort_priority(self) -> int:
        return 999999
    
    def action(self) -> None:
        print("Closing program")
        self.user_interaction_data.end_interaction = True