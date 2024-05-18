class vehicle:
    def __init__(self,name,mileage,cost):
        self.name = name
        self.mileage = mileage
        self.cost = cost
    
    def show_details(self):
        print(f"Hello, I am {self.name}")
        print(f"Mileage of the vehicle is: {self.mileage}")
        print(f"Cost of vehicle is: {self.cost}")
    
class car(vehicle):
    def __init__(self,name,mileage,cost, color):
        super().__init__(name,mileage,cost)
        self.color = color

    def show_car(self):
        print("I am a Car")
        print(f"car color: {self.color}")

# v1 = vehicle("Rolls Royal",100,50000000)
# v2 = vehicle("Farrari",150,8000000)
# v1.show_details()
    
c1 = car("Rolls Royal",100,50000000,"Black")
c1.show_details() # Instantiating the object for child class
c1.show_car()     # Invoking the child class method

