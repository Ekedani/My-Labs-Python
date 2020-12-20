def func_g(param):
    sum_n, sum_d = 0, 0
    for k in range(0,11):
        num_n = param**(2*k + 1)
        den_n = factorial(2*k + 1)
        sum_n = sum_n + num_n / den_n
    for k in range(0,11):
        num_d = param**(3*k)
        den_d = factorial(3*k)
        sum_d = sum_d + num_d / den_d
    result = sum_n / sum_d
    return result

def factorial(n):
    result = 1
    if n != 0:
        for i in range(1, n+1):
            result *= i
    return result

def one_of_two_results(y):
    if (func_g(y**2) - 1) == 6 or y == 1 or y == -1:
        print("Данное значение y вызывает неопределенность!")
    else:
        result = (1.7 * func_g(0.25) + 2 * func_g(1 + y)) / (6 - func_g(y**2 - 1))
        print("Значение функции при заданном y равно:", result)

y = float(input("Введите значение y: "))
one_of_two_results(y)