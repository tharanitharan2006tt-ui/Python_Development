numbers = [45,12,89,3,67]
small = numbers[0]
for i in numbers:
    if i < small:
        small = i
print(small)