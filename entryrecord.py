from services import SoapOnly, SoapAndPolish, SoapPolishInnerClean
from vehicle import Vehicle

class EntryRecord:
    def __init__(self, customer, vehicle, record_id, entry_time, exit_time, wash_service):
        self.customer = customer
        self.vehicle = vehicle
        self.record_id = record_id
        self.entry_time = entry_time
        self.exit_time = exit_time
        self.wash_service = wash_service


    def vehicle_type(self):
        return f"Vehicle Type: {self.vehicle.make} {self.vehicle.model}"

    
    def wash_info(self):
        return f"Wash Info for {self.vehicle.make} {self.vehicle.model}: Entry Time: {self.entry_time}, Exit Time: {self.exit_time}"
