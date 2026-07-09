class Animal:
    def __init__(self):
        return
    def eat(self):
        print("meat")
class lion(Animal):
    def eat(self):
        print("lion")
class tiger(Animal):
    def eat(self):
        print("tiger")
class chicken(Animal):
    def eat(self):
        print("chicken")


class Zoo:
    def __init__(self):
        self.gh=[]
    def add(self,animal):
        self.gh.append(animal)
    def feed(self):
        for f in self.gh:
            print(f.eat())
c=Zoo()
c.add(lion())
c.add(tiger())
c.add(chicken())

c.feed()
