def Add(no1, no2):
    addition_result = 0
    addition_result = no1 + no2
    return addition_result


def Sub(no1, no2):
    subtraction_result = 0
    subtraction_result = no1 - no2
    return subtraction_result


def Mult(no1, no2):
    multiplication_result = 0
    multiplication_result = no1 * no2
    return multiplication_result


def Div(no1, no2):
    division_result = 0
    if no2 == 0:
        print("Division by zero is not allowed.")
        return None
    else:
        division_result = no1 / no2
    return division_result
