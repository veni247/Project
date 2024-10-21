tuples = ("Minh Quang", 21130243, "Sinh viên VLLT")
print(tuples)
print(len(tuples))
print(type(tuples))
print(tuples[1])
#Change: Because tuples are unchangeable. Therefore, if we want to change the tuple, we need to convert it into a list and change it. After change the list we convert it back into a tuple.
x = list(tuples)
x.append("21 tuổi")
newtuple = tuple(x)
print(newtuple)
#Remove: Use the way like change to remove items in a tuple
y = list(newtuple)
y.remove("21 tuổi")
newtuple1 = tuple(y)
print(newtuple1)
#Add tuple to a tuple
y = ("21 tuổi",)
tuples +=y
print(tuples)
#Loop through a tuple
for x in tuples:
    print(x)

for i in range(len(tuples)):
  print(tuples[i])

i = 0
while i < len(tuples):
  print(tuples[i])
  i = i + 1
#Join two tuples
tuple1 = ("Một", "Hai" , "Ba")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)
#Multiply tuples
tuple4 = tuples*2
print(tuple4)