# student.py
from university_person import UniversityPerson  #Using 'from' to import
class Student(UniversityPerson):
    def __init__(self, name, address, age, tax_id, academic_record):
        super().__init__(name, address, age, tax_id)
        self.academic_record = academic_record

    def show_info(self):
        super().show_info()
        print(f"Academic Record: {self.academic_record}")

# Main function
def main():
    s = Student("Dheeraj Kumar", "Delhi", 29, "DKOPK5597R", "A+")
    print("\n--- Student Details ---")
    s.show_info()

# Run the program
if __name__ == "__main__":
    main()
