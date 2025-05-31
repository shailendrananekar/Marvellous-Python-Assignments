class Numbers:
    def __init__(self):
        self.value = int(input("Enter a number: "))

    def ChkPrime(self):
        if self.value <= 1:
            print(f"{self.value} is not a prime number.")
            return False
        for i in range(2, int(self.value)):
            if self.value % i == 0:
                print(f"{self.value} is not a prime number.")
                return False
        print(f"{self.value} is a prime number.")
        return True

    def ChkPerfect(self):
        if self.SumFactors() == self.value:
            print(f"{self.value} is a perfect number.")
        else:
            print(f"{self.value} is not a perfect number.")
        return True

    def SumFactors(self):
        sum_of_factors = 0
        for i in range(1, self.value):
            if self.value % i == 0:
                sum_of_factors = sum_of_factors + i
        print(f"The sum of factors of {self.value} is {sum_of_factors}.")
        return sum_of_factors

    def Factors(self):
        factors = []
        for i in range(1, self.value + 1):
            if self.value % i == 0:
                factors.append(i)
        print(f"The factors of {self.value} are: {factors}.")
        return factors


def main():
    num = Numbers()
    num.ChkPrime()
    num.ChkPerfect()
    num.SumFactors()
    num.Factors()


if __name__ == "__main__":
    main()
