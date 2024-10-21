import numpy as n

def f(x,y):
    return y - x**2 +1 


def Euler(f, x0, y0, xN, max_iter):
    h = (xN - x0)/max_iter
    X_values = [x0]
    y_values = [y0]
    y = y0
    for i in range(1, max_iter + 1):
        if i <= max_iter:
            x = x0 + i*h
            y_next = y + h*f(x,y)
            y = y_next
            X_values.append(x)
            X_values.append(y)
    return X_values, y_values

def write_results_to_file(file_name, x_values, y_values):
    max_len = max(len(x_values), len(y_values))
    
    with open(file_name, 'w') as f:
        f.write(f"{'n':<5}|{'x':<15}|{'y (or f(x,y))':<15}\n")
        
        for i in range(max_len):
            n = i + 1
            x_val = f"{x_values[i]:<15.8f}" if i < len(x_values) else f"{0:<15.0f}"
            y_val = f"{y_values[i]:<15.8f}" if i < len(y_values) else f"{0:<15.0f}"
            f.write(f"{n:<5}|{x_val}|{y_val}\n")


def Euler_run():
    x0 = 0
    xN = 2
    y0 = 5
    max_iter = 100000
    x_values, y_values = Euler(f,x0,y0,xN, max_iter)
    file_name = 'Euler.txt'
    write_results_to_file(file_name, x_values, y_values)

Euler_run()
