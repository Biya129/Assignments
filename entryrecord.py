from vehicle import Vehicle

class EntryRecord:
    def __init__(self, record_id, entry_time, exit_time, vehicle_type):
        self.record_id = record_id
        self.entry_time = entry_time
        self.exit_time = exit_time
        self.vehicle_type = vehicle_type
        self.vehicle = None

    def wash_info(self):
        return f"Vehicle Type: {self.vehicle_type}, Entry Time: {self.entry_time}, Exit Time: {self.exit_time}"