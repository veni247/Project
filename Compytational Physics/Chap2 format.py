message = "Hello, My name is {}. I am {} years old."
fmessage = message.format("Minh Quang", 21)
print(fmessage)

message = "Hello, My name is {name}. I am {age} years old."
fmessage = message.format(name="Minh Quang", age=21)
print(fmessage)

message = "Hello, My name is {0}. I am {1} years old."
fmessage = message.format("Minh Quang", 21)
print(fmessage)

message = "Hello, My name is {1}. I am {0} years old."
fmessage = message.format("Minh Quang", 21)
print(fmessage)

left_aligned = "{:<10}".format("left")
right_aligned = "{:>10}".format("right")
center_aligned = "{:^10}".format("center")

print(f"|{left_aligned}|")
print(f"|{right_aligned}|")
print(f"|{center_aligned}|")

pi = 3.141592653589793
fpi = "Pi is approximately {:.2f}".format(pi)
print(fpi)

large_number = 12345678910
fnumber = "The number is {:,}".format(large_number)
print(fnumber)

padded_number = "Number: {:05d}".format(52)
padded_spaces = "Number: {:5d}".format(41)

print(padded_number)
print(padded_spaces)
