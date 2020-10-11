# iterators - object in python used to iterate over iterable objects
# like lists, tuples, dicts, sets
# Usage:
# - Iterator object is initialised using iter() method
# - It uses next() method for iteration

# simple iterator example
iterable_value = 'HelloWorld'
iterable_object = iter(iterable_value)

while True:
    try:
        # iterate by calling next
        item = next(iterable_object)
        print(item, end=',')
    except StopIteration:
        # exception will happen when iteration will be over
        break
print('')

# making custom iterator
# An iterable user defined type
class Test:

    # constructor
    def __init__(self, limit, start=10):
        self.limit = limit
        self.start = start

    # called below when iteration is initialised
    def __iter__(self):
        self.x = self.start
        return self
    # to move to next element - __next__ method
    def __next__(self):
        # store current value of x
        x = self.x

        # stop iteration if limit is reached
        if x > self.limit:
            raise StopIteration

        # else increment and return old value
        self.x = x + 1;
        return x

# using our custom iterator
for i in Test(20,10):
    print(i, end=' ')
print(' ')
for i in Test(9):
    print(i, end=' ')
print(' ')
