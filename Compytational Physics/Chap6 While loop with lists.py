fruits = ["Táo", "Chuối", "Sơ ri", "Cam"]
index = 0
while index < len(fruits):
    print(f"Trái cây thứ {index + 1}: {fruits[index]}")
    index += 1

#Use while to remove elements from a list
while fruits:
    print(f"Đang loại trái {fruits[0]}")
    fruits.pop(0)

print("Danh còn lại:", fruits)

fruits1 = []
fruits2 = ["Táo", "Chuối", "Sơ ri", "Cam"]
# Use while to move fruits from list 'fruits' to 'fruits1'
while fruits2:
    fruit = fruits2.pop(0)
    fruits1.append(fruit)
    print(f"Minh Quang đang đi mua {fruit}")

print(f"Trái cây đã được mua: {fruits1}")
    
