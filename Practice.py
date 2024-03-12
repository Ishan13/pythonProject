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

# for i in range(1, 10):
#     if i % 3 == 0:
#         print(i)
#     else:
#         print(i, end=" ")

