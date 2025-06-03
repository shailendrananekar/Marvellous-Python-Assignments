class Person:

    def __init__(self, a, b):
        self.name = a
        self.age = b


class Teacher(Person):

    def __init__(self, c, d, e, f):
        self.subject = c
        self.salary = d

        super().__init__(e, f)  # Call the constructor of the Person class

    def Display(self):
        print(
            f"Name: {self.name}, Age: {self.age}, Subject: {self.subject}, Salary: {self.salary}"
        )


def main():

    teacher1 = Teacher("Mathematics", 60000, "Alice", 30)

    teacher1.Display()


if __name__ == "__main__":
    main()
