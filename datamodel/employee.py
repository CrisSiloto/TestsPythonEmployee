

class Employee(object):

    raise_amount = 1.05

    def __init__(self, id, name, surname, pay):
        super().__init__()
        #super(Employee, self).__init__()
        self._id = id 
        self._name = name
        self._surname = surname 
        self._pay = pay

    def set_id(self, id):
        self._id = id    

    def set_name(self, name):
        self._name = name

    def set_surname(self, surname):
        self._surname = surname

    def set_pay(self, pay):
        self._pay = pay    

    def get_name(self):
        return self._name

    def get_surname(self):
        return self._surname

    def get_id(self):
        return self._id

    def get_pay(self):
        return self._pay    

    id = property(get_id)
    name = property(get_name, set_name)
    surname = property(get_surname, set_surname)
    pay = property(get_pay, set_pay)

    @property
    def email(self):
        return '{}.{}@emailbanca.it'.format(self.name, self.surname)

    @property
    def fullname(self):
        return '{} {}'.format(self.name, self.surname)   

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


    # def __str__(self):
    #     return 'ID number: ' + self.ident + \
    #            '\nName: ' + self.name + \
    #            '\nSurname: ' + self.surname 



      