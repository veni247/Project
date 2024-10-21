student = {
    1: {"Họ và tên": "Phạm Hoàng Minh Quang", "Tuổi":21,"MSSV":21130243,"Chuyên ngành": "Vật lý lý thuyết"},
    2: {"Họ và tên": "Ngô Loan Phụng", "Tuổi": 21, "MSSV": 2182702633, "Chuyên ngành": "Luật kinh tế"}
}
print("In ra các keys trong từ điển:")
for key in student:
    print(key)
print("In ra đầy đủ thông tin: ")
for student_id, student_info in student.items():
    print(f"ID: {student_id}")
    for key, value in student_info.items():
        print(f" {key}: {value}")

#Customize value in dictionary:
for student_id, student_info in student.items():
    student_info["Tuổi"] += 1  # Tăng tuổi thêm 1
    print(f"ID: {student_id}")
    for key, value in student_info.items():
        print(f" {key}: {value}")