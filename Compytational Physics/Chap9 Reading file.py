# Reading
with open('Chap9_file.txt', 'r') as file:
    content = file.read()

print("File content:")
print(content)

# Read the file line by line
with open('Chap9_file.txt', 'r') as file:
    for line in file:
        print(line.strip())

# Read the file into a list of lines
with open('Chap9_file.txt', 'r') as file:
    lines = file.readlines()

print("Lines in the file:")
for line in lines:
    print(line.strip())

# Read a specific number of characters from the file
with open('Chap9_file.txt', 'r') as file:
    content = file.read(10)

print("First 10 characters:")
print(content)

# Read specific parts of the file
with open('Chap9_file.txt', 'r') as file:
    file.seek(0)
    print("First 5 characters:")
    print(file.read(5))

    file.seek(10)
    print("Next 10 characters:")
    print(file.read(10))
