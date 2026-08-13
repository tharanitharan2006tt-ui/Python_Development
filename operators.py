#arithmetic operators
a = 20
b = 40
add = a+b
print(add)
sub = a-b
print(sub)
mul = a*b
print(mul)
div = a/b
print(div)
fl_div = 11//2 #it will return remider values
print(fl_div)
mod = 11%2
print(mod)
#power
expo = 3**3
print(expo)
#comparistion operators-it will return boolean value
eq = 10 == 11
print(eq)
no = 10 != 11
print(no)
lt = 20 < 13
print(lt)
gt = 20 > 13
print(gt)
le = 20 <= 13
print(le)
ge = 20 >= 13
print(ge)
#logical operators
#and - if both a condition is true it will return true
logic_and = 12 > 10 and 15 < 18
print(logic_and)
#or- if any of the  condition is true it will return true
logic_or = 12 < 10 or 15 > 16
print(logic_or)
#not-it return oposit value
logic_not = not 12==13
print(logic_not)
#assignment operators
x = 10
y = 60
x += y
print(x)
x -= y
print(x)
x *= y
print(x)
x /= y
x %= y
print(x)
x **= y
print(x)
x //= y
print(x)
#membership operators
#in,not in-it return boolen value
list1 = [1,2,3]
print(10 in list1)
print(2 not in list1)
#identity operators
#is,is not - to check the memory
list2 = [1,2,3]
list3 = [1,2,3]
list4 = list2
print(list2 is not list3)
print(list2 is list4)
#bitwise operators
bit_and = 58 & 18
print(bit_and)
#or - |
bit_or = 58 | 18
print(bit_or)
#xor-^
bit_xor = 13 ^ 5
print(bit_xor)
#not - ~
bit_not = ~10
print(bit_not)
#left-shift <<
left_shift = 23 << 2
print(left_shift)
#right_shift >>
right_shift = 46 >> 3
print(right_shift)


