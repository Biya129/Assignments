from person import Person

class Customer(Person):
    def __init__(self, name, email, vehicle, loyalty_points, membership_date):
        super().__init__(name, email)
        self.vehicle = vehicle
        self.loyalty_points = loyalty_points
        self.membership_date = membership_date


    def make_purchase(self):
        self.loyalty_points += 10

    def get_membership_info(self):
        return f"Customer: {self.name}, Loyalty Points: {self.loyalty_points}, Member since: {self.membership_date}"
