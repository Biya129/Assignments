class Vehicle:
    def __init__(self, owner, make, model, color, registration_num):
        self.owner = owner
        self.make = make
        self.model = model
        self.color = color
        self.registration_num = registration_num
        self.entry_records = []


    def set_vehicle_record(self, record):
        self.entry_records.append(record)

    def get_vehicle_info(self):
        return f"Vehicle {self.make} {self.model}, Color: {self.color}, Registration: {self.registration_num}"