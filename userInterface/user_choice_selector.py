from typing import Callable, TypeVar

T = TypeVar("T")

class UserChoiceSelector():
    
    @staticmethod
    def get_user_choice_from_objects(objects: list[T], obj_to_str_func: Callable[[T],str], *, null_choice: str = "") -> int:
        _name_list: list[str] = []

        if null_choice:
            _name_list.append(null_choice)

        for _object in objects:
            _name = obj_to_str_func(_object)
            _name_list.append(_name)
        
        _index = UserChoiceSelector.get_user_choice_from_name_list(_name_list)
        _offset = 1 if null_choice else 0
        return _index -_offset

    @staticmethod
    def get_user_choice_from_name_list(choice_name_list : list[str]) -> int:
        if not choice_name_list:
            print("There were no selection options")
            return -1

        _index = UserChoiceSelector._get_choice_index(choice_name_list)
        print("You have selected: (" + str(_index) + ") " + choice_name_list[_index])
        print("")
        return _index

    @staticmethod
    def _get_choice_index(choice_name_list : list[str]) -> int:
        while (True):
            print("")
            print("You have the following options:")

            for i, _choice in enumerate(choice_name_list):
                print("(" + str(i) + ") " + _choice)
                if i % 3 == 2:
                    print("")

            while(True):
                print("")
                _input = input("Please make a selection: ")
                _input = _input.strip()

                _input_lower = _input.lower()
                for i, _choice in enumerate(choice_name_list):
                    if _input_lower == _choice.lower():
                        return i
                    
                _value = UserChoiceSelector._attempt_to_get_an_int(_input)
                if 0 <= _value and _value < len(choice_name_list):
                    return _value
                
                print("Invalid selection.")

    @staticmethod
    def _attempt_to_get_an_int(_input : str):
        try:
            _value = int(_input)
        except:
            return -1
        return _value
