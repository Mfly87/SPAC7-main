from faker import Faker

from dataFaker.fake_product import FakeProduct

a = FakeProduct()

for _ in range(100):
    print(a.generate_fake_item())