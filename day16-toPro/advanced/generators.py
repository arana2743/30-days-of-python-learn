import random

def lottery():
    for i in range(6):
        yield random.randint(1,50)

    yield random.randint(1,10)

for random_number in lottery():
    print('And the next number is... %d!' % random_number)

# another example : simple generator function
def simpleGeneratorFun():
    yield 1
    yield 2
    yield 3

# now calling generator function
for value in simpleGeneratorFun():
    print(value)

# another way of calling generator function
x = simpleGeneratorFun()
print(x.__next__())
print(x.__next__())
print(x.__next__())
