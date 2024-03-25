from .abs_user_action import AbsUserAction

class UserActionClose(AbsUserAction):
        
    @property
    def name(self) -> str:
        return "Close program"
    
    @property
    def sort_priority(self) -> int:
        return 999999

    def is_usable(self) -> bool:
        return self.uid.state == ""
    
    def execute_action(self) -> None:
        print("Closing program")
        print("\n\n")
        self.uid.end_interaction = True