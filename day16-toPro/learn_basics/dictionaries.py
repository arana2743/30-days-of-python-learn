# dictionary example
phonebook = {
    "John": 938477566,
    "Jack": 938377264,
    "Jill": 947662781
}
print(phonebook)

# iterate over a dictionary
for name,number in phonebook.items():
    print("Phone number of %s is %d" % (name,number))

# removing a value in dictionary
del phonebook['John']
print(phonebook)
# or using pop method
phonebook.pop('Jack')
print(phonebook)

# adding a value in dictionary
phonebook['Jake'] = 938273443
print(phonebook)
