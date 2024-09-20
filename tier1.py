from carwashservice import CarWashService

class SoapOnly(CarWashService):
    def __init__(self, price, basic_services):
        super().__init__(price)
        self.basic_services = basic_services

    def perform_wash(self):
        return f"Performing SoapOnly wash. Services: {self.basic_services}"
    
    
    def apply_basic_services(self):
        return f"Applying basic services: {self.basic_services}"
