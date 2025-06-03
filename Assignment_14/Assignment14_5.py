class BankAccount:

    def __init__(self, a, b, c):
        self.account_number = a
        self.name = b
        self.balance = c

    def deposit(self, amount):
        self.balance = self.balance + amount
        return self.balance

    def withdraw(self, amount):
        self.balance = self.balance - amount
        return self.balance

    def display(self):
        print(f"Balance: {self.balance}")


def main():

    bankaccount1 = BankAccount(123456, "John Doe", 1000)
    bankaccount1.display()
    bankaccount1.deposit(500)
    print(f"Balance after deposit: {bankaccount1.balance}")
    bankaccount1.withdraw(200)
    print(f"Balance after withdrawal: {bankaccount1.balance}")


if __name__ == "__main__":
    main()
