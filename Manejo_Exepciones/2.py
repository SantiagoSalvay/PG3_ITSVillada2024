def division_numeros():
   
    while True:
       
        try:
           
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            
            resultado = num1 / num2
            print("El resultado de la división es:", resultado)
    
        except ZeroDivisionError:
            print("Error: No se puede dividir entre 0.")
      
        except ValueError:
            print("Error: Por favor, ingrese solo números.")
        else:
            break  


division_numeros()
 