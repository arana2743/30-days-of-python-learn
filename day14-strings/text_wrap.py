import textwrap

# wrap method
string = "This is a very very very very long string"
print(textwrap.wrap(string,8))

# fill method
print(textwrap.fill(string,8))
