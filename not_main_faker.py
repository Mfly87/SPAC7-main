from dataFaker import FakeCategory
from dataFaker import FakeProduct
from dataFaker import FakeTransaction

def fake_main():
    _product_factory = FakeProduct()
    _category_factory = FakeCategory()
    _transaction_factory = FakeTransaction()
    _product_factory.set_seed(0)

    _category_list = _category_factory.generate_fake_item_list()
    for _ in range(10):
        _product = _product_factory.generate_fake_item_from_category_list(_category_list)
        print(_product.to_string())

    for _ in range(10):
        _transaction = _transaction_factory.generate_fake_item(_product)
        print(_transaction.to_string())

if __name__ == "main":
    fake_main()