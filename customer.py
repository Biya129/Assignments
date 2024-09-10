from person import Person

class Customer(Person):
    def __init__(self, name, email, loyalty_points, membership_date):
        super().__init__(name, email)
        self.loyalty_points = loyalty_points
        self.membership_date = membership_date
    
    def make_purchase(self):
        return f"{self.name} makes a purchase."
    
    def get_membership_info(self):
        return f"Membership Date: {self.membership_date}, Loyalty Points: {self.loyalty_points}"
