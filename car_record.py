from vehicle import Vehicle

class VehicleRecord:
    def __init__(self, license_plate, model, vehicle: Vehicle):
        self.license_plate = license_plate
        self.model = model
        self.vehicle = vehicle
    
    def get_service_type(self):
        return f"Service type for {self.model} with plate {self.license_plate}"
    
    def get_vehicle_info(self):
        from vehicle import Vehicle
        return self.vehicle.get_vehicle_info()