from .abs_user_action import AbsUserAction

class UserActionCancel():

    @property
    def name(self) -> str:
        return "Cancel"
    
    @property
    def list_priority(self) -> int:
        return -1

    def is_usable(self) -> bool:
        return True

    def execute_action(self) -> None:
        print("Cancelled!")