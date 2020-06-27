class Employee:
    company_name = 'Net Solvents'
    raise_amount = 22
    num_of_employess = 0
    def __init__(self, fname, lname, email, pay):
        # instance variables
        self.fname = fname
        self.lname = lname
        self.email = email
        self.pay = pay

        Employee.num_of_employess += 1

    def fullname(self):
        return ('{} {}'.format(self.fname, self.lname))

    # using class variable : raise_2020 here 
    def apply_raise(self):
        self.pay += int(self.pay * self.raise_amount / 100)

    # adding class methods
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    # adding static methods
    @staticmethod
    def is_workday():

def main():
    emp_1 = Employee('John', 'Test', 'john.test@example.com', 42000)
    emp_2 = Employee('Doe', 'Test', 'doe.test@example.com', 53000)

    # to check all variables for an instance
    # print(emp_1.__dict__)
    # print(emp_2.__dict__)

    # we can also do classname.__dict__ to see all class variables.
    # print(Employee.__dict__)

    print('Numbers of Employees are: {}'.format(Employee.num_of_employess))
    
    print('Employe 1 is {}'.format(emp_1.fullname()))
    print('Employee 2 is {}'.format(emp_2.fullname()))

    # class variables are same for all instances
    print(emp_1.company_name)
    print(emp_2.company_name)

    print('Employee 2 salary: {}'.format(emp_2.pay))
    emp_2.apply_raise()
    print('After raise, Employee 2 salary: {}'.format(emp_2.pay))


    print('Changing the raise amount for employees')
    Employee.set_raise_amt(25)
    emp_2.apply_raise()
    print('Employee 2 salary after new raise: {}'.format(emp_2.pay))



if __name__ == '__main__':
    main()