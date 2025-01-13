class Employee:
    def __init__(self, name, id, **kwargs):
        self.name = name
        self.id = id

    def get_info(self):
        return f"Имя: {self.name}, ID: {self.id}"


class Manager(Employee):
    def __init__(self, name, id, departments, **kwargs):
        super().__init__(name, id, **kwargs)
        self.department = departments

    def manage_project(self):
        return f"{self.name} управляет проектом в {self.department}."

    def get_info(self):
        return super().get_info() + f", Отдел: {self.department}"


class Technician(Employee):
    def __init__(self, name, id, specialization, **kwargs):
        super().__init__(name, id, **kwargs)
        self.specialization = specialization

    def perform_maintenance(self):
        return f"{self.name} управляет проектом в {self.specialization}."

    def get_info(self):
        return super().get_info() + f", Специализация: {self.specialization}"


class TechManager(Manager, Technician):
    def __init__(self, name, id, departments, specialization):
        super().__init__(name, id, departments = departments, specialization = specialization)
        self.team = []  # список подчинённых

    def add_employee(self, employee):
        self.team.append(employee)

    def get_team_info(self):
        team_info = [member.get_info() for member in self.team]
        return "Информация о компании:\n" + "\n".join(team_info)

    def get_info(self):
        return super().get_info() + f", Специализация: {self.specialization}"


employee = Employee("Олег", 1)
print(employee.get_info(),"\n")

manager = Manager("Сергей", 2, "Маркетинг")
print(manager.get_info())
print(manager.manage_project(),"\n")

technician = Technician("Андрей", 3, "Разработка")
print(technician.get_info())
print(technician.perform_maintenance(),"\n")

tech_manager = TechManager("Никита", 4, "IT", "Тестировка")
print(tech_manager.get_info())
print(tech_manager.manage_project())
print(tech_manager.perform_maintenance(),"\n")

tech_manager.add_employee(employee)
tech_manager.add_employee(manager)
tech_manager.add_employee(technician)
print(tech_manager.get_team_info())