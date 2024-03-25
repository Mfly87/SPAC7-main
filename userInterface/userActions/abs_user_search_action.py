from .abs_user_action import AbsUserAction
from dataClasses.absDataTypes import UniqueData
from my_sql_database import SearchQuerySpecifier

from typing import Callable

class AbsUserSearchAction(AbsUserAction):

    def is_usable(self) -> bool:
        return self.uid.state == "search"
    
    def _search_action(self,
                       user_prompt: str,
                       query_func: Callable[[str],str],
                       table_subclass: UniqueData,
                       ) -> None:
        self.uid.state = ""

        while(True):
            print("Please enter your search")
            print("The MySQL wildcards _ and % will be used.")
            print("")

            _search_string = input("%s " % user_prompt)
            _search_string.strip()
            
            _query_specifier = query_func(_search_string)
            _unique_data_list = self.uid.warehouse.search_all_tables_of_subclass(table_subclass, _query_specifier)
            self.uid.prev_search_result = _unique_data_list
            
            self.uid.print_search_report()

            if not _unique_data_list:
                _retry = "y" in input("Do you wish to try again (y/n)?: ").lower()
                if _retry:
                    print("")
                    continue
            break
                