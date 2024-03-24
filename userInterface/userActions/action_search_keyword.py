from userInterface import UserInteractionData
from .abs_user_action import AbsUserAction

from dataClasses import UniqueData

class UserActionSearchKeyword(AbsUserAction):

    @property
    def name(self) -> str:
        return "Search using keyword"

    @property
    def required_state(self) -> str:
        return "Search"

    @property
    def next_state(self) -> str:
        return ""
    
    @property
    def sort_priority(self) -> int:
        return -1
    
    def action(self) -> None:
        print("Please enter your search")
        print("The MySQL wildcards _ and % will be used.")
        print("")

        _input = input("Keyword: ")
        _input.strip()
        
        _unique_data_list = self.user_interaction_data.warehouse.search_item(_input)
        self._print_search_report(_unique_data_list)

        
    def _print_search_report(self, _unique_data_list: list[UniqueData]) -> None:
        print("")
        if not _unique_data_list:
            print("I'm sorry, nothing matched your search.")
            return
        else:
            print("Found %i items" % len(_unique_data_list))
            for _unique_data in _unique_data_list:
                print(_unique_data.to_string())