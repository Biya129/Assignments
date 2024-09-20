from tier1 import SoapOnly
from tier2 import SoapAndPolish
from tier3 import SoapPolishInnerClean
from vehicle import Vehicle
from customer import Customer

class EntryRecord:
    def __init__(self, record_id, entry_time, exit_time, wash_service):
        self.customer = Customer("Bisma Ali", "biya929@gmail.com", 450, "2024-07-09")
        self.vehicle = Vehicle("Abdul Wahab", "Toyota", "Corolla", "Red", "Abdul-1378")
        self.record_id = record_id
        self.entry_time = entry_time
        self.exit_time = exit_time
        self.wash_service = wash_service


    def vehicle_type(self):
        return f"Vehicle Type: {self.vehicle.make} {self.vehicle.model}"

    
    def wash_info(self):
        return f"Wash Info for {self.vehicle.make} {self.vehicle.model}: Entry Time: {self.entry_time}, Exit Time: {self.exit_time}"
