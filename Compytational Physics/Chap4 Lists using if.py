List1 = [i for i in range(0,51) if i%2 == 0]
print("Các số chẵn trong khoảng từ 1 đến 50 là:")
print(List1)
for num in List1:
    if num > 10:
        print(f"{num} là các số chẵn lớn hơn 10")
List2 = [num for num in List1 if num > 25]
print("Các số chẵn lớn hơn 25 là:")
print(List2)
