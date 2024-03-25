from .abs_user_action import AbsUserAction
from dataClasses.absDataTypes import UniqueNamedData
from my_sql_database import SearchQuerySpecifier

class UserActionSearchDirectSQL(AbsUserAction):

    @property
    def name(self) -> str:
        return "Search using direct sql"
    
    @property
    def sort_priority(self) -> int:
        return 950

    def is_usable(self) -> bool:
        return self.uid.state == "search"
    
    def execute_action(self) -> None:
        self.uid.state = ""

        while(True):
            print("Please enter your search")
            print("The MySQL wildcards _ and % will be used.")
            print("")

            _search_string = input("WHERE ")
            _search_string.strip()

            _unique_data_list = self.uid.warehouse.search_all_tables(_search_string)
            self.uid.prev_search_result = _unique_data_list
            
            self.uid.print_search_report()

            if not _unique_data_list:
                _retry = "y" in input("Do you wish to perform another search (y/n)?: ").lower()
                if _retry:
                    print("")
                    continue
            break
                