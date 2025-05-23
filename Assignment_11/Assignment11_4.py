count = 1

res =1

def power(x, n):
    
    global count,res
    if count <= n:
    # while count <= n:  # normal Iteration
        res = res * x
        count = count + 1
        power(x,n)  # recursion
    return res


def main():
    res = power(2, 3)
    print("power :", res)


if __name__ == "__main__":
    main()
