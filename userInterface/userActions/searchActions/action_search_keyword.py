from .abs_user_search_action import AbsUserSearchAction
from dataClasses.absDataTypes import UniqueNamedData
from my_sql_database import SearchQuerySpecifier

class UserActionSearchKeyword(AbsUserSearchAction):

    @property
    def name(self) -> str:
        return "Search names and descriptions using keyword"
    
    @property
    def sort_priority(self) -> int:
        return 0

    def execute_action(self) -> None:
        self._search_action(
            "keyword:",
            lambda x : SearchQuerySpecifier.get_keyword_specifier(x),
            UniqueNamedData
        )