numbers = [1,2,4,6,7,9,10]
missing = []
for i in range (1,11):
    if  i not in numbers:
        missing.append(i)
print(missing)