class Operation:
    def __init__(self, num1, num2):
        self.nombre1=num1
        self.nombre2=num2
    def addition (self):
        somme = self.nombre1 + self.nombre2
        print(somme)
calcule = Operation(8, 3)
calcule.addition()

