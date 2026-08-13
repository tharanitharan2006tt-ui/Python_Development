list1 = [1,2,3,4]

list2 = [3,4,5]

l3 = []
for i in list1:
    if i not in list2:
        l3.append(i)
print(l3)