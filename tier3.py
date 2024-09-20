from carwashservice import CarWashService

class SoapPolishInnerClean(CarWashService):
    def __init__(self, price, luxury_services):
        super().__init__(price)
        self.luxury_services = luxury_services

    def perform_wash(self):
        return f"Performing SoapPolishInnerClean wash. Services: {self.luxury_services}"    
    
    def apply_deluxe_services(self):
        return f"Applying deluxe services: {self.luxury_services}"

