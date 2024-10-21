# Positional Arguments
def introduce(name, age):
    print(f"Tôi tên là {name}, năm nay tôi {age} tuổi.")

introduce("Minh Quang", 21)

# Keyword Arguments
def student_info(name, age):
    print(f"Họ và tên: {name}")
    print(f"Tuổi: {age}")

student_info(name ="Phạm Hoàng Minh Quang",age= 22)

def describe_me(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

describe_me(name="Phạm Hoàng Minh Quang", age=21, major="Vật lý lý thuyết")

# Default Arguments
def greet(name, greeting="Hello"):
    print(f"{greeting} {name}!")

greet("world")
greet("thế giới", "Xin chào")

# Arbitrary Arguments
def print_numbers(*numbers):
    for num in numbers:
        print(num)

print_numbers(5, 10, 15, 20, 25, 30)

# Mixing
def info(name, age, *hobbies, **additional_info):
    """Hàm hiển thị thông tin cá nhân, sở thích và thông tin bổ sung."""
    print(f"Tên: {name}")
    print(f"Tuổi: {age}")
    print("Sở thích:")
    for hobby in hobbies:
        print(f" - {hobby}")
    print("Thông tin bổ sung:")
    for key, value in additional_info.items():
        print(f" {key}: {value}")

info("Minh Quang", 21, "Ngắm cảnh", "Chơi thể thao", city ="Hồ Chí Minh", major = "Vật lý lý thuyết")
