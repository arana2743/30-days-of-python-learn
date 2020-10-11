# class creation
class MyClass:
    variable = 'blah'

    def function(self):
        print('This is a message inside the class!')

# object creation
myobjectx = MyClass()
myobjecty = MyClass()
# calling class function
myobjectx.function()
# calling class variable
print(myobjectx.variable)
myobjecty.variable = 'yackcity'
print(myobjecty.variable)
