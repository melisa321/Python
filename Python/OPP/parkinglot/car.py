class Car:
    
    def __init__(self, license_plate, model, color):
        self.license_plate = license_plate
        self.model = model
        self.color = color
  
    def __repr__(self):
        return f'{self.license_plate}, {self.model}, {self.color}'