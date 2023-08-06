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
sum=0;
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
import math;
def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True

def prime(number):
    if is_prime(number):
        print(f"{number} is  a prime number.")
    else:
        print(f"{number} is  a prime number.")

prime(17)

def factorial(n):
    if n < 0:
        return 
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

input_number = 6
output_factorial = factorial(input_number)
print(f"The factorial of {input_number} is: {output_factorial}")

def fibonacci_sequence(n):
    if n <= 0:
        return 
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_sequence = [0, 1]
        while len(fib_sequence) < n:
            next_number = fib_sequence[-1] + fib_sequence[-2]
            fib_sequence.append(next_number)
        return fib_sequence

# Test the function with n = 10
n = 10
result = fibonacci_sequence(n)
print(result)

squares = [x ** 2 for x in range(1, 11)]
print(squares)