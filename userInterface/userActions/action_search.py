from .abs_user_action import AbsUserAction

class UserActionSearch(AbsUserAction): 

    @property
    def name(self) -> str:
        return "Search"
    
    @property
    def sort_priority(self) -> int:
        return 0

    def is_usable(self) -> bool:
        return self.uid.state == ""
    
    def execute_action(self) -> None:
        self.uid.state = "search"