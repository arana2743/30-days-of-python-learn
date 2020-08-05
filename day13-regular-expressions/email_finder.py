import re

# simple try with general use of regex
def email_finder_try1(str):
    match = re.search(r'\w+@\w+', str)
    if match:
        print(match.group())

# use of square brackets
def email_finder_try2(str):
    match = re.search(r'[\w.-]+@[\w.-]+', str)
    if match:
        print(match.group())

def main():
    str = 'violet john-d@gmail.com cat sink'
    email_finder_try1(str)
    email_finder_try2(str)

if __name__ == '__main__':
    main()
