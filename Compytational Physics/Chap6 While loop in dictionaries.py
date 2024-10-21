students = {
    1: {"Họ và tên": "Phạm Hoàng Minh Quang", "Tuổi": 21},
    2: {"Họ và tên": "Ngô Loan Phụng", "Tuổi": 21},
}


keys = list(students.keys())

# Browse through each student and print information
index = 0
while index < len(keys):
    student_id = keys[index]
    student_info = students[student_id]
    
    print(f"ID: {student_id}")
    for key, value in student_info.items():
        print(f" {key}: {value}")
    
    index += 1

# Using while with dictionary to plus age by 1
index1 = 0
while index1 < len(keys):
    student_id = keys[index1]
    students[student_id]["Tuổi"] += 1
    index1 += 1
print(students)



# Find a information in dictionary
search_id = 1
found = False
index2 = 0

while index2 < len(keys):
    student_id = keys[index2]
    if student_id == search_id:
        student_info = students[student_id]
        print(f"Thông tin sinh viên với ID {search_id}: {student_info}")
        found = True
        break
    index2 += 1

if not found:
    print(f"Không tìm thấy sinh viên với ID {search_id}.")

# Delete an element in dictionary
index3 = 0

while index3 < len(keys):
    student_id = keys[index3]
    if students[student_id]["Tuổi"] <= 25:
        del students[student_id]
        keys = list(students.keys())
    else:
        index3 += 1

print(students)