import numpy as np
def f(x,y):
    return 1+(x-y)**2

#Điều kiện ban đầu
x0 = 2
xN = 3
y0 = 1
N = 100

h = (xN - x0)/N

x_values = [x0]
y_values = [y0]

y=y0
for i in range(1, N + 1):
    if i <= N:
        x = x0 + i*h
        y_next = y + h*f(x,y)
        y = y_next
        x_values.append(x)
        y_values.append(y)

with open('EulerODE.txt', 'w') as file:
    file.write("x y\n")
    for x, y in zip(x_values, y_values):
        file.write(f"{x:.1f} {y:.6f}\n")

print('Kết quả đã được ghi vào EulerODE.txt')