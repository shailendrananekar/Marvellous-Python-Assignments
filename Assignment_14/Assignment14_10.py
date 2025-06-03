class Employee:

    def __init__(self, a, b, c):
        self.name = a
        self._department = b
        self.__salary = c


def main():

    emp1 = Employee("Rohit", "IT", 50000)


    print(f"Name: {emp1.name}")

    
    print(f"Department: {emp1._department}")

    
    print(f"Salary: {emp1._Employee__salary}")



if __name__ == "__main__":
    main()
