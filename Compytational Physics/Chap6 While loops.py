# Basic while loop
print("Dùng để đếm số:")
count = 1
while count <= 5:
    print(f"Số đếm: {count}")
    count += 1

print("Dùng để đếm ngược:")
countdown = 5
while countdown > 0:
    print(f"Đếm ngược: {countdown}")
    countdown -= 1

print("Dùng để tính tổng")
total = 0
number = 1
while number <= 100:
    total += number
    number += 1
print(f"Tổng của các số từ 1 đến 100 là: {total}")

# While loop with stop condition
print("Dùng để kiểm tra mật khẩu")
password = ""
while password != "Sinhvienvatlylythuyet":
    password = input("Nhập mật khẩu: ")
print("Mật khẩu đúng!")