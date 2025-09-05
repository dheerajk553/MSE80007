#Parent class: UniversityPerson
class UniversityPerson:
    def __init__(self, name, Address, age, TaxID):
        # Initialize common attributes for all university people
        self.name = name
        self.Address = Address
        self.age = age
        self.TaxID = TaxID

    def show_info(self):
        # Display basic personal information
        print(f"Name: {self.name}")
        print(f"Address: {self.Address}")
        print(f"Age: {self.age}")
        print(f"TaxID: {self.TaxID}")

#Child class: Student (inherits from UniversityPerson)
class Student(UniversityPerson):
    def __init__(self, name, Address, age, TaxID, academic_record):
        # Call the parent class constructor to initialize common attributes
        super().__init__(name, Address, age, TaxID)
        # Initialize student-specific attribute
        self.academic_record = academic_record

    #Method overriding: redefining show_info for Student
    def show_info(self):
        # Optionally call the parent method to reuse its output
        super().show_info()
        # Add student-specific information
        print(f"Academic Record: {self.academic_record}")

 #Main function to run the program
def main():
    # Create a Student object with all required data
    s = Student("Dheeraj Kumar", "Delhi", 29, "DKOPK5597R", "A+")
    print("\n--- Student Details ---")
    # Call the overridden method to display full student info
    s.show_info()

# Program execution starts here
if __name__ == "__main__":
    main()
