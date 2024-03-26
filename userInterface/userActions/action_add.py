'''

from .abs_user_action import AbsUserAction
from dataClasses import UniqueData
from dataClasses.factory import DataClassFactory

from ..user_choice_selector import UserChoiceSelector
from my_sql_database.search_query_specifier import SearchQuerySpecifier

class UserActionAdd(AbsUserAction):
        
    @property
    def name(self) -> str:
        return "Add item"
    
    @property
    def sort_priority(self) -> int:
        return 100

    def is_usable(self) -> bool:
        return self.uid.state == ""
    
    def execute_action(self) -> None:

        _table_types: list[UniqueData | type] = self.uid.warehouse.mysql_handler.get_table_types()
        _type_name_list = [_type.__name__ for _type in _table_types] + ["Cancel"]
        _type_index = UserChoiceSelector.get_user_choice_from_name_list(_type_name_list)

        if _type_index == len(_type_name_list)-1:
            return

        _type_selected = _table_types[_type_index]

        _dict = {"class": "'%s'" % (_type_selected.__name__)}
        for _field in _type_selected.get_headers():
            if _field in _dict.keys():
                continue
            
            _input = input("%s: " % (_field)).strip()
            _input = "'%s'" % (_input)
            print("")
            _dict |= {_field: _input}

            if not self._is_dependency(_field):
                continue
            
            _table_name = _field.split("_")[0]
            _query_specifier = SearchQuerySpecifier.get_identical_specifier("id", _input)
            _data_list = self.uid.warehouse.search_table(_table_name, query_specifier = _query_specifier)

            if not _data_list:
                print("No valid ID match in the database.")
                print("Terminating procedure.")
                return
            
        for _unique_data in DataClassFactory.create_from_dict(**_dict):
            self.uid.warehouse.add_item(_unique_data)
            print("Added item:")
            print(_unique_data.to_string())



    def _is_dependency(self, _string: str) -> bool:
        _split = _string.split("_")
        if len(_split) != 2:
            return False
        return _split[1] == "id"

                







    def _unused(self):

        _types_in_search: set[str] = set()

        _max_count = self.uid.max_search_results
        _limited_search = self.uid.prev_search_result[0:_max_count]
        for _unique_data in _limited_search:
            _types_in_search.add(_unique_data.__class__.__name__.lower())

        _table_types: list[UniqueData | type] = self.uid.warehouse.mysql_handler.get_table_types()
        _valid_types: list[UniqueData | type] = []
        
        for _type in _table_types:
            _valid = True
            for _dependency in _type.get_dependencies():
                if _dependency in _types_in_search:
                    continue
                _valid = False
                print("Can't create '%s' due to missing '%s' in the last %i search results" % (_type.__name__, _dependency, _max_count))
                break
            if _valid:
                _valid_types.append(_type)

        print("Which type do you wish to add?")

        _type_name_list = [_type.__name__ for _type in _valid_types] + ["Cancel"]
        _type_index = UserChoiceSelector.get_user_choice_from_name_list(_type_name_list)

        if _type_index == len(_type_name_list)-1:
            return

        _type_selected = _valid_types[_type_index]

        print(_type_selected)



'''