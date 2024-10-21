mylist=["Toán","Lý","Hóa"]
print(mylist)
print(len(mylist))
print(type(mylist))
print(mylist[-1])
#Changable: List can be change, add and remove items in a list after it had been created
mylist[-1] = "Anh"
print(mylist)
mylist.insert(1,"Hóa")
print(mylist)
mylist.append("Sinh")
print(mylist)
mylist.remove("Sinh")
print(mylist)
mylist.pop(1)
print(mylist)
mylist.clear()
print(mylist)
del mylist
#Loop through a list
list=["A","B","C"]
for x in list:
    print(x)
for i in range(len(list)):
    print(list[i])
i = 0
while i < len(list):
    print(list[i])
    i=i+1
[print(x) for x in list]
newlist = [x for x in range(10) if x < 5]
newlist.sort()
print(newlist)
newlist.sort(reverse = True)
print(newlist)
#Join two list
list3= newlist + list
print(list3)
