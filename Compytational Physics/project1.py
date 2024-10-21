print("Temperature Conversion")
print("1. Fahrenheit to Celsius")
print("2. Celsius to Fahrenheit")
choice = int(input("Enter your choice: "))
if choice == 1:
    f = float(input("Enter temperature in Fahrenheit: "))
    c = (f - 32) * 5 / 9
    print(f"{f}°F is equal to {c:.2f}°C")
elif choice == 2:
    c = float(input("Enter temperature in Celsius: "))
    f = (c * 9 / 5) + 32
    print(f"{c}°C is equal to {f:.2f}°F")
else:
    print("Invalid choice, please choose either 1 or 2.")
