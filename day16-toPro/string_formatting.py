# this print out 'Hello, John!'
name = 'John'
print("Hello %s" % name)

# formatting with 2 or more arguments
# we use typle of variables
name1 = 'Dug'
age = 29
print("%s is %d years old" % (name1, age))

# some of the basic argument specifiers
# %s - String(or any object with a string representation, like numbers)
# %d - Integers
# %f - Floating point numbers
# %.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot
# %x or %X - Integers in hex representation (lowercase or uppercase)


# example
data = ("John", "Doe", 60.89)
format_string = "Hello %s %s. Your current balance is $%s."

print(format_string % data)
