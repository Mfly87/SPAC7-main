from ..abs_user_action import AbsUserAction
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
            
            self._print_search_report()

            if not _unique_data_list:
                _retry = "y" in input("Do you wish to try again (y/n)?: ").lower()
                if _retry:
                    print("")
                    continue
            break
                

    def _print_search_report(self) -> None:
        print("")
        if not self.uid.prev_search_result:
            print("I'm sorry, nothing matched your search.")
            return
        else:
            print("Found %i items" % len(self.uid.prev_search_result))
            print("")
            _mini_list = self.uid.prev_search_result[0:self.uid.max_search_results]
            for i, _unique_data in enumerate(_mini_list):
                if 0 < i and i % 3 == 0:
                    print("")
                print(_unique_data.to_string())

            _remaining = len(self.uid.prev_search_result) - len(_mini_list)
            if 0 < _remaining:
                print("...")
                print("and %i more items" % (_remaining))