'''
定义一个用于创建对象的接口，让子类决定实例化哪个类。工厂方法使一个类的实例化延迟到其子类。
'''

class Snake:
    name = ""
    price = 0.0
    type = "SNACK"

    def getPrice(self):
        return self.price

    def setPrice(self, p):
        self.price = p

    def getName(self):
        return self.name


class chip(Snake):
    def __init__(self):
        self.name = "chips"
        self.price = 6.0


class chickenWings(Snake):
    def __init__(self):
        self.name = "chicken wings"
        self.price = 12.0

class foodFactory:

    type = ""

    def createFood(self, foodClass):
        print(self.type, " factory produce a instance.")
        foodIns = foodClass()
        return foodIns

class burgerFactory(foodFactory):
    def __init__(self):
        self.type = "BURGER"


'''
简单工厂模式
'''
# import abc
class simpleFoodFactory:

    @classmethod
    # @abc.abstractmethod
    def createFood(cls, foodClass):
        print("s")
        foodIns = foodClass()
        return foodIns

if __name__ == '__main__':
    burger_factory = burgerFactory()
    chip_burger = burger_factory.createFood(chip)
    print(chip_burger.getName())
    print(chip_burger.getPrice())


