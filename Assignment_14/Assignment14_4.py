class Student:
    global school_name

    def __init__(self, a, b,c):
        self.name = a
        self.roll_no = b
        Student.school_name = c

    def Display(self):
        print(f"Name: {self.name}, Roll No: {self.roll_no}, School Name: {Student.school_name}")


def main():
    # global school_name
    # school_name = "ABC High School"

    student1 = Student("John Doe", 123,"Atha")

    student1.Display()


if __name__ == "__main__":
    main()
