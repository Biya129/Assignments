from person import Person

class Customer(Person):
    def __init__(self, name, email, loyalty_points, membership_date):
        super().__init__(name, email)
        self.loyalty_points = loyalty_points
        self.membership_date = membership_date
        self.vehicles = []

    def make_purchase(self):
        self.loyalty_points += 10

    def get_membership_info(self):
        return f"Membership since: {self.membership_date}, Loyalty Points: {self.loyalty_points}"

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)
        vehicle.owner = self

    def get_vehicle_info(self):
        return [vehicle.get_vehicle_info() for vehicle in self.vehicles]
