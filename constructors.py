#Constructors In Python

class Vehicle:
    speed = 20

    def __init__(self,speed = 0):
      self.speed = speed

    def IncreaseSpeed(self, increaseAmount):
      self.speed += increaseAmount

bmw = Vehicle()
audi = Vehicle(55)

print("Speed of bmw is: %i" % bmw.speed)
print("Speed of audi is: %i" % audi.speed)

audi.IncreaseSpeed(6)
print("Speed of bmw is: %i" % bmw.speed)
print("Speed of audi is: %i" % audi.speed)
