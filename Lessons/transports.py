class car(transport):
    def __init__(self,fuelType,engineLitres,color,model,year):
        self.fuelType = fuelType
        self.engineLitres = engineLitres
        self.color = color
        self.model = model
        self.year = year
    @override
    def toGo(self):
        print("car is going")
class transport:
    def toGo(self):
        print("transport is going")
class boat(transport):
    @override
    def toGo(self):
        print("boat is going")
randomBlackPrius = car("hybrid", 2.0,"black","prius",2013)
car.toGo()
transport.toGo()
boat.toGo()