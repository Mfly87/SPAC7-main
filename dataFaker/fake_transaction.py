from .abs_faker import AbsFaker
from datetime import datetime

from dataClasses import DataClassFactory
from dataClasses.dataTypes import Product
from dataClasses.dataTypes import Transaction

class FakeTransaction(AbsFaker):
    @property
    def id_tag(self):
        return "Tran"
    
    def generate_fake_item(self, product : Product) -> Transaction:
        _factory = DataClassFactory()
        
        _tansaction_amount = self._create_non_zero_transaction_amount()
        
        return _factory.create_transaction(
            self.get_next_id(),
            product,
            self._create_date(),
            _tansaction_amount,
            "Sell" if _tansaction_amount < 0 else "Buy"
        )
    
    def _create_non_zero_transaction_amount(self) -> int:
        _value = 0
        while (_value == 0):
            for _ in range(3):
                _value += self._create_int(-3,3)
        return _value