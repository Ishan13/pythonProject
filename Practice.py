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

# def odd_even(main_list):
#     odd_list = []
#     even_list = []
#
#     for num in main_list:
#         if num % 2 == 0:
#             even_list.append(num)
#         else:
#             odd_list.append(num)
#
#     return odd_list, even_list
#
#
# main_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# odd_list, even_list = odd_even(main_list)
# print("Odd numbers:", odd_list)
# print("Even numbers:", even_list)

# def odd_even(main_list):
#     odd_list = []
#     even_list = []
#
#     i = 0
#     while i < len(main_list):
#         num = main_list[i]
#         if num % 2 == 0:
#             even_list += [num]
#         else:
#             odd_list += [num]
#         i += 1
#
#     return odd_list, even_list
#
# main_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# odd_list, even_list = odd_even(main_list)
# print("Odd numbers:", odd_list)
# print("Even numbers:", even_list)

# def number_to_word(number):
#     # Define lists for words representing numbers
#     ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
#     teens = ["", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
#     tens = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
#     thousands = ["", "thousand", "million"]
#
#     # Function to convert three-digit number to word
#     def three_digits(num):
#         if num < 100:
#             return two_digits(num)
#         else:
#             if num % 100 == 0:
#                 return ones[num // 100] + " hundred"
#             else:
#                 return ones[num // 100] + " hundred and " + two_digits(num % 100)
#
#     # Function to convert two-digit number to word
#     def two_digits(num):
#         if num < 10:
#             return ones[num]
#         elif 10 <= num < 20:
#             return teens[num - 10]
#         else:
#             return tens[num // 10] + ("-" + ones[num % 10] if num % 10 != 0 else "")
#
#     # Function to convert any number to word
#     def number_to_words(num):
#         if num == 0:
#             return "zero"
#         elif num < 10:
#             return ones[num]
#         elif num < 100:
#             return two_digits(num)
#         else:
#             words = ""
#             for i in range(3):
#                 if num % 1000 != 0:
#                     words = three_digits(num % 1000) + " " + thousands[i] + " " + words
#                 num //= 1000
#             return words.strip()
#
#     return number_to_words(number)
#
#
# # Input from the user
# num = int(input("Enter a number: "))
# print("Word representation:", number_to_word(num))

# Define empty list to store employee data
# employee_data = []
#
# # Function to input hardcoded employee data
# def input_employee_data():
#     hardcoded_data = [
#         {"Employee Number": "1", "Employee Name": "Jane Doe", "Department Number": "10", "Salary": "50000"},
#         {"Employee Number": "2", "Employee Name": "Jane Doe", "Department Number": "10", "Salary": "60000"},
#         {"Employee Number": "3", "Employee Name": "Jane Doe", "Department Number": "20", "Salary": "55000"},
#         {"Employee Number": "4", "Employee Name": "Jane Doe", "Department Number": "20", "Salary": "52000"},
#         {"Employee Number": "5", "Employee Name": "Jane Doe", "Department Number": "30", "Salary": "58000"},
#         {"Employee Number": "6", "Employee Name": "Jane Doe", "Department Number": "30", "Salary": "62000"},
#         {"Employee Number": "7", "Employee Name": "Jane Doe", "Department Number": "40", "Salary": "53000"},
#         {"Employee Number": "8", "Employee Name": "Jane Doe", "Department Number": "40", "Salary": "54000"},
#         {"Employee Number": "9", "Employee Name": "Jane Doe", "Department Number": "50", "Salary": "57000"},
#         {"Employee Number": "10", "Employee Name": "Jane Doe", "Department Number": "50", "Salary": "59000"}
#     ]
#
#     for data in hardcoded_data:
#         employee_data.append(data)
#
# # Function to print employee data
# def print_employee_data():
#     for employee_info in employee_data:
#         print("Employee Number:", employee_info["Employee Number"])
#         print("Employee Name:", employee_info["Employee Name"])
#         print("Department Number:", employee_info["Department Number"])
#         print("Salary:", employee_info["Salary"])
#         print()
#
# def findempbyempno():
#     print("Find Employee By EmpNo Operation is going to be executed.")
#     emp_no = input("Enter the Employee Number to search: ")
#
#     # Your existing code logic goes here
#     # For example:
#     for i in range(len(employee_numbers)):
#         if emp_no == employee_numbers[i]:
#             print("Employee found!")
#             print("Employee Number:", employee_numbers[i])
#             print("Department Number:", department_numbers[i])
#             print("Salary:", salaries[i])
#             break
#     else:
#         print("Employee not found.")
#
# def findempbydeptno():
#     print("Find Employee By DeptNo Operation is going to be executed.")
#     dept_no = input("Enter the Department Number to search: ")
#
#     # Your logic to find employee by department number goes here
#
# def findempbysalary():
#     print("Find Employee By Salary Operation is going to be executed.")
#     salary = input("Enter the Salary to search: ")
#
#     # Your logic to find employee by salary goes here
#
#
# # Your existing code continues...
# while True:
#     print("\n"*4)
#     print(f"\t\t\t\t MENU: Press 1, 2, 3, 4, 5 or 6")
#     print(f"\t\t\t\t ================================")
#     print(f"\t\t\t\t1. Find employee by empno.")
#     print(f"\t\t\t\t2. Find employee by deptno")
#     print(f"\t\t\t\t3. Find employee by salary.")
#     print(f"\t\t\t\t4. Input employee data.")
#     print(f"\t\t\t\t5. Print employee data.")
#     print(f"\n\n\t\t\t\t6. Press 6 to quit.")
#
#     choice = int(input("Enter your choice of operation:"))
#     if choice == 6:
#         break
#
#     if choice == 1:
#         findempbyempno()
#     elif choice == 2:
#         findempbydeptno()
#     elif choice == 3:
#         findempbysalary()
#     elif choice == 4:
#         input_employee_data()
#     elif choice == 5:
#         print_employee_data()

# a = [[2, 5], [7, 3]]
# b = [[9, -5], [3, 2]]
#
# def add_matrices(m1, m2):
#     results = []
#     for i in range(len(a)):
#         result = []
#         for j in range(len(a[0])):
#             c = a[i][j] + b[i][j]
#             result.append(c)
#         results.append(result)
#     return results
#
# test = add_matrices(a, b)
# print(test)

