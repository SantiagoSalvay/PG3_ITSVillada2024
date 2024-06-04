class Operaciones:
    def __init__(self):
        self.numero1 = int(input("Ingrese el primer numero entero"))
        self.numero2=int(input("Ingrese el segundo numero entero"))
        self.suma()
        self.resta()
        self.division()
        self.multiplicacion()
    
    def suma (self):
        suma= self.numero1 + self.numero2
        print(f'El resultado de la suma:', suma)
    
    def resta(self):
        resta = self.numero1 - self.numero2
        print(f'El resultado de la resta:', resta)

    def division(self):
        division = self.numero1/self.numero2
        print(f'El resultado de la division:' , division)

    def multiplicacion (self):
        multi= self.numero1*self.numero2    
        print(F'El resultado de la multi:', multi)
    
operacion = Operaciones()