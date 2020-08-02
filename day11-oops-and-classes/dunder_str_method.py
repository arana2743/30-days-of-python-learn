class Dog:
    spieces = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # can be used as descirption method to print details of instance
    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"

def main():
    charlie = Dog("Charlie", 3)
    print(charlie)

    miles = Dog("Miles", 4)
    print(miles)

if __name__ == '__main__':
    main()
