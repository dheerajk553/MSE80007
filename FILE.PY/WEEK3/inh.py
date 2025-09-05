# Parent class: UniversityPerson
class UniversityPerson:
    def __init__(self, name, Address, age, TaxID):
        self.name = name
        self.Address = Address
        self.age = age
        self.TaxID = TaxID

    def show_info(self):
        print(f"Name: {self.name}")
        print(f"Address: {self.Address}")
        print(f"Age: {self.age}")
        print(f"TaxID: {self.TaxID}")

# Child class: Student
class Student(UniversityPerson):
    def __init__(self, name, Address, age, TaxID, academic_record):
        super().__init__(name, Address, age, TaxID)
        self.academic_record = academic_record

    def show_student_info(self):
        self.show_info()
        print(f"Academic Record: {self.academic_record}")

# Main function
def main():
    s = Student("Dheeraj Kumar", "Delhi", 29, "DKOPK5597R", "A+")
    print("\n--- Student Details ---")
    s.show_student_info()

# Program starts here
if __name__ == "__main__":
    main()
