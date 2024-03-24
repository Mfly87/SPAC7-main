from .abs_user_action import AbsUserAction

class UserActionCancel(AbsUserAction):

    @property
    def name(self) -> str:
        return "Close"
    
    @property
    def list_priority(self) -> int:
        return -1

    def is_usable(self, _interaction_dict : dict) -> bool:
        return True

    def execute_action(self, _interaction_dict : dict) -> None:
        print("Closing program")
        _interaction_dict["end_interaction"] = True