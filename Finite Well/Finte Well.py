import numpy as np
import matplotlib.pyplot as plt
from math import cos, tan, sqrt, exp
from scipy.constants import hbar

# Định nghĩa hàm f và f_derivative
def f(z, z0):
    return tan(z) - sqrt((z0 / z) ** 2 - 1)

def f_derivative(z, z0):
    return (1 / (cos(z) ** 2)) + (z0 ** 2 / (z ** 3 * sqrt((z0 / z) ** 2 - 1)))

# Chia khoảng dùng để giải số
def find_intervals(f, z0, z_min, z_max, delta_z):
    intervals = []
    z = z_min
    while z < z_max:
        try:
            if f(z, z0) * f(z + delta_z, z0) < 0:
                intervals.append((z, z + delta_z))
        except ValueError:
            pass
        z += delta_z
    return intervals

# Phương pháp Bisection để tìm nghiệm
def bisection(f, z0, b, c, N, tol=1e-8):
    if f(b, z0) * f(c, z0) >= 0:
        print("Không thể áp dụng phương pháp Bisection.")
        return None
    for i in range(N):
        x = (b + c) / 2
        if abs(f(x, z0)) < tol:
            print(f"PP Bisection: Nghiệm hội tụ tại {x} với {i+1} lần thử")
            return x
        if f(b, z0) * f(x, z0) < 0:
            c = x
        else:
            b = x
    return None

# Phương pháp Newton-Raphson
def NR(f, g, x0, z0, N, eps):
    z = np.zeros(N)
    z[0] = x0
    results_NR = np.zeros(N)
    for i in range(N):
        if i + 1 < N:
            try:
                z[i + 1] = z[i] - f(z[i], z0) / g(z[i], z0)
                if abs(z[i + 1] - z[i]) <= eps:
                    print(f'PP NR: Nghiệm hội tụ tại {z[i + 1]} với {i} lần lặp')
                    results_NR[i + 1] = z[i + 1]
                    break
            except (ZeroDivisionError, ValueError) as Z:
                print(f"LỖI CHƯƠNG TRÌNH: {Z}")
    return z, results_NR

# Phương pháp Secant
def Secant(f, z0, x0, x1, N, eps):
    z = np.zeros(N)
    z[0] = x0
    z[1] = x1
    results_Secant = np.zeros(N)
    for i in range(N):
        if i + 2 < N:
            try:
                z[i + 2] = z[i + 1] - f(z[i + 1], z0) * ((z[i + 1] - z[i]) / (f(z[i + 1], z0) - f(z[i], z0)))
                if abs(z[i + 2] - z[i + 1]) <= eps:
                    print(f'PP Secant: Nghiệm hội tụ tại {z[i + 2]} với {i} lần lặp')
                    results_Secant[i + 2] = z[i + 2]
                    break
            except (ZeroDivisionError, ValueError) as Z:
                print(f"LỖI CHƯƠNG TRÌNH: {Z}")
    return z, results_Secant

# Tìm hàm sóng
def find_all_ψ(x, a, kappa_values, l_values):
    all_ψ = []
    for kappa, l in zip(kappa_values, l_values):
        D = 1 / (sqrt(a + 1 / kappa))
        F = (exp(kappa * a) * cos(l * a)) / (sqrt(a + 1 / kappa))
        ψ = np.zeros(len(x))
        
        for i, xi in enumerate(x):
            if -a <= xi <= 0:  # Đối xứng trái của giếng thế (x < 0)
                ψ[i] = D * cos(l * -xi)
            elif 0 <= xi <= a:  # Trong giếng thế (x từ 0 đến a)
                ψ[i] = D * cos(l * xi)
            elif xi > a:  # Bên ngoài giếng thế (x > a)
                ψ[i] = F * exp(-kappa * xi)
            elif xi < -a:  # Bên ngoài giếng thế đối xứng trái (x < -a)
                ψ[i] = F * exp(kappa * xi)

        all_ψ.append(ψ)
    
    return all_ψ


# Hàm vẽ đồ thị
def plot_graph(z0, z_values, tan_z, sqrt_term, f_max, x_values, all_ψ_values, z, κ, l):
    # Tạo đồ thị đầu tiên: tan(z) và sqrt_term
    plt.figure(figsize=(12, 10))

    plt.subplot(2, 1, 1)  # Vẽ hai đồ thị trong cùng một hình ảnh (2 hàng, 1 cột, đồ thị đầu tiên)
    plt.plot(z_values, tan_z, label=r'$\tan(z)$', color='blue')
    plt.plot(z_values, sqrt_term, label=r'$\sqrt{(z_0 / z)^2 - 1}$', color='red')
    plt.scatter(z, np.tan(z), color='green', label='Nghiệm của $z$', zorder=5)

    plt.axhline(0, color='black', linewidth=0.5)

    # Đặt giới hạn trục
    plt.xlim(0, z0)
    plt.ylim(-5, f_max + 5)
    plt.title(r'Đồ thị của $\tan(z)$ và $\sqrt{(z_0 / z)^2 - 1}$')
    plt.xlabel('z')
    plt.ylabel('f(z)')
    plt.legend()
    plt.grid(True)

    # Dùng để vẽ Gnupot
    with open('z_data.txt', 'w', encoding='utf8') as f:
        # Ghi tiêu đề cột
        s0 = ('{0:^20}|{1:^20}|{2:^20}\n'.format('z Values', 'tan(z)', 'sqrt_term'))
        f.write(s0)

        # Ghi dữ liệu theo định dạng bảng
        for z_val, tan_val, sqrt_val in zip(z_values, tan_z, sqrt_term):
            s1 =('{0:^20.5f}|{1:^20.5f}|{2:^20.5f}\n'.format(z_val, tan_val, sqrt_val))
            f.write(s1)


    # Tạo đồ thị thứ hai: Hàm sóng ψ
    plt.subplot(2, 1, 2)  # Đồ thị thứ hai (2 hàng, 1 cột, đồ thị thứ hai)
    for idx, ψ_values in enumerate(all_ψ_values):
        plt.plot(x_values, ψ_values, label = f'ψ{idx + 1}')
    #plt.plot(-x_values, ψ_values, color = 'purple')
    plt.axhline(0, color='black', linewidth=0.5)

    # Đặt giới hạn trục x dựa trên giá trị của x_values
    plt.xlim(- max(x_values), max(x_values))
    plt.title(r'Hàm sóng $\psi(x)$ trong hố thế hữu hạn')
    plt.xlabel('x (m)')
    plt.ylabel(r'$\psi(x)$')
    plt.legend()
    plt.grid(True)

    # Dùng để vẽ Gnupot
    with open('psi_data.txt', 'w', encoding='utf8') as f:
        # Ghi tiêu đề cột
        header = '{0:^20}|'.format('x Values')
        for idx in range(len(all_ψ_values)):
            header += '{0:^20}|'.format(f'ψ{idx+1} Values')
        header += '\n'
        f.write(header)
        
        # Ghi dữ liệu theo định dạng bảng
        for i in range(len(x_values)):
            row = '{0:^20.5f}|'.format(x_values[i])
            for ψ_values in all_ψ_values:
                row += '{0:^20.5f}|'.format(ψ_values[i])
            row += '\n'
            f.write(row)

    # Điều chỉnh khoảng cách giữa các đồ thị
    plt.tight_layout()
    plt.show()


def main():
    # Các thông số

    # Giếng thế sâu rộng
    a = 8e-10  # Đơn vị mét
    m = 9.11e-31  # Khối lượng electron
    V0 = 10 # eV
    V0_Joules = V0*1.6e-19  # Chuyển đổi sang joules
    z0 = (a/hbar)*sqrt(2*m*V0_Joules) # Giá trị z0
    print(f'z0 là: {z0}')

    # Giếng thế nông hẹp
    """a = 2.5e-10  # Đơn vị mét
    m = 9.11e-31  # Khối lượng electron
    V0 = 2 # eV
    V0_Joules = V0*1.6e-19  # Chuyển đổi sang joules
    z0 = (a/hbar)*sqrt(2*m*V0_Joules) # Giá trị z0
    print(f'z0 là: {z0}')"""
    
    # Thông số cho các phương pháp tìm nghiệm
    N = 10000

    # Tìm khoảng có nghiệm
    intervals = find_intervals(f, z0, 1e-10, z0, 1e-5)

    # Tạo các mảng cho các thông số khác
    κ = []
    l = []
    z = []
    E = []
    # Lưu kết quả của phương pháp Bisection
    with open('result_Bisection.txt', 'w') as B_file:
        s0 = '{0:^20} \n'  # Cập nhật tiêu đề
        B_file.write(s0.format('z_Bisection'))
        for interval in intervals:
            z_bisection = bisection(f, z0, interval[0], interval[1], N)
            if z_bisection is not None:
                z.append(z_bisection)
                kappa = sqrt(z0**2 - z_bisection**2) / (a)
                κ.append(kappa)
                L = z_bisection/a
                l.append(L)
                s1 = '{0:20} \n'  # Chỉ ghi giá trị
                B_file.write(s1.format(z_bisection))

    # Lưu kết quả của phương pháp Newton-Raphson
    with open('result_NR.txt', 'w') as NR_file:
        s0 = '{0:^20} \n'  # Cập nhật tiêu đề
        NR_file.write(s0.format('z_NR'))
        for interval in intervals:
            z_NR, results_NR = NR(f, f_derivative, interval[0], z0, N, 1e-15)
            for i in range(N):
                if results_NR[i] != 0:
                    s1 = '{0:20} \n'  # Chỉ ghi giá trị
                    NR_file.write(s1.format(z_NR[i]))

    # Lưu kết quả của phương pháp Secant
    with open('result_Secant.txt', 'w') as Secant_file:
        s0 = '{0:^20} \n'  # Cập nhật tiêu đề
        Secant_file.write(s0.format('z_Secant'))
        for interval in intervals:
            z_Secant, results_Secant = Secant(f, z0, interval[0], interval[1], N, 1e-15)
            for i in range(N):
                if results_Secant[i] != 0:
                    s1 = '{0:20} \n'  # Chỉ ghi giá trị
                    Secant_file.write(s1.format(z_Secant[i]))      

    # Lưu kết quả của κ, l và E vào cùng một file
    κ = np.array(κ) # Định dạng lại để tính E
    E = ((κ * hbar) **2) / (-2*m)
    with open('κ_l_E_data.txt', 'w', encoding= 'utf8') as file:
        # Ghi tiêu đề cột
        s0 = '{0:^20} {1:^20} {2:^20}\n'.format('κ Values', 'l Values', 'E Values')
        file.write(s0)
        
        # Ghi dữ liệu theo định dạng bảng
        for κ_value, l_value, E_value in zip(κ, l, E):
            s1 = '{0:^20.5f} {1:^20.5f} {2:^20.5e}\n'.format(κ_value, l_value, E_value)
            file.write(s1)


    # Lấy dữ liệu nghiệm đầu tiên trong file nghiệm để tính giá trị cực đại của f(z)
    with open('result_Bisection.txt', 'r') as Bisection_file:
        lines = Bisection_file.readlines() 
        if len(lines) >= 2:
            second_line = float(lines[1].strip())
    
    # Tính toán giá trị cần thiết cho đồ thị
    z_values = np.arange(0.01, z0, (z0-0.01)/N)  # Tránh z=0 do điểm kỳ dị
    tan_z = np.tan(z_values)
    sqrt_term = np.sqrt((z0 / z_values) ** 2 - 1)
    f_max = np.sqrt((z0/second_line)**2 - 1)
    x_values = np.linspace(-a-1e-9, a+1e-9, 10000)  # Giá trị x cho hàm sóng

    # Tính toán hàm sóng
    all_ψ_values = find_all_ψ(x_values, a, κ, l) # Gọi hàm find_ψ để tính ψ(x)

    # Gọi hàm plot_graph để vẽ đồ thị
    plot_graph(z0, z_values, tan_z, sqrt_term, f_max, x_values, all_ψ_values, z, κ, l)


if __name__ == "__main__":
    main()
