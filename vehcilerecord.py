from vehicle import Vehicle

class VehicleRecord:
    def __init__(self, vehicle, record_id, license_plate, model):
        self.vehicle = vehicle
        self.record_id = record_id
        self.license_plate = license_plate
        self.model = model

    def get_record_info(self):
        return f"Record ID: {self.record_id}, License Plate: {self.license_plate}, Model: {self.model}"

    def get_vehicle_info(self):
        return self.vehicle.get_vehicle_info()