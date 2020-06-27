# building up alternative constructor for class
# using classmethods

class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @classmethod
    # alternative constructor
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)


def main():
    emp_str_1 = 'John-Doe-40000'
    emp_str_2 = 'Marry-Jane-50000'

    emp_1 = Employee.from_string(emp_str_1)
    emp_2 = Employee.from_string(emp_str_2)

    print('Employee 1 name is : {} {}'.format(emp_1.first, emp_1.last))
    print('Employee 2 name is : {} {}'.format(emp_2.first, emp_2.last))


if __name__ == '__main__':
    main()