# closures : a function object that remembers values in enclosing scopes even if they are not present in memory

# nested function - function defined inside another function
# Note: nested functions can access the variables of the enclosing scope
# Exampl1:
def transmit_to_space(message):
    "This is the enclosing function"
    def data_transmitter():
        "The nested function"
        print(message)
    return data_transmitter

print(transmit_to_space("test message"))
# another way
fun2 = transmit_to_space("Burn the Sun!")
fun2()

# Example2 : nonlocal keyword ussage
def print_msg(number):
    def printer():
        "here we are using the nonlocal keyword"
        nonlocal number
        number = 10
        print("Variable inside nonlocal scrope : %s" % number)
    printer()
    print("Variable outside scrope : %s" % number)

print_msg(20)

# Example3:
def multiplier_of(n):
    def multiplier(number):
        return number*n
    return multiplier

multiplywith5 = multiplier_of(5)
print(multiplywith5(9))
