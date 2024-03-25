from .abs_user_search_action import AbsUserSearchAction
from dataClasses import UniqueData

class UserActionSearchDirectSQL(AbsUserSearchAction):

    @property
    def name(self) -> str:
        return "Search using direct sql"
    
    @property
    def sort_priority(self) -> int:
        return 950

    def execute_action(self) -> None:
        self._search_action(
            "WHERE",
            lambda x : "WHERE %s" % (x),
            UniqueData
        )