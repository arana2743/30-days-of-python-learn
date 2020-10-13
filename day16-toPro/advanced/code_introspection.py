# Code interospection is ability to check class,function and keywords
# we check what they are, what they do and what they know

# help()
# dir()
# hasattr()
# id()
# type()
# repr() : returns the printable representation of the given object
# callable() : returns True if the object passed is callable else False
# issubclass()
# isinstance()
# __doc__
# __name__

# example1:
class Vehicle:
    name = ""
    kind = "car"
    color = "grey"
    value = 100.00

    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." %(self.name, self.color, self.kind, self.value)
        return desc_str

    def __repr__(self):
        return repr("%s is a %s %s worth $%.2f." %(self.name, self.color, self.kind, self.value))

    def __call__(self):
        print('Callable function Vehicle class.')

# prints all attributes of the Vehicle class
# this will include both variables and methods
print(dir(Vehicle))
name = 'name'
obj1 = Vehicle()
obj2 = Vehicle()
obj1.name = 'mercedes'
obj1.value = 2000.00
obj2.name = 'bmw'
obj2.color = 'black'
obj2.value = 2150.00
print(obj1.description())
print(obj2.description())

# id() method : to check unique id of objects
print("My object id for obj1 is : %s" % id(obj1))
print("My object id for obj2 is : %s" % id(obj2))

# hasattr() method : to check if object has given attribute or not
print("checking is obj1 has attribute named 'value' : %s" % hasattr(obj1,'value'))
print("checking is obj2 has attribute named 'description' : %s" % hasattr(obj2,'description'))

# repr() method : returns the printable representation of the given object
print(repr('Hello'))
print(repr(obj1))
print(repr(obj2))


# callable() method
print('Checking is object obj1 is callable, only because we have added __call__ to the class : %s' %callable(obj1))
def testFunction():
    print("Test")
y = testFunction
print('Checking if y is callable : %s' % callable(y))
# type() method : to check type of object/variable
print(type(obj1))
print(type('HelloWorld'))
