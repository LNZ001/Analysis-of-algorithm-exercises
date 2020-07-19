
class drinkDecorator:
    def getName(self):
        pass

    def getPrice(self):
        pass

    def __getattr__(self, item):
        print("getattr")
        return lambda : 4

    def __getattribute__(self, item):
        print("getattribute")

        return lambda : 54

class sugarDecorator(drinkDecorator):
    # def __init__(self, beverage):
    #     self.beverage = beverage

    def test(self):
        print("test")
    # def getName(self):
    #     return self.beverage.getName() + " +sugar"
    #
    # def getPrice(self):
    #     return self.beverage.getPrice() + 0.5


if  __name__=="__main__":
    # coke_cola=coke()
    # print "Name:%s"%coke_cola.getName()
    # print "Price:%s"%coke_cola.getPrice()
    # ice_coke=iceDecorator(coke_cola)
    # print "Name:%s" % ice_coke.getName()
    # print "Price:%s" % ice_coke.getPrice()
    a = sugarDecorator()
    print(a.t())