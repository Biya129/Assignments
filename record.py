from vehicle import Vehicle

class EntryRecord:
    def __init__(self, entry_time, exit_time, vehicle: Vehicle):
        self.entry_time = entry_time
        self.exit_time = exit_time
        self.vehicle = vehicle 
    
    def vehicle_type(self):
        return self.vehicle.get_vehicle_info()
    
    def wash_info(self):
        return f"Entry Time: {self.entry_time}, Exit Time: {self.exit_time}"