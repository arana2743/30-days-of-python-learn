class Employee:
    def __init__(self, fname, lname, email, pay):
        self.fname = fname
        self.lname = lname
        self.email = email
        self.pay = pay

    def fullname(self):
        return ('{} {}'.format(self.fname, self.lname))

def main():
    emp_1 = Employee('John', 'Test', 'john.test@example.com', 40000)
    emp_2 = Employee('Doe', 'Test', 'doe.test@example.com', 50000)

    print('Employe 1 is {}'.format(emp_1.fullname()))
    print('Employee 2 is {}'.format(emp_2.fullname()))




if __name__ == '__main__':
    main()