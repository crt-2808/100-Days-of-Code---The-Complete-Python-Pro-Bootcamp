#Herencia

class Animal:
    def __init__(self):
        self.num_eyes=2

    def breathe(self):
        print("Inhale, exhale.")

class Fish(Animal):
    def __init__(self):
        super().__init__() #Hereda todos los atributos de la super clase
    def swim(self):
        print("gloo gloo")

    def breathe(self):
        super().breathe()
        print("Doing it underwater")

nemo=Fish()
nemo.swim()
nemo.breathe()
print(nemo.num_eyes)