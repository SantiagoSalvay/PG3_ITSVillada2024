class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def cargar_datos(self):
        self.nombre = input("Ingrese nombre: ")
        self.edad = int(input("Ingrese edad: "))
    
    def imprimir_datos(self):
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)


class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self.sueldo = sueldo
        
    
    def calcular_impuestos(self):
        if self.sueldo > 3000:
            print("Este empleado debe pagar impuestos.")
        else:
            print("Este empleado no debe pagar impuestos.")

    def cargar_datos(self):
        super().cargar_datos()
        self.sueldo = float(input("Ingrese sueldo: "))



if __name__ == "__main__":
 
    persona1 = Persona("Juan", 30)
    print("Datos de la persona:")
    persona1.imprimir_datos()
    print()


    empleado1 = Empleado("Pedro", 25, 3500)
    print("Datos del empleado:")
    empleado1.imprimir_datos()
    empleado1.calcular_impuestos()
    print()

  
    empleado2 = Empleado("", 0, 0)
    empleado2.cargar_datos()
    print("Datos del nuevo empleado:")
    empleado2.imprimir_datos()
    empleado2.calcular_impuestos()
