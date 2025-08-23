class EMP:
    def __init__(self, name, salary, job_title):
        self.name = name
        self.salary = salary
        self.jobTitle = job_title

    def display_info(self):
        print(f"Name: {self.name} | Job: {self.jobTitle} | Salary: ${self.salary}")

    def giveraise(self, amount):
        self.salary += amount
        print(f"{self.name} raise of ${amount}. New Salary: ${self.salary}")


def main():
    # Create Two Employees
    emp1 = EMP("Dheeraj", 100000, "Tester")
    emp2 = EMP("Kumar", 4500, "QA")

    # Display Employee's Details
    emp1.display_info()
    emp2.display_info()

    # Give a raise to Both Employee and display updated Salary
    emp1.giveraise(1000)
    emp2.giveraise(1000)
     # Display updated info
    emp1.display_info()
    emp2.display_info()  


if __name__ == "__main__":
    main()