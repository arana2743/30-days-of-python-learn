msg_template = """
Hello {name} , Thanks for joining {website}.
We are happy to have you with us.
"""

def format_msg(my_name="John", my_website="gitlab.co"):
    my_msg = msg_template.format(name=my_name, website=my_website)
    print(my_msg)

format_msg()

# checking up args and kargs
def base_functions(*args, **kargs):
    print(args, kargs)

base_functions(name="John",website="gitlab")
base_functions("John", "another-one")
