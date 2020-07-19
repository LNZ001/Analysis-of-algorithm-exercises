class Burger:

    name = ""
    price = 0.0

    def getPrice(self):
        return self.price

    def setPrice(self, p):
        self.price = p

    def getName(self):
        return self.name

class cheeseBurger(Burger):

    def __init__(self):
        self.name ="cheese burger"
        self.price = 10.0

class order:

    def __init__(self, orderBuilder):
        self.burger = orderBuilder.bBurger

    def show(self):
        print(f"{self.burger.getName()} | {self.burger.getPrice()} order~")

class orderBuilder:

    bBurger = ""

    def addBurger(self, xBurger):
        self.bBurger = xBurger

    def build(self):
        return order(self)

if __name__ == '__main__':
    ob = orderBuilder()
    ob.addBurger(cheeseBurger())
    ob.build().show()