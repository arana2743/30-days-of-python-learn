# sets are lists with no duplicate entries
print(set("my name is John and John is my name".split()))


# example1
a = set(["Jake", "John", "Eric", "Drake"])
b = set(["John", "Jill"])

# intersection method on sets
print("Employees who attended both events : %s" % a.intersection(b))
print("Employees who attended both events : %s" % b.intersection(a))

# symmetric_difference on sets
print("Employees who attended only one of the events : %s" % a.symmetric_difference(b))
print("Employees who attended only one of the events : %s" % b.symmetric_difference(a))

# difference method
print("Employees who attended only a event and not b : %s" % a.difference(b))
print("Employees who attended only b event and not a : %s" % b.difference(a))
