mark = int(input("Enter your mark: "))
if mark < 0 or mark > 100:
    print("Invalid Mark! Enter marks between 0 and 100.")
elif mark >= 75:
    print("Grade A")
elif mark >= 50:
    print("Grade B")
elif mark >= 25:
    print("Grade C")
elif mark >= 15:
    print("Grade D")
else:
    print("Grade E")