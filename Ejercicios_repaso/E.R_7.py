def es_numero_step(numero):
   
    numero_str = str(numero)
    
  
    for i in range(len(numero_str) - 1):
       
        diferencia = abs(int(numero_str[i]) - int(numero_str[i + 1]))
       
        if diferencia != 1:
            return False
   
    return True


if __name__ == "__main__":
    numero = int(input("Ingrese un número: "))
    if es_numero_step(numero):
        print(f"{numero} es un número step.")
    else:
        print(f"{numero} no es un número step.")
