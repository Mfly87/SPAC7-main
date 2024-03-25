from .abs_faker import AbsFaker
from datetime import datetime

from dataClasses.factory import DataClassFactory
from dataClasses.dataTypes import Product
from dataClasses.dataTypes import Transaction

class FakeTransaction(AbsFaker):
    @property
    def id_tag(self):
        return "Tran"
    
    def generate_fake_item_from_product_list(self, product_list : list[Product]) -> list[Transaction]:
        _product : Product = self._get_rand_item(product_list)
        return self.generate_fake_item(_product)
    
    def generate_fake_item(self, product : Product) -> list[Transaction]:
        _factory = DataClassFactory()
        _tansaction_amount = self._create_non_zero_transaction_amount(product)
        _params = [
            self.get_next_id(),
            product.id,
            self._create_date(),
            _tansaction_amount,
            "Sell" if _tansaction_amount < 0 else "Buy"
        ]
        return _factory.create_transaction(*_params)
    
    def _create_non_zero_transaction_amount(self, product : Product) -> int:
        _prev_value = product.quantity
        while product.quantity == _prev_value:
            for _ in range(3):
                product.quantity += self._create_int(-3,3)
        return product.quantity - _prev_value