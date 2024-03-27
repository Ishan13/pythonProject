# def factorial(n):
#
#     if n == 0:
#         return 1
#     else:
#         result = 1
#         for i in range(1, n + 1):
#             result *= i
#         return result
#
#
# def sine_taylor_series(x, terms=10):
#
#     sine = 0.0
#     for n in range(terms):
#         coefficient = (-1) ** n
#         term = coefficient * (x ** (2 * n + 1)) / factorial(2 * n + 1)
#         sine += term
#     return sine
#
# angle_degrees = 30
# angle_radians = angle_degrees * (3.14159 / 180)
# print("Approximate sine of", angle_degrees, "degrees:", sine_taylor_series(angle_radians))

def factorial(n):
    res = 1
    for i in range(1, n+1):
        res = res * i
    return res

# def power(x, n):
#     res = 1
#     for i in range(1, n+1):
#         res = res * x
#     return res
#
# print(power(2, 3))

def power(x, n):
    return x ** n

def sine_series(x, n):
    sign = 1
    res = 0

    for i in range(1, n+1):
        if i%2 != 0:
            a = sign * (power(x, i)/factorial(i))
            print(a, end=' ')
            res = res + a
            sign = sign * -1

    return res

x = int(input("enter the value of x: "))
n = int(input("enter the upper limit: "))
ans = sine_series(x, n)
print("\nThe answer is: ", ans)
