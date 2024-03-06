# with open("my_file.txt", "w") as my_file:
#     print('I am writing some stuff that I expect to see in my_file.txt\n', file=my_file)

# first I made a new file, used "w" for write mode and saved an output and second I used "a" for append mode and added the second sentence to the same file.

with open("my_file.txt", "a") as my_file:
    print('I am updating the file with this sentence.\n', file=my_file)
