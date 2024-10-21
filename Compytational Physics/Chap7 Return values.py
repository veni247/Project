# Function returns a value
def sum(a,b):
    return a + b

print(sum(5,15))

def power(base, exponent = 2 ):
    return base ** exponent

print(power(2))
print(power(2,5))

def factorial(n):

    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))
# Functions that return multiple values
def min_max(numbers):
    return min(numbers), max(numbers)


min_value, max_value = min_max([32, 53, 14, 9, 21])
print(f"Giá trị nhỏ nhất: {min_value}")
print(f"Giá trị lớn nhất: {max_value}")

# Function returns default value
def greet(name, greeting="Hello"):
    return f"{greeting} {name}!"

message1 = greet("world")
message2 = greet("thế giới", "Xin chào")

print(message1)
print(message2)

# Function returns condition value
def even(number):
    return number % 2 == 0

print(even(4))
print(even(7))
