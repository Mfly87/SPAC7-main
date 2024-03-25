from dataClasses import DataClassFactory
from .abs_user_action import AbsUserAction

from userInterface.user_choice_selector import UserChoiceSelector

class UserActionEdit(AbsUserAction):
        
    @property
    def name(self) -> str:
        return "Edit a search entry"
    
    @property
    def sort_priority(self) -> int:
        return 1

    def is_usable(self) -> bool:
        return self.uid.state == "" and 0 < len(self.uid.prev_search_result)
    
    def execute_action(self) -> None:
        self.uid.state = ""

        print("Please select which entry you wish to edit:")
        
        _max_count = self.uid.max_search_results
        _unique_data_list = self.uid.prev_search_result
        _name_list = [x.to_string() for x in _unique_data_list[0:_max_count]]

        _item_index = UserChoiceSelector.get_user_choice_from_name_list(_name_list)
        _unique_data = _unique_data_list[_item_index]

        print("Please select which field you wish to edit:")

        _field_list = _unique_data.get_headers()

        # Removing one from either end to avoid the ID and Class fields
        _field_list = _field_list[1:len(_field_list)-1]

        _field_index = UserChoiceSelector.get_user_choice_from_name_list(_field_list)
        _field = _field_list[_field_index]

        # We remove 1 initially to avoid the ID field
        _field_index += 1

        _old_value = _unique_data.to_list()[_field_index]

        while(True):
            print("The current value of '%s' is: %s" % (_field, _old_value))
            _new_value = input("Please enter the desired value: ")
            
            __dict = _unique_data.to_dict()
            __dict |= {_field: _new_value}
            _new_unique_data_list = DataClassFactory.create_from_dict(**__dict)

            print("")
            if not _new_unique_data_list:
                print("I'm sorry, the new value was invalid.")
                if "y" in input("Do you wish to try again (y/n)? ").lower():
                    print("")
                    continue
            for _new_unique_data in _new_unique_data_list:
                _unique_data = _new_unique_data
                self.uid.prev_search_result[_item_index] = _new_unique_data
                self.uid.warehouse.mysql_handler.update_item(_unique_data)
                print("Updated item:")
                print(_unique_data.to_string())
            return

