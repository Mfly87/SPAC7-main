from userInterface.user_interaction import UserInteraction
from warehouse.absWarehouse import WarehouseOOP

#user_interaction = UserInteraction()
#user_interaction.start_interation()

_wh = WarehouseOOP[int](
    lambda x : str(x),
    lambda x, search_str : str(x) == search_str
)

_wh.update_item(42)
_wh.update_item(26)
_wh.update_item("B")
_wh.update_item(32)
_list = _wh.get_items(["B"])
print(len(_list))