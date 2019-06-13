import datamodel.employee as emp


class Department(object):

    def __init__(self, depto_name):
        super().__init__()
        #super(Department, self).__init__()
        self.depto_name = depto_name
        self.emp_map = {}

    def add_employee(self, id, name, surname, pay):
        #assert helps code debugging
        #Assert is a run-time check of any condition.
        #If the condition is not true, an AssertionError exception occurs and the program stops.
        assert id is not None
        assert isinstance(id, str)
        assert isinstance(name, str)
        assert isinstance(surname, str)
        assert isinstance(pay, int)
        self.emp_map[id] = emp.Employee(id, name, surname, pay)

    def set_depto_name(self, depto_name):
        self.depto_name = depto_name

    def get_depto_name(self):
        return self.depto_name

    def get_employee(self, id):
        return self.emp_map[id]

    def get_employee_id_list(self):
        self.emp_map.keys()
