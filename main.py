from faker import Faker

from dataFaker.abs_faker import AbsFaker

a = AbsFaker()

for _ in range(100):
    print(a.create_last_name())