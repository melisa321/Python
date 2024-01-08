from abc import ABC, abstractmethod

class Figure(ABC):
    
    @abstractmethod
    def get_perimeter(self):
        pass

    @abstractmethod
    def get_area(self):
        pass

print(f"Hello , to ja Parent class Figure wywołany z importu macro __name__")    