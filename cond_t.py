from threading import Condition
import threading
global count
count =0
def printBar():
    global count
    print("bar", count)
    count += 1
def printFoo():
    global count
    print("foo", count)
    count += 1


import threading
import time


class FooBar:
    def __init__(self, n):
        self.n = n
        self.cond = threading.Condition()
        # self.b = threading.Barrier(3)
        self.t = 0
        print(0,)

    def foo(self, printFoo: 'Callable[[], None]') -> None:

        for i in range(self.n):
            with self.cond:

                # printFoo() outputs "foo". Do not change or remove this line.
                printFoo()
                self.cond.notify()
                if i < self.n-1:
                    self.cond.wait()

    def bar(self, printBar: 'Callable[[], None]') -> None:

        for i in range(self.n):
            with self.cond:
                # printBar() outputs "bar". Do not change or remove this line.
                printBar()
                self.cond.notify()
                if i < self.n - 1:
                    self.cond.wait()


if __name__ == '__main__':
    foobar = FooBar(100)
    t2 = threading.Thread(target=foobar.bar, args=(printBar,))
    t1 = threading.Thread(target=foobar.foo, args=(printFoo,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
