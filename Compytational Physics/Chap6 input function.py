Tên = input("Nhập tên của bạn: ")
print(f"Xin chào, {Tên}!")

#Enter numbers to calculate and Handling incorrect input data
try:
    num1 = input("Nhập số nguyên thứ nhất: ")
    num2 = input("Nhập số nguyên thứ hai: ")
    sum = int(num1) + int(num2)
    print(f"Tổng của hai số nguyên vừa nhập là: {sum}")
except ValueError:
    print("Bạn đã nhập không phải là số nguyên.")