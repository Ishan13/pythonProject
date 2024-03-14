# for i in range(5):
#     # Inner loop to print stars for each row
#     for j in range(i + 1):
#         print("*", end=" ")
#     print()  # Move to the next line after each row
#
#
# # Outer loop to iterate through each row
# for i in range(5):
#     # Print spaces for alignment
#     for j in range(5 - i - 1):
#         print(" ", end="")
#
#     # Print asterisks for the pattern
#     for k in range(i + 1):
#         print("* ", end="")
#
#     # Move to the next line after each row
#     print()
#
# rows = 5
# k = 2 * rows - 2
# for i in range(0, rows):
#     # process each column
#     for j in range(0, k):
#         # print space in pyramid
#         print(end=" ")
#     k = k - 2
#     for j in range(0, i + 1):
#         # display star
#         print("* ", end="")
#     print("")


# for i in range(1, 10):
#     if i % 3 == 0:
#         print(i)
#     else:
#         print(i, end=" ")