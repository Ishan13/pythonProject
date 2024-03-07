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

grade = float(input("Enter the grade of the student: "))

if grade >= 90:
    print("Outstanding")
elif grade >= 80:
    print("Excellent")
elif grade >= 70:
    print("Very Good")
elif grade >= 60:
    print("Good")
elif grade >= 50:
    print("Fair")
elif grade >= 40:
    print("Below Average")
else:
    print("Failed/Absent")

