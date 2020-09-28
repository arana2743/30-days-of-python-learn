# Lists : ordered, mutable, allows duplicate elements
myList = ["banana", "cherry", "apple"]
print(myList)

myList2 = list()
print('Empty list : ' + str(myList2))

myList3 = [5, True, "apple", "apple"]
print(myList3)

if 'apple' in myList3:
  print('apple exists')
else:
  print("apple doesn't exist")

myList3.append("banana")
print("After appending values are: " + str(myList3))

myList3.insert(2, '20')
print("After insert at index 2 : " + str(myList3))


# remove last element
myList3.pop()
print("After pop() values are: " + str(myList3))


# remove specific element
myList3.remove("apple")
print("After remove() method values are : " + str(myList3))


# reverse elements of list
myList3.reverse()
print("After reverse() values are : " + str(myList3))


# clear the complete list
myList2.clear()
print("After clear() method values are : " + str(myList2))


# sort method to sort a list
# to implement sort method we must have same type of elements in list
myList4 = [100, 44, -55, -90]

newList4 = sorted(myList4)
myList4.sort()
print("After sorting values are: " + str(myList4))
print("After sorted() method values are : " + str(newList4))


# short way to create list with same element
myList5 = [222] * 5
print(myList5)


myList52 = [1,2,3,4,5]
# concatenate 2 lists
newList5 = myList5 + myList52
print("After concatenation new list : " + str(newList5))


# slicing of list
myList6 = [1,2,3,4,5,6,7,8,9,10]
myList6a = myList6[4:8]
print("Sliced list : " + str(myList6a))
# another way of slicing
myList6b = myList6[1::3]
print("Sliced list with every 3rd element : " + str(myList6b))


# copying a list
list_org = ["banana", "cherry", "apple"]
list_cpy1 = list_org
# copy() method makes a new copy of list and then assigns to the copy variable
list_cpy2 = list_org.copy()
# slicing method also makes a new copy of list and then assigns to the copy variable
list_cpy3 = list_org[:]

# adding a element to copy 1
list_cpy1.append("lemon")
print("Original list : " + str(list_org))
print("Copy 1 list : " + str(list_cpy1))
print("Copy 2 list : " + str(list_cpy2))
print("Copy 3 list : " + str(list_cpy3))


# list comprehensions
# Example : to square all numbers in a list
a1 = [i for i in range(1,11,1)]
sq_a1 = [i*i for i in a1]
print("Original list : " + str(a1))
print("Squared list : " + str(sq_a1))