from person import Person

class Worker(Person):
    def __init__(self, name, email, position, salary):
       super().__init__(name, email)
       self.position = position
       self.salary = salary
        
    def work(self):
       return f"{self.name} is working as a {self.position}"
        
    def get_salary(self):
       return self.salary