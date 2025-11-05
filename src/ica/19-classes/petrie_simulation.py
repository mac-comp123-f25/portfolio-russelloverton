"""
Contains a simulation of the Petrie Multiplier that is based on classes.
"""

import random
import math

PCT_SEXIST = .2

class Employee:
    """
    For this simulation, we only focus on the gender of an employee and on
    whether this employee is likely to make negative statements
    towards the other gender.
    """

    def __init__(self, gender: str, will_comment):
        """
        Takes in the employee's gender and whether they comment, and it
        saves those values to instance variables. It also initializes the
        variable that holds the comments received by this employee to zero.
        """
        self.gender = gender
        self.will_comment = will_comment
        self.comments_received = 0

    def set_commenter_status(self, comment_status):
        self.will_comment = comment_status

    def receive_sexist_comment(self):
        self.comments_received += 1

    def get_gender(self):
        return self.gender

    def get_commenter_status(self):
        return self.will_comment

    def get_comments_received(self):
        return self.comments_received

    def __str__(self):
        """
        Produces a printable string format for this employee.
        """
        return (self.gender.rjust(5)
                + ": "
                + str(self.comments_received)
                + " sexist comments received."
                + " Commenter Status: "
                + str(self.will_comment))


def print_employee_list(lst):
    """
    Given a list of employees, this method will print the details of each employee
    by using the print() method
    """
    for employee in lst:
        print(employee)


def create_employees(total_num):
    """
    Takes in the number of employees to make, builds and returns a list that contains
    that many employees. It ensures that ~80% are men and the rest women.
    """
    for i in range(total_num):
        num_men = math.ceil(total_num * 0.8)
        if i < num_men:
            gender = 'Man'
            num_men += 1
        elif total_num > i >= num_men:
            gender = 'Woman'
        will_comment = False
        employee = Employee(gender, will_comment)
        lst.append(employee)
    return lst


def create_commenters(lst, PCT_SEXIST):
    """
    Given a list of employees, make 20% of each gender be sexist employees. This
    method should not return anything.
    """
    # TODO: Implement this function then remove this line
    for employee in lst:
        employee.set_commenter_status(random.random() < PCT_SEXIST)


def generate_comments(lst):
    """
    Given a list of employees, have each sexist employee give one sexist comment to
    another employee of the opposite gender, chosen randomly. This method should
    not return anything
    """
    men = []
    women = []
    for employee in lst:
        if employee.get_gender() == 'Man':
            men.append(employee)
        else:
            women.append(employee)
    for man in men:
        if man.get_commenter_status():
            woman = women[random.randint(0, len(women) - 1)]
            woman.receive_sexist_comment()

    for woman in women:
        if woman.get_commenter_status():
            man = men[random.randint(0, len(men) - 1)]
            man.receive_sexist_comment()


def average_comments(lst):
    """
    Returns a tuple that represents the average amount of comments received for men and women
    respectively. Return statement will be in the form (<avg_for_men>, <avg_for_women>)
    """
    # TODO: Implement this function then remove this line
    men = 0
    women = 0
    men_comments_received = 0
    women_comments_received = 0
    for employee in lst:
        if employee.get_gender() == 'Man':
            men_comments_received += employee.get_comments_received()
            men += 1
        else:
            women_comments_received += employee.get_comments_received()
            women += 1

    return (men_comments_received / men, women_comments_received / women)

def main():
    """
    Print out information about the average comments
    received by men and women after a simulation has been run
    """
    num_employees_to_generate = 100
    num_comment_rounds = 50

    employee_list = create_employees(num_employees_to_generate)
    create_commenters(employee_list, PCT_SEXIST)
    for rounds in range(num_comment_rounds):
        generate_comments(employee_list)

    (men_avg, women_avg) = average_comments(employee_list)
    print("  Men received on average ",   men_avg, "sexist comments")
    print("Women received on average ", women_avg, "sexist comments")


if __name__ == "__main__":
    "<----- Test code for print_employee_list ----->"
    lst = [Employee('Man', True),
           Employee('Man', False),
           Employee('Woman', True),
           Employee('Woman', False)]
    print_employee_list(lst)

    "<----- Test code for create_employees ----->"
    employees = create_employees(10)
    print_employee_list(employees)

    "<----- Test code for create_commenters ----->"
    create_commenters(employees, PCT_SEXIST)
    print_employee_list(employees)

    "<----- Test code for generate_comments ----->"
    generate_comments(employees)
    print_employee_list(employees)

    "<----- Test code for average_comments ----->"
    print(average_comments(employees))

    "<----- Run the simulation ----->"
    main()  # <-- KEEP THIS, Uncomment it after implementing all the functions
