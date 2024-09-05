class CarWashService:
    def __init__(self, price):
        self.price = price

    def perform_wash(self):
        return "Performing car wash."

class SoapOnly(CarWashService):
    def __init__(self, price, basic_services):
        super().__init__(price)
        self.basic_services = basic_services
    
    def apply_basic_services(self):
        return f"Applying basic services: {self.basic_services}"

class SoapAndPolish(CarWashService):
    def __init__(self, price, extra_services):
        super().__init__(price)
        self.extra_services = extra_services
    
    def apply_premium_services(self):
        return f"Applying premium services: {self.extra_services}"

class SoapPolishInnerClean(CarWashService):
    def __init__(self, price, luxury_services):
        super().__init__(price)
        self.luxury_services = luxury_services
    
    def apply_deluxe_services(self):
        return f"Applying deluxe services: {self.luxury_services}"
