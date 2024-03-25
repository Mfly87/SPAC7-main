from .abs_user_action import AbsUserAction
from dataClasses.absDataTypes import UniqueNamedData
from my_sql_database import SearchQuerySpecifier

class UserActionSearchKeyword(AbsUserAction):

    @property
    def name(self) -> str:
        return "Search using keyword"
    
    @property
    def sort_priority(self) -> int:
        return 0

    def is_usable(self) -> bool:
        return self.uid.state == "search"
    
    def execute_action(self) -> None:
        self.uid.state = ""

        while(True):
            print("Please enter your search")
            print("The MySQL wildcards _ and % will be used.")
            print("")

            _search_string = input("Keyword: ")
            _search_string.strip()
            
            _query_specifier = SearchQuerySpecifier.get_keyword_specifier(_search_string)
            _unique_data_list = self.uid.warehouse.search_all_tables_of_subclass(UniqueNamedData, _query_specifier)
            self.uid.prev_search_result = _unique_data_list
            
            self.uid.print_search_report()

            if not _unique_data_list:
                _retry = "y" in input("Do you wish to search for another keyword (y/n)?: ").lower()
                if _retry:
                    print("")
                    continue
            break
                