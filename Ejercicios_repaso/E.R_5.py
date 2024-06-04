def es_palindromo(palabra):
   
    palabra = palabra.lower()
    
   
    if palabra == palabra[::-1]:
        return True
    else:
        return False


if __name__ == "__main__":
    palabra1 = "neuquen"
    palabra2 = "jovenes"

    print(f"¿'{palabra1}' es un palíndromo?: {es_palindromo(palabra1)}")
    print(f"¿'{palabra2}' es un palíndromo?: {es_palindromo(palabra2)}")
