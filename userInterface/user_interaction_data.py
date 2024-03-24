from warehouse import WarhouseMySQL
from dataClasses import UniqueData

class UserInteractionData():

    prev_search_result: list[UniqueData] = []
    end_interaction: bool = False
    state: str = ""

    def __init__(self, warehouse: WarhouseMySQL) -> None:
        self._warehouse = warehouse

    @property
    def warehouse(self) -> WarhouseMySQL:
        return self._warehouse
    
    @property
    def max_search_results(self) -> int:
        return 10
    

    def print_search_report(self) -> None:
        print("")
        if not self.prev_search_result:
            print("I'm sorry, nothing matched your search.")
            return
        else:
            print("Found %i items" % len(self.prev_search_result))
            print("")
            _mini_list = self.prev_search_result[0:self.max_search_results]
            for i, _unique_data in enumerate(_mini_list):
                print(_unique_data.to_string())
                if i % 3 == 2:
                    print("")

            _remaining = len(self.prev_search_result) - len(_mini_list)
            if 0 < _remaining:
                print("...")
                print("and %i more items" % (_remaining))