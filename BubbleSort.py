l = [3, 1, 4, 0, 2, 5, -1]

for i in range(0, len(l) -1): #pass
    for j in range(0, len(l) - i - 1): #comparisons during each pass
        if l[j] > l[j + 1]:
            l[j],  l[j + 1] = l[j + 1], l[j]
        print(f"After Pass # {i + 1} and Comparison # {j + 1} the list is: {l}")

print(f"The sorted list is: {l}")