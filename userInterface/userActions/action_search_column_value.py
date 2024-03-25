from .abs_user_action import AbsUserAction
from dataClasses.absDataTypes import UniqueNamedData
from my_sql_database import SearchQuerySpecifier

from userInterface.user_choice_selector import UserChoiceSelector

class UserActioNSearchColumnValue(AbsUserAction):

    @property
    def name(self) -> str:
        return "Search using column values"
    
    @property
    def sort_priority(self) -> int:
        return 1

    def is_usable(self) -> bool:
        return self.uid.state == "search"
    
    def execute_action(self) -> None:
        self.uid.state = ""

        print("Which table do you wish to search?")

        _class_type_name_list = self.uid.warehouse.mysql_handler.get_table_names()
        _class_type_index = UserChoiceSelector.get_user_choice_from_name_list(_class_type_name_list)        
        _class_type_list = self.uid.warehouse.mysql_handler.get_table_types()
        _class_type = _class_type_list[_class_type_index]

        _search_affector = self.get_search_accector(_class_type)
            
        _query_specifier = "WHERE " + _search_affector
        print(_query_specifier)
        
        _unique_data_list = self.uid.warehouse.search_all_tables_of_subclass(_class_type, _query_specifier)
        self.uid.prev_search_result = _unique_data_list
        
        self.uid.print_search_report()

    def get_search_accector(self, _class_type):
        _search_affector = ""
        while True:
            _search_affector += self.get_field_search_affector(_class_type)

            print ("Do you wish to add another specification?")
            _union_descriptions = list(self.unions.values())
            _union_index = UserChoiceSelector.get_user_choice_from_name_list(_union_descriptions)
            
            if _union_index == 0:
                return _search_affector

            _union = list(self.unions.keys())[_union_index]
            _search_affector += _union + " "

    def get_field_search_affector(self, _class_type):

        print("Which field would you like to search?")
        _field_name, _field_index =self._get_unique_data_field_choice(_class_type)
        
        _search_affector = _field_name + " "

        _field_type_list = _class_type.get_types()
        _field_type = _field_type_list[_field_index]
        _field_is_string = isinstance(_field_type, str)

        print("Which opperator would you like to use?")
        _opperator_descriptions = list(self.opperators.values())
        _opperator_index = UserChoiceSelector.get_user_choice_from_name_list(_opperator_descriptions)
        _opperator_description = _opperator_descriptions[_opperator_index]
        _opperator = list(self.opperators.keys())[_opperator_index]

        _search_affector += _opperator + " "

        _input = input("Please which value you wish %s to be %s?: " % (_field_name, _opperator_description.lower()))
        if _field_is_string:
            _input = "'%s'" % (_input)
        
        _search_affector += _input + " "

        return _search_affector


    @property
    def opperators(self) -> dict[str,str]:
        return {
            "=": "Equal",
            ">": "Greater than",
            "<": "Less than",
            ">=": "Greater than or equal",
            "<=": "Less than or equal",
            "<>": "Not equal",
            #"BETWEEN": "Between a certain range",
            #"LIKE": "Search for a pattern",
            #"IN": To specify multiple possible values for a column,
        }
    
    @property
    def unions(self) -> dict[str,str]:
        return {
            "": "No, complete search",
            "OR": "Yes, using the 'OR' opperation",
            "AND": "Yes, using the 'AND' opperation",
        }