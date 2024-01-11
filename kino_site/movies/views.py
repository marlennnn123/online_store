class Employees:
    def init(self, name, salary):
        self.name = name
        self.salary = salary

    def get_info(self):
        return f'Name: {self.name}, salary is {self.salary} som'


class Manager(Employees):
    def init(self, name, salary, department):
        super().init(name, salary)
        self.department = department


    def get_info(self):
        return f'Name: {self.name}, salary is {self.salary} som, department is {self.department}'


    def check(self):
        if self.department == "IT":
            return "Cool"
        else:
            return "Not Cool"


class Intern(Employees):
    def init(self, name, salary, exeperience):
        super().init(name, salary)
        self.exeperience = exeperience


    def countt(self):
        return f'{12 * self.exeperience * self.salary} som'


    def get_info(self):
        return f'Name: {self.name}, salary is {self.salary} som, exeperience is {self.exeperience}'


employ1 = Employees('Nurbek', 33000)
manager1 = Manager('Mirbek', 20000, 'IT')
manager2 = Manager('Asan', 45000, 'Marketing')
intern1 = Intern('Aigul', 20000, 3)

print(employ1.get_info())
print(manager1.get_info())
print(manager1.check())
print(manager2.get_info())
print(manager2.check())
print(intern1.get_info())
print(intern1.countt())