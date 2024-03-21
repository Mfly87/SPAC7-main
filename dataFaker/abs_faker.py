import abc
from faker import Faker
from datetime import datetime, date
class AbsFaker(abc.ABC):
    def __init__(self) -> None:
        self._product_id : int = 0
        self._faker : Faker = Faker()

    def set_seed(self, seed : int):
        Faker.seed(seed)

    @abc.abstractproperty
    def id_tag(self):
        pass

    def get_next_id(self) -> str:
        _id = self.id_tag + "-" + str(self._product_id).zfill(6)
        self._product_id += 1
        return _id

    @abc.abstractclassmethod
    def generate_fake_item(self):
        pass
    
    def _create_float(self, min :float, max: float) -> int:
        '''min and max are inclusive'''
        return self._faker.pyfloat(min_value = min, max_value = max)
    
    def _create_int(self, min :int, max: int) -> int:
        '''min and max are inclusive'''
        return self._faker.pyint(min_value = min, max_value = max)

    def _create_sentence(self):
        return self._faker.paragraph(nb_sentences=1)
    
    def _create_transaction_type(self):        
        _transaction = ["Buy", "Sell"] #Return?
        return self._get_rand_item(_transaction)
    
    def _create_date(self) -> date:
        return self._faker.date_between(start_date = "-5y")

    def _create_awesomizer(self):
        _options = []
        _options.append( str(self._faker.century()) )
        _options.append( str(self._create_int(0,9) * 100) )
        _options.append( str(self._create_int(1950,2024)) )
        return self._get_rand_item(_options)

    def _create_last_name(self):
        return self._faker.last_name()

    def _get_rand_item(self, item_list : list):
        _index = self._create_int(0, len(item_list) - 1)
        return item_list[_index]