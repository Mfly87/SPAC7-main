class SearchQuerySpecifier():

    @staticmethod
    def get_keyword_specifier(search_string: str) -> str:
        return f"WHERE name LIKE '%{search_string}%' OR description LIKE '%{search_string}%'"
    
    @staticmethod
    def get_identical_specifier(column_name: str, value: str) -> str:
        return "WHERE %s='%s'" % (column_name, value)
    
    @staticmethod
    def get_like_specifier(column_name: str, value: str) -> str:
        return f"WHERE {column_name} LIKE '%{value}%'"