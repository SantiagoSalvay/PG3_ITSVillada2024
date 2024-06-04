def suma_numeros():
   
    while True:
       
        try:
           
            num1 = int(input("Ingrese el primer número entero: "))
            num2 = int(input("Ingrese el segundo número entero: "))
           
            suma = num1 + num2
            print("La suma de los números es:", suma)
        
        except ValueError:
            print("Error: Por favor, ingrese solo números enteros.")
        
        finally:
            seguir = input("¿Quiere seguir sumando valores? (s/n): ")
            if seguir.lower() != 's':
                break

suma_numeros()
