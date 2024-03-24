from warehouse import AbsWarehouse

class UserInteractionData():

    end_interaction: bool = False

    def __init__(self, warehouse: AbsWarehouse ) -> None:
        self._warehouse = warehouse

    @property
    def warehouse(self) -> AbsWarehouse:
        return self._warehouse
    
    