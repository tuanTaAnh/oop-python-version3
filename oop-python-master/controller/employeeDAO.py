from model.employee import *

class EmployeeDAO:
    def __init__(self):
       self.employList =  []

    def add_employee(self, employeeID, lastname, firstname, birthdate, photos, notes):
        assert self.__check_unique_id(employeeID), "The id is not unique"

        emp = Employee(employeeID, lastname, firstname, birthdate, photos, notes)
        self.employList.append(emp)

    def get_emp_by_id(self, id):
        for emp in self.employList:
            if emp.get_employeeID() == id:
                return emp
        return None

    def print_emplist(self):
        print("LIST OF EMPLOYEES: ")
        for emp in self.employList:
            print(emp.get_infor())
        print()

    def get_dict_list(self):
        empdictlist = []
        for emp in self.employList:
            empdictlist.append(emp.get_infor_dist())
        return empdictlist


    def __check_unique_id(self, id):
        for emp in self.employList:
            if emp.get_employeeID() == id:
                return False
        return True