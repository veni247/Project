Student = {
    "Tên": "Phạm Hoàng Minh Quang",
    "Tuổi": 21,
    "Chuyên ngành": "Vật lý lý thuyết"
}
print("THÔNG TIN SINH VIÊN")
print("Họ và tên", end=": ")
print(Student["Tên"])
print("Tuổi", end=": ")
print(Student["Tuổi"])
print("Chuyên ngành", end=": ")
print(Student["Chuyên ngành"])

#Add information into dictionary:
Student["GPA"] = 8.357
print("GPA", end=": ")
print(Student["GPA"])

#Delete a information in dictionary
del Student["GPA"]
print("Thông tin sau lệnh xóa:")
for key, value in Student.items():
    print(f"{key}: {value}")