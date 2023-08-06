#question 1
my_tuples= [("John", 25), ("Jane", 30)]
updated=""
for name,age in my_tuples:
  updated+=f"{name} is {age} years old."

print(updated)

# #question 2
students={}

def student(name, age):

  students[name]=age
  return students

studen_name=student("john",25)
print(studen_name)

students["john"]=26

print(students)

del students["john"]
print(students)

#question 3
def two_sum(nums, target):
    num_indices = {}

    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_indices:
            return [num_indices[complement], i]

       
        num_indices[num] = i

    return []

input_list = [2, 7, 11, 15]
target = 9
result = two_sum(input_list, target)
print(result)
 #another approach
Number_list=[2, 7, 11, 15]
target=9
def two_sum(Number_list,target):
 for i in range(0,len(Number_list)-1):
  if(Number_list[i]+Number_list[i+1])==target:
    return [i,i+1]

print(two_sum(Number_list,target))

#question 4
def Pallindrome(s):
  reversed=""
  for char in s:
    reversed=reversed+char
  if reversed==s:
    return "it is pallindrome"
  else:
    return "it's not a pallindrome"

print(Pallindrome("madam"))

#question 5

def selection_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

num_list=[64, 25, 12, 22, 11]
print(selection_sort(num_list))

#question 6
for i in range(1,101):
  if i%3==0 and i%5==0:
    print("FizzBuzz")
  elif i%3==0:
    print("Fizz")
  elif i%5==0:
    print("Buzz")
  else:
    print(i)

#question 7
def count_words_in_file(input_file, output_file):
    try:
        with open(input_file, 'r') as file:
            content = file.read()

        words = content.split()  # Split the content into words using whitespace as the delimiter
        word_count = len(words)

        with open(output_file, 'w') as output:
            output.write(f"The number of words in the file is: {word_count}")

        print("Word count successfully written to the output file.")

    except FileNotFoundError:
        print("Input file not found.")
    except Exception as e:
        print("An error occurred:", e)

input_file="input_file.txt"
output_file="output_file.txt"
count_words_in_file(input_file, output_file)

#question 10

def divison(a,b):
   if b==0:
      return "Cannot divide by zero"
   else :
    return a/b
  
print(divison(5,15))

