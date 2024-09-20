from carwashservice import CarWashService

class SoapAndPolish(CarWashService):
    def __init__(self, price, extra_services):
        super().__init__(price)
        self.extra_services = extra_services

    def perform_wash(self):
        return f"Performing SoapAndPolish wash. Services: {self.extra_services}"    
    
    def apply_premium_services(self):
        return f"Applying premium services: {self.extra_services}"