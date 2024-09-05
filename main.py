from person import Customer
from person import Worker 
from services import SoapOnly
from services import SoapAndPolish
from services import SoapPolishInnerClean
from record import EntryRecord
from vehicle import Vehicle
from car_record import VehicleRecord

customer = Customer("Bisma Ali", "biya929@gmail.com", "33%", "2024-09-01")
worker = Worker("Ali Ahmad", "Ali129@gmail.com","Cleaner", 33000)

print(worker.work())   

c1=SoapPolishInnerClean(5500,"Soap, Polish & Inner Clean")
print(c1.price)
print(c1.luxury_services)
print(c1.apply_deluxe_services())

entry_record = EntryRecord("09:00", "10:00", Vehicle)
print(entry_record.wash_info())

vehicle = Vehicle("Toyota", "Red", "123ABC")
print(vehicle.registration_num)
print(vehicle.get_vehicle_info())

vehicle_record = VehicleRecord("123ABC", "Camry", vehicle)
print(vehicle_record.license_plate)
print(vehicle_record.get_service_type())
print(vehicle_record.get_vehicle_info())