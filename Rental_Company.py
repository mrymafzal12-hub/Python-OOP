from abc import ABC, abstractmethod
class Vehicle(ABC): # Abstract Class

    def __init__(self, brand, model,hours,name,id): #Step 3
        self.brand = brand
        self.model = model
        self.hours = hours
        self.name = name
        self.id = id
    def display(self):  # Step 5
        print("=== Renting Slip ===")
        print(f"Rented To : {self.name}")
        print(f"Id : {self.id}")
        print(f"Vehicle_Name : {self.brand}")
        print(f"Model : {self.model}")
        print(f"Hours : {self.hours}")

    @abstractmethod   # Abstraction
    def rent(self):   # Step 4
        pass
class Bike(Vehicle):  # Inheritance
    hourly_rent=2000
    def rent(self):    # rent() is overridden in every class showing Polymorphism
        super().display()
        rent= self.hourly_rent * self.hours
        return rent

class Car(Vehicle):  # Inheritance
    hourly_rent=5000
    def rent(self):
        super().display()
        rent = self.hourly_rent * self.hours
        return rent

class Truck(Vehicle):  # Inheritance
    hourly_rent=10000
    def rent(self):
        super().display()
        rent= self.hourly_rent * self.hours
        return rent
class Luxury(Car): # Multilevel Inheritance
    Luxury_Tax = 1000
    def rent(self):
        r=super().rent () + self.Luxury_Tax
        return r


def show():# Step 2
   a = input("Enter Vehicle Brand:").upper()
   b = input("Enter  Model:").upper()
   d = int(input("Enter  Hours:"))
   t=input("Enter Your Name:")
   q=input("Enter Your CNIC:")
   return a,b,d,t,q

print("----Rental Company----")  #  Step 1
print(f"{'1. Bike':<15}2000 Rs/hr")
print(f"{'2. Car':<15}5000 Rs/hr")
print(f"{'3. Truck':<15}10000 Rs/hr")
vehicle_type=input("What do you want to rent out ?\n").upper()
if vehicle_type=="BIKE":

    Brand,Model,Hrs,Name,ID=show()
    bike=Bike(Brand,Model,Hrs,Name,ID)
    print(f"Rent is : {bike.rent()}") # Step 6

elif vehicle_type=="CAR":

     g=input("Enter Class:").upper()
     if g == "LUXURY":
         Brand, Model, Hrs, Name, ID = show()
         luxury=Luxury( Brand,Model,Hrs,Name,ID)
         print(f"Rent is : {luxury.rent()}") #Step 6

     elif g == "BASIC":

         Brand, Model, Hrs, Name, ID = show()
         car=Car( Brand,Model,Hrs,Name,ID)
         print(f"Rent is : {car.rent()}") #Step 6

elif vehicle_type=="TRUCK":

    Brand, Model, Hrs, Name, ID=show()
    truck=Truck( Brand,Model,Hrs,Name,ID)
    print(f"Rent is : {truck.rent()}") #Step 6

else:
    print("Invalid Vehicle Type !")


