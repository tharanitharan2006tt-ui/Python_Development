my_string = "HelloWorld"
print(my_string)
print(type(my_string))
print(len(my_string))
#spillitting
s = my_string[0:6]
print(s)
s1 = my_string[-7:-1]
print(s1)
s2 = my_string[6:]
print(s2)
#lowercase to uppwecase
print(my_string.upper())
#upercase to lowercase
print(my_string.lower())
#capitalize
print(my_string.capitalize())
#title
new_string = "welcome all"
print(new_string.title())
#replace
sentence = "i love coffee"
print(sentence.replace("coffee", "tea"))
#split
data = "red,green,blue"
print(data.split(","))
#strip is deleite the st and end space
method = "    hellow world"
print(method)
print(method.strip())

text = "hellowwordtharanitharan"
#find first occurrence(how many times) of string (not find = -1)
print(text.find("tharanitharan"))
#count occurrence of string
print(text.count("i"))
#startswith  check the start characters
print(text.startswith("hello"))
#endswith to chick to end the charecters
print(text.endswith("n"))
#check if string contins only alphabets,if contain any spaces
print(text.isalpha())
#f-string
num1 = "hello"
num2 = "20"
#add = num1 + num2
add = f"{num1}{num2}"
print(add)
#input type
num = int(input("Enter a number: "))
num3 =int(input("Enter another number: "))
add1 = num + num3
print(add1)

