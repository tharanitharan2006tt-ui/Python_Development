my_list = [1, 2, 3, 4, 5, "tharani","tharani",12.5,[1,2,3],{1,2,3}]
print(my_list)
print(type(my_list))

#assing the list elemennts
fruits = ["apple", "banana", "cherry","orange"]
print(fruits[-1])
print(fruits[-7:-1])
print(my_list[-7:-1])
print(my_list[:8])
#change items or modify
fruits = ["apple", "banana", "cherry","orange"]
fruits[1] = "mongo"
print(fruits)
#add item
fruits.append("orange")
print(fruits)
#insert at intex
fruits = ["apple", "banana", "cherry","orange"]
fruits.insert(1,"grape")
print(fruits)
#remove
fruits.remove("orange")
print(fruits)
#pop(remove last item)
fruits.pop()
print(fruits)
fruits.pop(0)
print(fruits)
#list function
num = [1,2,3,4,5,6,7,8,9]
a = ["apple", "banana", "cherry","orange","ZZZ","zzz"]
print(num)
print(len(num))
print(max(num))
print(min(num))
print(max(a))
print(sum(num))
a.sort()#ascending order
print(a)
num.sort()
print(num)
num.remove(8)#desending order
print(num)
a.reverse()
print(a)