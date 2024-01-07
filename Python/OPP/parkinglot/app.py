
from car import Car
from garage import Garage

# class App:
my_garage = Garage()
print(my_garage.spots_available())
my_garage.add_car(Car('LVG34', 'Ferrari', 'Red'))
my_garage.add_car(Car('UTEV3', 'Porsche', 'Blue'))
my_garage.add_car(Car('LVG34', 'Optra', 'Red'))
my_garage.cars_in_garage()
print(my_garage.remove_car('A1', '10'))
print(my_garage.spots_available())