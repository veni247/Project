a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
c = float(input("Nhập c: "))
if a < b and a < c:
    print("a là số nhỏ nhất")
elif b < a and b < c:
    print("b là số nhỏ nhất")
else:
    print("c là số nhỏ nhất")
