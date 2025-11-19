from abc import ABC, abstractmethod


class Employee(ABC):
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary

    @abstractmethod
    def calculate_total_salary(self):
        pass

    def __str__(self):
        return f"Employee Name={self.name} ,base_salary={self.base_salary}"


    def __lt__(self, other):
        return self.calculate_total_salary() > other.calculate_total_salary()


class Developer(Employee):
    def __init__(self, name, base_salary, num_bugs_fixed):
        super().__init__(name, base_salary)
        self.num_bugs_fixed = num_bugs_fixed


    def calculate_total_salary(self):
        bonus = self.num_bugs_fixed * 50
        return bonus+self.base_salary

    def __str__(self):
        return f"Developer name={self.name},salary={self.base_salary}"



class Manager(Employee):
    def __init__(self, name, base_salary, num_projects_managed):
        super().__init__(name, base_salary)
        self.num_projects_managed = num_projects_managed

    def calculate_total_salary(self):
        bonus = self.num_projects_managed * 1200
        return self.base_salary + bonus


    def __str__(self):
        return f"Developer name={self.name},salary={self.base_salary}"


if __name__ == "__main__":
    dev = Developer("Ahmed", 5000, 10)
    mgr = Manager("Marwan", 8000, 3)
    dev2 = Developer("Mahmoud", 6000, 5)

    print(dev)
    print("Total Salary:", dev.calculate_total_salary())

    print(dev2)
    print("Total Salary:", dev2.calculate_total_salary())

    print(mgr)
    print("Total Salary:", mgr.calculate_total_salary())

    sorted_employees = sorted([dev, mgr, dev2])
    print("Employees sorted by total salary (descending):")
    for emp in sorted_employees:
        print(f"{emp.name}: {emp.calculate_total_salary()}")

