# length = int(input("Enter the length of the rectangle :"))
# width = int(input("Enter the width of the rectangle:"))
# perimeter = 2 * (length + width)
# print("The perimeter of the rectangle is : " f'{perimeter}')


# pi = 3.14
# radius = int(input("Enter the radius of the circle:"))
# area = pi * radius ** 2
# print("The area of the circle is", area)

# number = int(input("Enter a positive number:"))
# odd_even = number % 2
# if odd_even == 0:
#     print(f"Number {number} is Even.")
# else:
#     print(f"Number {number} is Odd.")

# grade = float(input("Enter the grade of the student: "))
#
# if grade >= 90:
#     print("Outstanding")
# elif grade >= 80:
#     print("Excellent")
# elif grade >= 70:
#     print("Very Good")
# elif grade >= 60:
#     print("Good")
# elif grade >= 50:
#     print("Fair")
# elif grade >= 40:
#     print("Below Average")
# else:
#     print("Failed/Absent")

# sample_dict = {1: 'Coffee', 2: 'Tea', 3: 'Juice'}
# for x in sample_dict:
#     print(x)

# def recursion(num):
#     print(num)
#     next = num - 3
#     if next > 1:
#         recursion(next)
#
# recursion(11)

# num = 9
# class Car:
#     num = 5
#     bathrooms = 2
#
# def cost_evaluation(num):
#     num = 10
#     return num
#
# class Bike():
#     num = 11
#
# cost_evaluation(num)
# car = Car()
# bike = Bike()
# car.num = 7
# Car.num = 2
# print(num)

# for i in range(25):
#     x = (i+1)*2
#     print(x)

# x = 0
# for i in range(1, 6):
#     x += i
#     print(x)
#
# print(f"The running summation is {x}")

# x = 1
# for i in range(1, 6):
#     x = x * i
#
# print(x)

# start = int(input("Enter the starting number of the range: "))
# end = int(input("Enter the ending number of the range: "))
# sum = 0
# for num in range(start, end+1):
#     sum += num
#
# print(sum)

# number = int(input("Enter a number: "))
#
# if number > 1:
#     for i in range(2, int(number**0.5)+1):
#         if (number % i) == 0:
#             print(f"{number} is not a prime number.")
#             break
#     else:
#         print(f"{number} is a prime number.")
# else:
#     print(f"{number} is not a prime number.")

# res = 0
# n = int(input("Enter the number: "))
# for i in range(1, n):
#     if n % i == 0:
#         res = res + i
#
# if res == n:
#     print(f"{n} is a perfect number")
# else:
#     print(f"{n} is not a perfect number")

# n = int(input("Enter a number: "))
# n2 = int(input("Enter second number: "))
# mul = 0
# for i in range(n, n2+1):
#     for j in range(1, 11):
#         mul = j * i
#         print(f"{i} x {j}  = {mul}")
#
#     print("=============================")

# i = 1
# while True:
# v = input("Enter the secret code: ")
# if v == "secret" and i < 3:
# print("Password matched. Access granted.")
# break
# elif i == 3:
# print("Take a break for 30 minutes and then try again!")
# break
# else:
# i = i + 1
# print("That was not the correct code. I cant grant you the access!")

# if __name__ ==__main()__

# def ten_print(n):
#     if n==11:
#         return
#     else:
#         print(n)
#         ten_print(n +1)
#
# ten_print(1)

# def fibonacci(n):
#     if n <= 1:
#         return n
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)
#
# n = 10
# fib_series = [fibonacci(i) for i in range(n)]
# print(fib_series)

# def fibonacci(n, a=0, b=1):
#     if a <= n:
#         return [a] + fibonacci(n, b, a+b)
#     else:
#         return []
#
# print(fibonacci(34))

# a = [2, 0, -5, "Hello", 9.99]
# i = 0
# while i < 5:
#     print(a[i])
#     i += 1

# def printlist(l):
#     i = 0
#     while i < len(l):
#         print(l[i])
#         i += 1
#
#
# a = [2, 0, -5, "Hello", 9.99]  # two blank lines expected after ending the block of function.
# printlist(a)

# def runningsum(nums):
#     for i in range(1, len(nums)):
#         nums[i] += nums[i - 1]
#     return nums
#
#
# input_list = [1, 2, 3, 4, 5]
# result = runningsum(input_list)
# print(result)

# def addlistwithwhile(l):
#     rs = 0
#     i = 0
#     runningsumlist = []
#
#     while i < len(l):
#         rs = rs + l[i]
#         runningsumlist.append(rs)
#         i = i+1
#
#     return runningsumlist
#
#
# ans = addlistwithwhile([1, 2, 3, 4, 5])
# print(ans)

# my_list3 = ["mouse", [9, 3, 6], ['a']]
# print(my_list3[0][3])
# print(my_list3[1][2])

def odd_even(main_list):
    odd_list = []
    even_list = []

    for num in main_list:
        if num % 2 == 0:
            even_list.append(num)
        else:
            odd_list.append(num)

    return odd_list, even_list


main_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_list, even_list = odd_even(main_list)
print("Odd numbers:", odd_list)
print("Even numbers:", even_list)


