# exception handling
# example1 : where for loop gets called beyond list length
def do_stuff_with_number(n):
    print(n, end=' ')

def catch_this():
    the_list = (1,2,3,4,5)

    for i in range(10):
        try:
            do_stuff_with_number(the_list[i])
        except IndexError:
            # raised when accessing a non-existing index of a list
            do_stuff_with_number(0)

catch_this()
print('')
