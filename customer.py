from person import Person
from vehicle import Vehicle

class Customer(Person):
    def __init__(self, name, email, loyalty_points, membership_date):
        super().__init__(name, email)
        self.loyalty_points = loyalty_points
        self.membership_date = membership_date
        self.v = Vehicle("Abdul Wahab", "Toyota", "Corolla", "Red", "Abdul-1378")

    def add_vehicle(self,v):
        self.vehicles.append(v)

    def make_purchase(self):
        self.loyalty_points += 10

    def get_membership_info(self):
        return f"Customer: {self.name}, Loyalty Points: {self.loyalty_points}, Member since: {self.membership_date}"