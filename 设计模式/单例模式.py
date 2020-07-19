class Singleton:

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "instance"):
            cls.instance = super().__new__(cls, *args, **kwargs)
        return cls.instance

    def test(self):
        print("test.")

if __name__ == '__main__':
    a= Singleton()
    b= Singleton()
    c= Singleton()
    print(id(a))
    print(id(b))
    print(id(c))
