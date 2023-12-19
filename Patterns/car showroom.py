class Car:
    def __init__(self, model, engine):
        self.model = model
        self.engine = engine

    def display_info(self):
        pass

class Sedan(Car):
    def display_info(self):
        print(f"Sedan: {self.model}, Engine: {self.engine}")

class SUV(Car):
    def display_info(self):
        print(f"SUV: {self.model}, Engine: {self.engine}")

class LuxurySedan(Car):
    def display_info(self):
        print(f"Luxury Sedan: {self.model}, Engine: {self.engine}")

class LuxurySUV(Car):
    def display_info(self):
        print(f"Luxury SUV: {self.model}, Engine: {self.engine}")


class CarFactory:
    def create_sedan(self, model):
        pass

    def create_suv(self, model):
        pass

class EconomyCarFactory(CarFactory):
    def create_sedan(self, model):
        return Sedan(model, "1.6L")

    def create_suv(self, model):
        return SUV(model, "2.0L")

class LuxuryCarFactory(CarFactory):
    def create_sedan(self, model):
        return LuxurySedan(model, "2.0L")

    def create_suv(self, model):
        return LuxurySUV(model, "3.0L")


if __name__ == "__main__":
    economy_factory = EconomyCarFactory()
    luxury_factory = LuxuryCarFactory()

    economy_sedan = economy_factory.create_sedan("Toyota Camry")
    economy_suv = economy_factory.create_suv("Jeep Cherokee")

    luxury_sedan = luxury_factory.create_sedan("Mercedes Benz E-Class")
    luxury_suv = luxury_factory.create_suv("Range Rover")

    economy_sedan.display_info()  
    economy_suv.display_info()    
    luxury_sedan.display_info()   
    luxury_suv.display_info()     
