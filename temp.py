from dataClasses.dataTypes import Category

from my_sql_database import QueryGenerator

_a = Category("abc","abc","abc")

_gen = QueryGenerator()



#print(_gen.generate_table_for_class(Category))
#print(_gen.generate_insertion_query(_a))