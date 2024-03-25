from .abs_user_action import AbsUserAction

class UserActionCancel(AbsUserAction):
        
    @property
    def name(self) -> str:
        return "Cancel"
    
    @property
    def sort_priority(self) -> int:
        return 999999

    def is_usable(self) -> bool:
        return self.uid.state != ""
    
    def execute_action(self) -> None:
        self.uid.state = ""