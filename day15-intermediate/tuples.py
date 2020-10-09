# Tuple: ordered, immutable, allows duplicate elements
myTuple = ("max", 28, "Boston")
print(myTuple)

# defina a tuple with only single element
myTuple1 = ("Single") # wrong way
print(type(myTuple1))
myTuple1 = ("Single",) # correct way
print(type(myTuple1))

# creating tuple with tuple() method
myTuple2 = tuple(["Matt", 30, "New York"])
print(myTuple2)

# count times a element occurs in tuple
myTuple3 = ('a', 'p', 'p', 'l', 'e')
print("p occurs {} times in word apple.".format(myTuple3.count('p')))

# slicing in tuples - works same as lists
myTuple4 = (1,2,3,4,5,6,7,8,9,10)
myTuple4_sliced = myTuple4[2:5]
print("Sliced tuple is : " + str(myTuple4_sliced))


# tuples are also more efficient for using than lists
# below example shows execution times for tuple and list
import timeit
print(timeit.timeit(stmt="[0,1,2,3,4,5,6]", number=1000000000))
print(timeit.timeit(stmt="(0,1,2,3,4,5,6)", number=1000000000))

