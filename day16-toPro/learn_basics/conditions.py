x = 10
print(x == 10) # prints out True
print(x == 11) # prints out False
print(x < 12) # prints out True

# boolean operators
name = 'John'
age = 25
if name == 'John' and age == 25:
    print('Your name is %s, and you are also %d years old' % (name, age))
else:
    print("Meh!, record doesn't exist")

# in operator
name = 'rick'
if name in ['John', 'Rick']:
    print('Your name is found in our db')
else:
    print('Nope, did you ever registered with us?')

# is operator
# unlike == , the "is" operator does not match the values of the variables, but the instances themselves.
x = [1,2,4]
y = [1,2,4]
print(x == y) # prints out True
print(x is y) # prints out False
