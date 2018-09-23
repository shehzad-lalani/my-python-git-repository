#Constructors In Python

class Vehicle:
    speed = 20

    def __init__(self,speed = 0):
      self.speed = speed

    def __add__(self, OtherVehicle):
        return Vehicle(self.speed + OtherVehicle.speed)

    def IncreaseSpeed(self, increaseAmount):
      self.speed += increaseAmount

class Car(Vehicle):
  weight = 10

  def IncreaseWeight(self, weight):
    self.weight += weight

  def IncreaseSpeed(self, increaseAmount):
      self.speed *= increaseAmount

bmw = Vehicle()
audi = Vehicle(55)
mehran = Car(7)

print(mehran.weight)
mehran.IncreaseWeight(9)
print(mehran.weight)
mehran.IncreaseSpeed(6)
print(mehran.speed)

print("Speed of bmw is: %i" % bmw.speed)
print("Speed of audi is: %i" % audi.speed)

audi.IncreaseSpeed(6)
bmw.IncreaseSpeed(7)
print("Speed of bmw is: %i" % bmw.speed)
print("Speed of audi is: %i" % audi.speed)

mehran = bmw + audi
print(mehran.speed)
