class Vehicle():
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def get_info(self):
        return(f"{self.make}, {self.model}")

class Car(Vehicle):
    def __init__(self, make, model, fuel_type):
        Vehicle.__init__(self, make, model)
        self.fuel_type = fuel_type

    def get_info(self):
        return(f"{self.make}, {self.model}, {self.fuel_type}")

vehi = Vehicle("Audi","R8")
carr = Car("Audi","R8","95")

print(vehi.get_info())
print(carr.get_info())