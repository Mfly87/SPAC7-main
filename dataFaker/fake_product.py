from .abs_faker import AbsFaker

class FakeProduct(AbsFaker):
    @property
    def id_tag(self):
        return "Prod"
    
    def generate_fake_item(self):
        _entry = ["Prod-" + str(self._product_id).zfill(6)]
        self._product_id += 1

        _catagory = self.create_category()

        _entry.append(self.generate_product_name(_catagory))
        _entry.append(self.create_sentence())
        _entry.append(_catagory)
        _entry.append(str(self.create_int(6,60)*50 - 1))
        _entry.append(str(self.create_int(0,50)))

        return _entry


    def generate_product_name(self, catagory : str):
        return " ".join([
            self.create_last_name(),
            catagory,
            self.create_awesomizer()
        ])
