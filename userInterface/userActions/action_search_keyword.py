from userInterface import UserInteractionData
from .abs_user_action import AbsUserAction

from dataClasses.absDataTypes import UniqueData, UniqueNamedData
from dataClasses import DataClassFactory

class UserActionSearchKeyword(AbsUserAction):

    @property
    def name(self) -> str:
        return "Search using keyword"
    
    @property
    def sort_priority(self) -> int:
        return 0

    def is_usable(self) -> bool:
        return self.uid.state == "search" or self.uid.state == "search_keyword"
    
    def execute_action(self) -> None:
        self.uid.state = ""

        while(True):
            print("Please enter your search")
            print("The MySQL wildcards _ and % will be used.")
            print("")

            _search_string = input("Keyword: ")
            _search_string.strip()
            
            _unique_data_list = self.uid.warehouse.mysql_handler.search_keyword(_search_string)
            self.uid.prev_search_result = _unique_data_list
            
            self.uid.print_search_report()

            if not _unique_data_list:
                _retry = "y" in input("Do you wish to search for another keyword (y/n)?: ").lower()
                if _retry:
                    print("")
                    continue
            break
                