class Person:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    
    def update_info(self, name, email):
        self.name = name
        self.email = email
    
    def get_details(self):
        return f"Name: {self.name}, Email: {self.email}."

class Worker(Person):
    def __init__(self, name, email, position, salary):
       super().__init__(name, email)
       self.position = position
       self.salary = salary
        
    def work(self):
       return f"{self.name} is working as a {self.position}"
        
    def get_salary(self):
       return self.salary

class Customer(Person):
    def __init__(self, name, email, loyalty_points, membership_date):
        super().__init__(name, email)
        self.loyalty_points = loyalty_points
        self.membership_date = membership_date
    
    def make_purchase(self):
        return f"{self.name} makes a purchase."
    
    def get_membership_info(self):
        return f"Membership Date: {self.membership_date}, Loyalty Points: {self.loyalty_points}"
