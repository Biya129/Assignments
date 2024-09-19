from person import Person
from vehicle import Vehicle

class Customer(Person):
    def __init__(self, name, email, vehicle:Vehicle, loyalty_points, membership_date, owner, make, model, color, registration_num):
        super().__init__(name, email)
        self.loyalty_points = loyalty_points
        self.membership_date = membership_date
        self.vehicle = Vehicle(owner, make, model, color, registration_num)

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def make_purchase(self):
        self.loyalty_points += 10

    def get_membership_info(self):
        return f"Customer: {self.name}, Loyalty Points: {self.loyalty_points}, Member since: {self.membership_date} ,{self.vehicle.get_vehicle_info()}"

    def get_vehicle_info(self):
        return self.vehicle.get_vehicle_info()