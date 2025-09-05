# Class to represent a university person

class UniversityPerson:
    def __init__(self, name, address, age, tax_id):
        self.name = name
        self.address = address
        self.age = age
        self.tax_id = tax_id

    def greet(self):
        print(f"Hello! My name is {self.name}. I am part of the university system.")

    def show_info(self):
        print(f"Name: {self.name}")
        print(f"Address: {self.address}")
        print(f"Age: {self.age}")
        print(f"TaxID: {self.tax_id}")

