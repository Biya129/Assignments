from customer import Customer
from worker import Worker
from services import SoapOnly, SoapAndPolish, SoapPolishInnerClean
from entryrecord import EntryRecord
from vehicle import Vehicle
from vehiclerecord import VehicleRecord

if __name__ == "__main__":

    vehicle1 = Vehicle(owner="Abdul Wahab", make="Toyota", model="Corolla", color="Red", registration_num="Abdul-1378")
    customer1 = Customer(name="Bisma Ali", email="biya929@gmail.com", vehicle=vehicle1, loyalty_points=450, membership_date="2024-07-09")

    vehicle2 = Vehicle(owner="Usman Ali", make="Honda", model="Civic", color="Blue", registration_num="Jutt-7856")
    customer2 = Customer(name="Iqra Ali", email="iqra442@gmail.com", vehicle=vehicle2, loyalty_points=700, membership_date="2023-10-14")

    worker = Worker(name="Ali Ahmad", email="ahmad112@gmail.com", position="Manager", salary=50000)
    print(worker.work())

    c1 = SoapPolishInnerClean(price=9500, luxury_services="Soap, Polish & Inner Clean")
    print(c1.price)
    print(c1.luxury_services) 
    print(c1.apply_deluxe_services())
    
    entry_record = EntryRecord(customer=customer1, 
                               vehicle=vehicle1, 
                               record_id=101, 
                               entry_time="07:00 PM", 
                               exit_time="8:30 PM",
                               wash_service=c1)
    vehicle1.set_vehicle_record(entry_record)
    print(entry_record.wash_info()) 
    
    print(vehicle1.registration_num)
    print(vehicle1.get_vehicle_info())  

    print(vehicle2.registration_num)
    print(vehicle2.get_vehicle_info())
    
    vehicle_record = VehicleRecord(vehicle=vehicle1, record_id="Biya929", license_plate="AHM-1229", model="Camry")
    print(vehicle_record.license_plate)
    print(vehicle_record.get_record_info()) 

    print(customer1.get_membership_info())
    print(customer2.get_membership_info())