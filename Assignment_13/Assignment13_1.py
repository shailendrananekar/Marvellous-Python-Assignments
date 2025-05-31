class BookStore:
    NoOfBooks = 0

    def __init__(self):
        self.Name = input("Enter the name of the book: ")
        self.Author = input("Enter the author of the book: ")
        BookStore.NoOfBooks = BookStore.NoOfBooks + 1

    def Display(self):
        print(f"Book Name: {self.Name}")
        print(f"Author: {self.Author}")
        print(f"Total Books: {BookStore.NoOfBooks}")


def main():
    Obj1 = BookStore()
    Obj1.Display()

    Obj2 = BookStore()
    Obj2.Display()


if __name__ == "__main__":
    main()
