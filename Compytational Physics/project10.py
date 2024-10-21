with open('projec10.txt', 'r') as file:
    numbers = file.readlines()


numbers = [float(number.strip()) for number in numbers]
tong = sum(numbers)

print(f"Tổng của các số trong danh sách là: {tong}")
