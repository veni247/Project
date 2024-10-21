text=f"My full name is Phạm Hoàng Minh Quang"
print(text)
price = 5
tax=0.05
txt=f"The price is {price} dollars"
print(txt)
a=f"The price is {price:.2f} dollars"
print(a)
b=f"The price is {price + (price * tax)} dollars"
print(b)
c=f"It's very {'Expensive' if price>5 else 'Cheap'}"
print(c)
print('Tên={0}, Họ={1}'.format('Quang', 'Phạm'))
print("My\nname\nis\nMinh\nQuang")