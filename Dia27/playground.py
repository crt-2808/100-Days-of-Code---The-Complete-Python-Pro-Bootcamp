def add(*args):
    result=sum(args)
    return result

print(add(1,2,3,4,5,6,7,8,9))

def calculate(n,**kwargs):
    print(kwargs)
    n+=kwargs["add"]
    n*=kwargs["mult"]
    print(n)


calculate(2, add=3, mult=5)


class Car:
    def __init__(self, **kwargs):
        self.make=kwargs.get("make")
        self.model=kwargs.get("model")

my_car=Car(make="Nissan")
print(my_car.model)

def all_aboard(a, *args, **kw): 
    print(a, args, kw)
 
all_aboard(4, 7, 3, 0, x=10, y=64)
