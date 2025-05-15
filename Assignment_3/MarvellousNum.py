def ChkPrime(no1):
    if no1 <= 1:
        # print("Not a Prime Number")
        return False
    for i in range(2, no1):
        if no1 % i == 0:
            # print("Not a Prime Number")
            return False
    # print("It is a Prime Number")
    return True
