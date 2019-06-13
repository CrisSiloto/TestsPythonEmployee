import unittest
import datamodel.department as dep
import datamodel.employee as emp


class TestDepartment(unittest.TestCase):
        # in un atro file di test
    def test_constructor(self):
        d = dep.Department('IT_Department')
        
        self.assertEqual(d.depto_name, 'IT_Department')
        

    def test_add_empl(self):  
        d = dep.Department('IT_Department')
        d.add_employee('11-111','Mario', 'Ricci', 1000)
        d.add_employee('22-222','Claudia', 'Rui', 1100)
        d.add_employee('33-333','Mariana', 'De Angeli', 1540)
        d.add_employee('44-444','Anna', 'Battistela', 990)
        d.add_employee('55-55', 'Irina', 'Vitti', 1300)

    def test_get_employee(self):
        d = dep.Department('IT_Department')
        e1 = d.add_employee('11-111','Mario', 'Ricci', 1000)
        #self.assertEqual(d.get_employee(id), '11-111')
        if d.get_employee('id') != None:
           print("Yes, 'id' key exists in emp_map")    
        else:
           print("No, 'id' key does not exists in emp_map")   


    # def test_get_employee_id_list(self):
    #     emp_map.keys()
    #     e1 = get_employee_id_list(emp_map)
    #     print(e1)
  
    def test_employee(self):
        employee = {"id": "11-111", "name": "Mario", "surname": "Ricci"}
        print(employee["surname"])
        print(employee["id"])
        print(employee["name"])
        

    # def test_get_employee(self):
    #     d = dep.Department('IT_Department')
    #       for id in d.emp_map[id]
    #           print(d.emp_map[id])

    
    # def test_iter(self):
    #     d = dep.Department("MyDepartment")
    #     # for e in d.iter():
    #     #    print(e.name)
    #     # for e in iter(d):
    #     #    print(e.name)

if __name__ == '__main__':
    unittest.main()  