import datetime

name = "John Doe"
age = 21

# using f-string to interpolate variables directly into a string.
message = f"My name is {name} and I am {age} years old."
print(message)

now = datetime.datetime.now()

formatted_date = f"Today is {now.strftime('%A, %B %d, %Y')} and the time is {now.strftime('%I:%M %p')}."
print(formatted_date)
