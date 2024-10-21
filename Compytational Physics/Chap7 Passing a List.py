# Passing a List and Printing Elements
def list(my_list):
    for item in my_list:
        print(item)

list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Passing a List and Adding an Element
def add(my_list, element):
    my_list.append(element)
    return my_list

my_list = [1, 2, 3]
updated_list = add(my_list, 4)
print(updated_list)

# Calculating the Sum of List Elements
def sum_list(numbers):
    total = sum(numbers)
    return total

result = sum_list([10, 20, 30, 40])
print(result)

def sum_even_numbers(my_list):
    return sum(x for x in my_list if x % 2 == 0)

result = sum_even_numbers([1, 2, 3, 4, 5, 6])
print(result)

# Passing a List and Performing Operations on Elements
def square_elements(my_list):
    squared_list = [x ** 2 for x in my_list]
    return squared_list

original_list = [1, 2, 3, 4]
squared_list = square_elements(original_list)
print(squared_list)

# Removing Specific Elements from a List
def remove_element(my_list, value_to_remove):
    return [x for x in my_list if x != value_to_remove]

original_list = [1, 2, 3, 2, 4, 2]
updated_list = remove_element(original_list, 2)
print(updated_list)
