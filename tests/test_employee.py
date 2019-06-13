import unittest
#from . import employee as emp
#from . import department as dep
#from datamodel import employee as emp
#from datamodel import department as dep

import datamodel.employee as emp
import datamodel.department as dep

class TestEmployee(unittest.TestCase):

    def test_constructor(self):
        e = emp.Employee('11-111', 'Mario', 'Ricci', 1000)
        print("Employee Id:{} \nName:{} \nSurname:{} \nPay:{}".format(e.id, e.name, e.surname, e.pay))
        self.assertEqual(e.id, '11-111')
        self.assertEqual(e.name, 'Mario')
        self.assertEqual(e.surname, 'Ricci')
        self.assertEqual(e.pay, 1000)

    def test_set_id(self):
        e = emp.Employee('11-111', 'Mario', 'Ricci', 1000)
        i = e.id
        self.assertEqual(i, '11-111')    

    def test_set_name(self):
        e = emp.Employee('22-222', 'Claudia', 'Rui', 1100)
        n = e.name
        self.assertEqual(n, 'Claudia')

        e.name = 'Cristina'

        updated_n = e.name
        self.assertEqual(updated_n, 'Cristina')

    def test_set_surname(self):
        e = emp.Employee('33-333', 'Marina', 'De Angeli', 1200)
        s = e.surname
        self.assertEqual(s, 'De Angeli')

    def test_get_id(self):
        e = emp.Employee('11-111', 'Mario', 'Ricci', 1000)
        self.assertEqual(e.get_id(), '11-111')


    def test_get_name(self):
        e = emp.Employee('22-222', 'Claudia', 'Rui', 1100)
        self.assertEqual(e.get_name(), 'Claudia')
        self.assertNotEqual(e.get_name(), 'Giulietta')

    def test_get_surname(self):
        e = emp.Employee('22-222', 'Anna', 'Fiorini', 1250)
        self.assertEqual(e.get_surname(), 'Fiorini')
        self.assertEqual(e.get_surname(), 'Dolce' )   

    def test_email(self):
        e = emp.Employee('22-222', 'Anna', 'Fiorini', 1250)
        e1 = emp.Employee('44-444', 'Claudia', 'Rui', 1100)

        self.assertEqual(e.email,'Anna.Fiorini@emailbanca.it')
        self.assertEqual(e1.email,'Claudia.Rui@emailbanca.it')
        self.assertEqual(e1.email, 'Isabella.Cielo@emailbanca.it')

    def test_fullname(self):
        e = emp.Employee('55-555', 'Isabella', 'Cielo', 1980)
        e1 = emp.Employee('33-333', 'Marina', 'Rossi', 1450)

        self.assertEqual(e.fullname, 'Isabella Cielo')
        self.assertEqual(e1.fullname, 'Marina Rossi')   
        self.assertEqual(e1.fullname, 'Marina De Angeli') 

    def test_apply_raise(self):
        e = emp.Employee('55-555', 'Isabella', 'Cielo', 5000)
        e1 = emp.Employee('33-333', 'Marina', 'Rossi', 6000)

        e.apply_raise()
        e1.apply_raise()

        self.assertEqual(e.pay, 5250)      
        self.assertEqual(e1.pay, 6300)    
     

if __name__ == '__main__':
    unittest.main()        

