#1
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Sum:", a + b)
print("Difference:", a - b)
print("Product:", a * b)

#2
num = int(input("Enter an integer: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

#3
grade = int(input("Enter grade (0-100): "))

if grade < 0 or grade > 100:
    print("Invalid input")
elif grade >= 80:
    print("A")
elif grade >= 60:
    print("B")
elif grade >= 40:
    print("C")
else:
    print("F")

#4
total = 0
count = 0

while count < 5:
    num = int(input("Enter a number: "))
    total += num
    count += 1

print("Sum of inputs:", total)

#5
layers = int(input("Enter number of layers: "))

for i in range(1, layers + 1):
    print(" " * (layers - i) + "*" * (2 * i - 1))
for i in range(1, 21):
    if i % 3 == 0:
        print("X")
    else:
        print(i)

#6
for i in range(1, 21):
    if i % 3 == 0:
        print("X")
    else:
        print(i)

#7
my_list = [10, 20, 30, 40, 50]
my_list[2] = 99
print("Changed list:", my_list)

#8
my_list = [1, 2, 3, 4, 5]
reversed_list = []

for i in range(len(my_list) - 1, -1, -1):
    reversed_list.append(my_list[i])

print("Reversed list:", reversed_list)

#9
my_tuple = (1, 2, 3)
temp_list = list(my_tuple)
temp_list[1] = 99
my_tuple = tuple(temp_list)

print("Changed tuple:", my_tuple)

#10
def sum_and_product(x, y):
    return x + y, x * y

s, p = sum_and_product(5, 3)
print("Sum:", s)
print("Product:", p)

#11
def odd_or_even(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

num = int(input("Enter a number: "))
print(odd_or_even(num))

#12
my_list = [1, 2, 3, 4, 5]
total = 0

for num in my_list:
    total += num

print("Sum of elements:", total)

#13
numbers = []
for i in range(5):
    num = int(input("Enter a number: "))
    numbers.append(num)

def smallest(nums):
    min_val = nums[0]
    for n in nums:
        if n < min_val:
            min_val = n
    return min_val

def largest(nums):
    max_val = nums[0]
    for n in nums:
        if n > max_val:
            max_val = n
    return max_val

def sum_elements(nums):
    total = 0
    for n in nums:
        total += n
    return total

print("Smallest:", smallest(numbers))
print("Largest:", largest(numbers))
print("Sum:", sum_elements(numbers))
