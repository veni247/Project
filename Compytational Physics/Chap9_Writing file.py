with open('Chap9_file1.txt', 'w') as file:
    # 1. Write a string to the file
    file.write("Hello!\n")
    file.write("My name is Minh Quang.\n")
    
    # 2. Append more content to the file
    file.write("I am 21 years old.\n")
    
    # 3. Write multiple lines at once
    lines = [
        "This is a file\n",
        "Written by\n",
        "Python\n"
    ]
    file.writelines(lines)
    
    # 4. Write formatted data
    name = "Minh Quang"
    age = 21
    city = "Ho Chi Minh"
    file.write(f"\nFormatted Data:\nName: {name}\nAge: {age}\nCity: {city}\n")
    
    # 5. Write binary data
    binary_data = b'\x00\x01\x02\x03\x04'
    file.write("\nBinary Data (in hex):\n")
    file.write(' '.join(f'{byte:02x}' for byte in binary_data))

print("All data written to 'Chap9_file1.txt'")
