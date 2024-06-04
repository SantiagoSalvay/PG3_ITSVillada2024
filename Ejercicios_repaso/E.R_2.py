def es_bisiesto(año):
   
    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        return True
    else:
        return False

if __name__ == "__main__":
    try:
        año = int(input("Ingrese un año: "))
        
        if es_bisiesto(año):
            print(f"{año} es bisiesto.")
        else:
            print(f"{año} no es bisiesto.")
    except ValueError:
        print("Por favor, ingrese un año válido.")
