class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_details(self):
        print("Hello! My name is " + str(self.name) + " and my age is " + str(self.age))


def main():
    person1 = Person('John Doe', 35)
    print(person1.name)
    print(person1.age)
    person1.get_details()

if __name__ == '__main__':
    main()