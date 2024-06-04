class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
    
    def imprimir_lado_mayor(self):
        lado_mayor = max(self.lado1, self.lado2, self.lado3)
        print("El lado mayor es:", lado_mayor)
    
    def es_equilatero(self):
        if self.lado1 == self.lado2 == self.lado3:
            print("El triángulo es equilátero.")
        else:
            print("El triángulo no es equilátero.")


lado1 = float(input("Ingrese la longitud del primer lado: "))
lado2 = float(input("Ingrese la longitud del segundo lado: "))
lado3 = float(input("Ingrese la longitud del tercer lado: "))

triangulo = Triangulo(lado1, lado2, lado3)
triangulo.imprimir_lado_mayor()
triangulo.es_equilatero() 
