from .abs_faker import AbsFaker

class FakeProduct(AbsFaker):
    def __init__(self) -> None:
        super().__init__()
    
    def headers(self):
        return [
            "ID",
            "Name",
            "Description",
            "Catagory",
            "Price",
            "Quantity"
        ]

    def generate_entry_line(self):
        _entry = [str(self._product_id)]
        self._product_id += 1

        _catagory = self.create_catagory()

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
