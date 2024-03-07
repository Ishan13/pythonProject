statement1 = "I fly in an invisible airplane"
statement2 = "My name is Wonder Woman"

# format each statement to be centered in a field of 40 characters.
f_stat1 = f"{statement1.center(40)}"
f_stat2 = f"{statement2.center(40)}"

print(f_stat1 + " ===> " + f_stat2)

# Using python slicing
print(f'{statement1:^40} ===> {statement2:^40}')
