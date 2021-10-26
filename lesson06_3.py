class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

class Position(Worker):
        def get_full_name(self):
            info = "{0} {1}".format(self.name, self.surname)
            return info
        def get_total_income(self):
            return self._income['wage'] + self._income['bonus']

employee = Position("Nik", "Odent", "engineer", 80000, 10000)
print(employee.name)
print(employee.surname)
print(employee.position)
print(employee._income)
print(employee.get_full_name())
print(f'Total incom: ', employee.get_total_income())
