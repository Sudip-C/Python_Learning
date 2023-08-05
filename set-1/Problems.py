print("Hello,World")
# string
_a= "sudip"
#float
b=3.14
#int
c=23
#boolean
d=True
#list
e=["rajesh",12,12.32,False]
#tuple
f = (10, 20, 30, 'world', False)
#dictionary
_dict = {'name': 'sudip', 'age': 23, 'city': 'Kolkata'}

print(type(_a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(_dict))

my_list=list(range(1, 11))
print(my_list)

number_to_add=3
my_list.append(number_to_add)
print(my_list)

number_to_remove=6
my_list.remove(number_to_remove)
print(my_list)

my_list.sort()
print(my_list)

num_list=[10,20,25,87]
sum=0
list_len=len(num_list)
for number in num_list:
  sum+=number

print(sum)
print(sum/list_len)

def new_string(input_string):
    reversed_string = ""
    for char in input_string:
        reversed_string = char + reversed_string
    return reversed_string

print(new_string("sudip"))

name="sudip"
vowels="aeiou"
count=0
for char in name:
  for c in vowels:
    if char==c:
      count=count+1

print(count)