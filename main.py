from customer import Customer
from worker import Worker
from services import SoapOnly
from services import SoapAndPolish
from services import SoapPolishInnerClean
from record import EntryRecord
from vehicle import Vehicle
from car_record import VehicleRecord

if __name__ == "__main__":
    customer = Customer("Bisma Ali", "biya929@gmail.com", "33%", "2024-09-01")

    car = Vehicle(make="Toyota", color="Red", registration_num="ABC123")
    customer.add_vehicle(car)
    
    worker = Worker("John Doe", "john.doe@gmail.com", position="Manager", salary=50000)
    print(worker.work())
    
    c1 = SoapPolishInnerClean(5500, "Soap, Polish & Inner Clean")
    print(c1.price)
    print(c1.luxury_services) 
    print(c1.apply_deluxe_services())
    
    entry_record = EntryRecord(record_id="001", entry_time="09:00", exit_time="10:00", vehicle_type="Sedan")
    car.set_vehicle_record(entry_record)
    print(entry_record.wash_info()) 
    
    print(car.registration_num)
    print(car.get_vehicle_info())  
    
    vehicle_record = VehicleRecord(vehicle=car, record_id="123ABC", license_plate="ABC123", model="Camry")
    print(vehicle_record.license_plate)
    print(vehicle_record.get_record_info()) 
