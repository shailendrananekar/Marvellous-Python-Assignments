class BankAccount:
    ROI = 10.5

    def __init__(self):
        self.Name = input("Enter the name of the account holder: ")
        self.Amount = int(input("Enter the amount : "))

    def Display(self):
        print(f"Account Holder Name: {self.Name}")
        print(f"Current Balance: {self.Amount}")
        print(f"Rate of Interest: {BankAccount.ROI}%")

    def Deposit(self):
        amt = int(input("Enter the amount to be deposited: "))
        self.Amount = self.Amount + amt

    def Withdraw(self):
        wit = int(input("Enter the amount to be withdrawn: "))
        self.Amount = self.Amount - wit

    def CalculateInterest(self):
        years = 1
        interest = (self.Amount * BankAccount.ROI * years) / 100
        print(f"Interest earned over {years} year: {interest}")


def main():
    account = BankAccount()
    account.Display()

    account.Deposit()
    print(f"New Balance: {account.Amount}")

    account.Withdraw()
    print(f"New Balance: {account.Amount}")

    account.CalculateInterest()


if __name__ == "__main__":
    main()
