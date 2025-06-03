class Employee:

    def __init__(self, a, b, c):
        self.name = a
        self.emp_id = b
        self.salary = c

    def Display(self):
        print(f"Name: {self.name}, ID: {self.emp_id}, Salary: {self.salary}")


def main():
    emp1 = Employee("Rohit", 101, 50000)

    emp1.Display()


if __name__ == "__main__":
    main()
