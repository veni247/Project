import matplotlib.pyplot as plt

x_values = []
y_values = []

with open('EulerODE1.txt', 'r') as file:
    next(file)  # Bỏ qua tiêu đề
    for line in file:
        x, y = map(float, line.split())
        x_values.append(x)
        y_values.append(y)

plt.plot(x_values, y_values, marker='o', linestyle='-', color='b')
plt.title('Giải phương trình vi phân bằng phương pháp Euler')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.savefig('EulerODE_plot.png')
plt.show()