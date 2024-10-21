import numpy as np

def f(x, y):
    return 1 + (x - y)**2

x0 = 2
y0 = 1
x_end = 3
h = 0.1

x_values = np.arange(x0, x_end + h, h)
y_values = []

# Phương pháp Euler
y = y0
for x in x_values:
    y_values.append(y)
    y = y + h * f(x, y)

with open('EulerODE1.txt', 'w') as file:
    file.write("x y\n")
    for x, y in zip(x_values, y_values):
        file.write(f"{x:.1f} {y:.6f}\n")

print("Kết quả đã được xuất ra file EulerODE.txt.")
