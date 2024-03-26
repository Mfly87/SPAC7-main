from .abs_user_search_action import AbsUserSearchAction
from dataClasses import UniqueData
from my_sql_database import SearchQuerySpecifier

class UserActionSearchID(AbsUserSearchAction):

    @property
    def name(self) -> str:
        return "Search by id"
    
    @property
    def sort_priority(self) -> int:
        return -1

    def execute_action(self) -> None:
        self._search_action(
            "id:",
            lambda x : SearchQuerySpecifier.get_like_specifier("id",x),
            UniqueData
        )