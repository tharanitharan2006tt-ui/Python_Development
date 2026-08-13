for_loop = "tharanitharan"
for i in for_loop:
    print(i)
list = [1,2,'string']
for x in list:
    print(x)
#range
for i in range (1,10):
    print(i)
#start,stop,step
for i in range (1,22,3):
    print(i)
for j in range (0,10,2):
    if j == 8:
        break
    print(j)
for k in range (0,10,4):
    if k == 8:
        break
    print(k)
#continue
for l in range (0,20):
    if l == 8:
        continue
    print(l)
#star pattern
col = 5
for i in range(5,0,-1):
    print("*"*i)
rows = 5
for i in range(1,6,-1):
    print(" " * (rows-1) + "*" * i)

row = 5
for i in range(row):
    print(" " * i + "*" * (rows - i))