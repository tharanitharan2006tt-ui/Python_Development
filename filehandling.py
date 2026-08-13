#write
# with open ("demo2.txt","w") as file :
#     file.write("There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some for"
#                "file handling")
# with open("demo2.txt", "a") as file:
#     file.write("\nfile handling!")
# with open ("demo2.txt","a") as file :
#     file.write("There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some for"
#                "file handling")

 #Show original content
# with open("demo2.txt", "r") as file:
#     print(file.read())

# Show only the first line
with open("demo2.txt", "r") as file:
    print(file.readline())
    print(file.readline())
    print(file.readline())


#  Append new content
with open("new.txt", "a") as file:
    file.write("\nfile handling!")

# Show final content
# with open("new.txt", "r") as file:
#     print(file.read())