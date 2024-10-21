from Chap8_info import person

def main():
    person1 = person(name="Minh Quang",age=21)
    person2 = person(name="Loan Phụng",age=21)
    print(person1.greet())
    print(person1)
    print(person2.greet())
    print(person2)
if __name__ == "__main__":
    main()