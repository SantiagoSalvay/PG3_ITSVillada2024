def contar_vocales(palabra):
    
    vocales = 'aeiou'
   
    palabra = palabra.lower()
  
    contador_vocales = 0
    
    for caracter in palabra:
   
        if caracter in vocales:
            contador_vocales += 1
    return contador_vocales


if __name__ == "__main__":
    palabra = input("Ingrese una palabra: ")
    cantidad_vocales = contar_vocales(palabra)
    print(f"La frase '{palabra}' tiene {cantidad_vocales} vocales.")
