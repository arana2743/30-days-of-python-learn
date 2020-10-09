astring = "Hello world!"
astring2 = 'Hello world!'
print(astring)
print(astring2)

# use of single and double quotes for strings
print("single quotes are ' '")

# find len of string
print('Length of astring variable is : %d' % len(astring))

# find the index of a character in string
print("Index of o in astring varaible is : %d" % astring.index('o'))

# find occurrence of character in string
print("character l occurs %d times in astring variable." % astring.count('l'))

# string splicing
astring3 = 'High Octane fuel'
print("spliced string is '%s'." % astring3[5:11])

# reverse a string
print(astring3[::-1])

# all lowercase or uppercase in string
print(astring3.upper())
print(astring3.lower())

# startswith and endswith methods for string
newstring = 'Hello world'
print(newstring.startswith('Hello'))
print(newstring.endswith('world!'))

# split method
print(newstring.split(' '))
