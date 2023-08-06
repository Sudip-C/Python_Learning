#question 1
for i in range(1,6):
    for j in range(1,i + 1):
        print(j, end=" ")
    print()


#question 2
numbers = [12, 75, 150, 180, 145, 525, 50]


for el in numbers:
  
  if el>500:
    break

  elif el>150:
    continue

  elif el%5==0 :
    print(el)


#question 3
s1 = "Ault"
s2 = "Kelly"
s3=""
max_length = min(len(s1), len(s2))

for i in range(max_length):
        s3 += s1[i] + s2[i]

s3 += s1[max_length:] + s2[max_length:]

print(s3)

#question 4
lower="abcdefghijklmnopqrstuvwxyz"
upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
my_test="PyNaTive"

sorted_lower=""
sorted_upper=""
for char in lower:
  for j in my_test:
    if char==j:
      sorted_lower+=j

for char in upper:
  for i in my_test:
    if char==i:
      sorted_upper+=i

print(sorted_lower+sorted_upper)

#question 6
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

list3 = []

for item1 in list1:
    for item2 in list2:
        list3.append(item1 + item2)

print(list3)

#question 7
list1 = [10, 20, 30, 40]
list2 = [400, 300, 200, 100]

for i in range(len(list1)):
    print(list1[i], list2[i])


#question 8

employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

output_result = {employee: defaults.copy() for employee in employees}

print(output_result)

#question 9
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# Keys to extract
keys = ["name", "salary"]
extracted_dict = {key: sample_dict[key] for key in keys}

print(extracted_dict)

#question 10
tuple1 = (11, [22, 33], 44, 55)

_list = list(tuple1[1])
_list[0] = 222
updated_tuple = (tuple1[0], _list, tuple1[2], tuple1[3])

print(updated_tuple)