import re

str = 'example sentence with word:cat'
match = re.search(r'word:\w\w\w', str)

if match:
    print('Found ' + match.group())
else:
    print('did not found')
