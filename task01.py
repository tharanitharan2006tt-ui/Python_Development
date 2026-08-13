string = input("Enter a string: ")
upper_count = 0
lower_count = 0
other_count = 0
for ch in string:
    if ch.isupper():
        upper_count += 1
    elif ch.islower():
        lower_count += 1
    else:
        other_count += 1
print("Uppercase letters:", upper_count)
print("Lowercase letters:", lower_count)
print("Other characters:", other_count)