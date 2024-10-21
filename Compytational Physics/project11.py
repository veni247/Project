with open('6times.dat', 'w') as file:
    for i in range(1, 11):
        result = 6 * i
        file.write(f"6 x {i} = {result}\n")

print("Bảng cửu chương 6 đã được ghi vào tệp 6times.dat")
