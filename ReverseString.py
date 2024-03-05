word = "WakeTech"

# Using string slicing to reverse the word
reversed_word = word[::-1]
print(reversed_word)

# Using reversed() method.
reversed_word = ''.join(reversed(reversed_word))
print(reversed_word)

# Using Loop to reverse the word.
reversed_word = ""
for char in word:
    reversed_word = char + reversed_word  # In Python, when you concatenate two strings using the + operator, the second string is appended to the end of the first string.
print(reversed_word)
