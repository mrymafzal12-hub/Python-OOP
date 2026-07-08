class Coffee:
# Amount in grams
    __beans = 50
    __milk = 100
    __water = 500
    __sugar=20
    __chocolate=30
    def __init__(self,**ingredients):
        self.ingredients=ingredients

        self.beans = ingredients.get("beans",0)
        self.milk = ingredients.get("milk",0)
        self.water =ingredients.get("water",0)
        self.sugar = ingredients.get("sugar",0)
        self.chocolate = ingredients.get("chocolate",0)
    def get_beans(self):
        return self.__beans
    def get_milk(self):
        return self.__milk
    def get_water(self):
        return self.__water
    def get_sugar(self):
        return self.__sugar
    def get_chocolate(self):
        return self.__chocolate
class Check_post:
    def check(self,name,available,given):
        for ingredient ,value in given.items():
            if available.get(ingredient,0) < value:
                print(f"Sorry, we don't have enough {ingredient}")
                return

        print(f"{name} is ready!")




class Latte(Coffee):
    def check(self):
        given = {
            "beans": self.get_beans(),
            "milk": self.get_milk(),
            "water": self.get_water()
        }
        Check_post().check("Latte", self.ingredients,given)

class Espresso(Coffee):
   def check(self):
      given = {
          "beans": self.get_beans(),
          "water": self.get_water()
      }
      Check_post().check("Espresso", self.ingredients, given)

class Cappuccino(Coffee):
    def check(self):
        given = {
            "beans": self.get_beans(),
            "milk": self.get_milk(),
            "sugar": self.get_sugar(),
            "water": self.get_water()

        }
        Check_post().check("Cappuccino", self.ingredients, given)

class Mocha(Coffee):
    def check(self):
        given = {
            "beans": self.get_beans(),
            "milk": self.get_milk(),
            "sugar": self.get_sugar(),
            "chocolate": self.get_chocolate()
        }
        Check_post().check("Mocha", self.ingredients, given)



print("----WELCOME TO COFFEE HUB----")
print(f"{'1. Latte':<20} 350/Rs")
print(f"{'2. Espresso':<20} 400/Rs")
print(f"{'3. Cappuccino':<20} 370/Rs")
print(f"{'4. Mocha':<20} 500/Rs")
n=input("Place Your Order : ").lower()
if n=="latte":
     Latte(beans=100, milk=100, water=1000).check()
elif n=="espresso":
     Espresso(beans=100, water=200).check()
elif n=="cappuccino":
     Cappuccino(beans=100, water=200, sugar=25).check()
elif n=="mocha":
     Mocha(beans=100, milk=100, water=300, chocolate=400).check()




