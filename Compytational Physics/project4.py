cot1 = [round(-10 + i * 2.2, 2) for i in range(10)]
cot2 = [i for i in range(51, 71, 2)]
cot3 = [4 ** i for i in range(10)]

print(f"{'Cột 1':>10} | {'Cột 2':>10} | {'Cột 3':>15}")
print("-" * 40)

for i in range(10):
    print(f"{cot1[i]:>10.2f} | {cot2[i]:>10} | {cot3[i]:>15}")
