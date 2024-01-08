
from car import Car
from garage import Garage

my_garage = Garage()
print("Initial spots available: ", my_garage.spots_available())
my_garage.add_car(Car('LVG34', 'Ferrari', 'Red'))
my_garage.add_car(Car('UTEV3', 'Porsche', 'Blue'))
my_garage.add_car(Car('LVG34', 'Opel', 'Red'))
my_garage.cars_in_garage()
print(my_garage.remove_car('A1', '10'))
print("Spots available after remove: ", my_garage.spots_available())
my_garage.add_car(Car('AVG36', 'Fiat', 'Orange'))
print("Spots available after add: ", my_garage.spots_available())
my_garage.cars_in_garage()