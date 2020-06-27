# f-strings
name = "John"
print(f'Hello {name}, this is awesome')

names = ["John", "Catherine", "Elliot"]
for name in names:
    print(f'Hello {name}, hello friend')


template = """
Hello {name}
Thanks for joining!!!
We hope you enjoy this journey with us
"""
name="Doe"
print(template.format(name=name))

another_str = "Hello \
there"
print(another_str)

print("http:\\\\thisisawesome")

# change format of float to only have upto 2 decimals
pi = 3.14523423
print("value of pi upto 3 decimals points: {:.4f}".format(pi))
