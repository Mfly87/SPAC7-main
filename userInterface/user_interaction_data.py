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
    