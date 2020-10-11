# importing my custom package named : my_package
from my_package import bar

bar.bar_print()

# to check all function listed in a bar module from custom package
print(dir(bar))

# another example
# to find all functions re module which containe the word 'find'
import re
find_members = []
total_members = dir(re)
for member in total_members:
    if 'find' in member:
        find_members.append(member)
print("And the members which containe 'find' keyword are : %s" % find_members)
