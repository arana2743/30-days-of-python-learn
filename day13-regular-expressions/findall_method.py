import re

str = "violet joey@gmail.com, blah cat doe@acd-corp.com blah sink"
emails = re.findall(r'[\w\.]+@[\w\.-]+', str)

for email in emails:
    print(email)


str = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'
tuples = re.findall(r'([\w\.-]+)@([\w\.-]+)', str)
print(tuples)  ## [('alice', 'google.com'), ('bob', 'abc.com')]
for tuple in tuples:
    print(tuple[0])  ## username
    print(tuple[1])  ## host
