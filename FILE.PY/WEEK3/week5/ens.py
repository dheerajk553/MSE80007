class Student:
    def __init__(self, name, age, address_obj):
        self.name = name # Public attribute
        self.age = age # Public attribute
        self.__grade = 'A'# Private attribute
        self.__address = address_obj  # private reference to Address object
    def get_grade(self):
        return self.__grade
        def updated_info(self):
            self._grade = 'A+'
    def get_address(self):
        return self.__address.get_full_address()
class Address:
    def __init__(self, street, city, zipcode):
        self.__street = street
        self.__city = city
        self.__zipcode = zipcode
    def get_full_address(self):
        return f"{self.__street}, {self.__city}, {self.__zipcode}"
# Object creation
addr = Address("123 Queen St", "Auckland", "1041")
student1 = Student("Dheeraj Kumar", 29, addr)
print(student1.name)           # Public attribute
print(student1.age)            # Public attribute
print(student1.get_grade())    # Private attribute via method
print(student1.get_address())  # Address via method
student1.updated_info()        # Grade upgraded
print("After update:", student1.get_grade())   