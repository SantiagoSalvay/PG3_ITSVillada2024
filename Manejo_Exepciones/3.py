def num_meses():
  
    meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
   
    try:
       
        numero_mes = int(input("Ingresa el número de mes (1-12): "))
       
        if numero_mes < 1 or numero_mes > 12:
            raise ValueError("Número de mes fuera de rango")
      
        nombre_mes = meses[numero_mes - 1]
        print(f"El mes correspondiente al número {numero_mes} es: {nombre_mes}")
    
    except ValueError:
        print("Error: Ingresa un número válido.")
    
    except IndexError:
        print("Error: Número de mes fuera de rango.")
    

num_meses()
