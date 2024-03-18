import abc
from faker import Faker
from datetime import datetime
class AbsFaker(abc.ABC):
    def __init__(self) -> None:
        self._product_id : int = 0
        self._faker : Faker = Faker()

    def set_seed(seed : int):
        Faker.seed(seed)

    @abc.abstractproperty
    def headers(self):
        pass

    @abc.abstractclassmethod
    def generate_entry_line(self):
        pass

    def create_float(self, min :float, max: float) -> int:
        '''min and max are inclusive'''
        return self._faker.pyfloat(min_value = min, max_value = max)
    
    def create_int(self, min :int, max: int) -> int:
        '''min and max are inclusive'''
        return self._faker.pyint(min_value = min, max_value = max)

    def create_sentence(self):
        return self._faker.paragraph(nb_sentences=1)
    
    def create_transaction_type(self):        
        _transaction = ["Buy", "Sell"] #Return?
        return self._get_rand_item(_transaction)
    
    def create_date(self) -> datetime:
        return self._faker.date_between(start_date = "-5y")

    def create_awesomizer(self):
        _options = []
        _options.append( str(self._faker.century()) )
        _options.append( str(self.create_int(0,9) * 100) )
        _options.append( str(self.create_int(1850,2024)) )
        return self._get_rand_item(_options)

    def create_last_name(self):
        return self._faker.last_name()

    def create_catagory(self):        
        _catagories = [
            "Refrigerator",
            "Oven",
            "Air fryer",
            "Microwave",
            "Dishwasher",
            "Washing machine",
            "Dryer",
            "Vacuum cleaner",
            "Air conditioner",
            "Heater",
            "Iron",
            "Blender",
            "Toaster",
            "Coffee maker",
            "Kettle",
            "Electric fan"
        ]
        return self._get_rand_item(_catagories)
    
    def _get_rand_item(self, item_list : list):
        _index = self.create_int(0, len(item_list) - 1)
        return item_list[_index]