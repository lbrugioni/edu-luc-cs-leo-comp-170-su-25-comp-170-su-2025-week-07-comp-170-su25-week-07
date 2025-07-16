#Create a superclass that holds eveything the vehicles has in common

class Vehicle:
    #Initialize the vehicle with its name and miles per gallon
    def __init__(self,name,mpg):
        self.name=name #Vehicles name 
        self.mpg=mpg #vehicles miles per gallon 
    #Create a method to calculate how much fuel is needed for a certain distance
    def fuel_needed(self,distance):
        fuel=distance/self.mpg #Calculates how much fuel is needed 
        return fuel
    #Create a method describing the vehicle
    def description(self):
        desc=f"{self.name} gets {self.mpg} miles per gallon." #Return a f-strng showing a description of the vehicles name and miles 
        return desc

#Create subclasses of the Superclass, Vehicle.
# This will allow the new classes to inherit from the Vehicle superclass to avoid repetition

class Car(Vehicle):
    def __init__(self):
        #Car has 30 miles per gallon
        super().__init__("Car",30) #use super() to automatically find the parent class

class Truck(Vehicle):
    def __init__(self):
        #Truck has 15 miles per gallon
        super().__init__("Truck",15) 

class Motercyle(Vehicle):
    def __init__(self):
        #Motercycle has 50 miles per gallon
        super(). __init__("Motercycle",50)

class Bus(Vehicle):
    def __init__(self):
        #Bus has 8 miles per gallon
        super().__init__("Bus",8)


#--------------------------------------------------------------------------------#
# ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎  WRITE YOUR CODE ABOVE THIS  LINE ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎

# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓  IF THERE IS ANY CODE BELOW THIS LINE ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓         PLEASE DO NOT MODIFY IF       ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
#--------------------------------------------------------------------------------#

#Testing the code
#Create one of each type of Vehicle
print() #blank line for readabiltiy 
car=Car()
truck=Truck()
motercycle=Motercyle()
bus=Bus()

#Print how much fuel each vehicle needs
print(car.fuel_needed(150))
print(truck.fuel_needed(150))
print(motercycle.fuel_needed(150))
print(bus.fuel_needed(150))
print() #blank line for readabiltiy 

#Print each vehicles description
print(car.description())
print(truck.description())
print(motercycle.description())
print(bus.description())
print() #blank line for readability 


