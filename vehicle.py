class Vehicle:
    def __init__(self, make, color, registration_num):
        self.make = make
        self.color = color
        self.registration_num = registration_num
        self.entry_records = []  
        self.owner = None

    def set_vehicle_record(self, record):
        self.entry_records.append(record)

    def get_vehicle_info(self):
        owner_name = self.owner.name if self.owner else "No owner"
        return f"Make: {self.make}, Color: {self.color}, Reg No: {self.registration_num}, Owner: {owner_name}"