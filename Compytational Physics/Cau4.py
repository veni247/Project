import math

def f(x):
    return x**2 - 1

def bisection(a, b, tol):
    if f(a) * f(b) >= 0:
        print("Không thể áp dụng phương pháp Bisection.")
        return None

    while (b - a) / 2 > tol:
        m = (a + b) / 2
        if f(m) == 0:
            return m
        elif f(a) * f(m) < 0:
            b = m
        else:
            a = m

    return (a + b) / 2

a = 0
b = 10
tolerance = 1e-5
nghiem = bisection(a, b, tolerance)

if nghiem is not None:
    print(f"Nghiệm xấp xỉ của phương trình là: {nghiem}")
else:
    print("Không tìm thấy nghiệm.")
