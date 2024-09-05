class Vehicle:
    def __init__(self, make, color, registration_num):
        self.make = make
        self.color = color
        self.registration_num = registration_num
    
    def get_vehicle_info(self):
        from car_record import VehicleRecord
        return f"Make: {self.make}, Color: {self.color}, Registration Number: {self.registration_num}"