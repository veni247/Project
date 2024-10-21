# Using *args
def print_all(*args):
    for arg in args:
        print(arg)

print_all(1, 2, 3)
print_all("Táo", "Chuối", "Sơ ri")
print_all("Minh Quang", 21, "Vật Lý Lý Thuyết", 21130243)

# Using *kwargs
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Call the function with different keyword arguments
print_info(Name="Minh Quang", Age=21, City="Ho Chi Minh")
print_info(ID= 21130243, Major="Theoretical Physic")

# Using *args and *kwargs
def combined_function(positional_arg, *args, **kwargs):
    print(f"Tham số vị trí: {positional_arg}")
    print("Các tham số vị trí khác:")
    for arg in args:
        print(arg)
    print("Các tham số với tên:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Gọi hàm với các tham số khác nhau
combined_function("Một", 2, 3, 4, Name="Minh Quang", Age=21, City="Ho Chi Minh")

