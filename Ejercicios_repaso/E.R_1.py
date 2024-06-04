def buscar_elemento(lista, elemento):
   
    try:
        indice = lista.index(elemento)
        return indice
    except ValueError:
        return -1


if __name__ == "__main__":
    lista = [8, 12, 9, 45]

    
    elemento_buscado = int(input("Ingrese el elemento que desea buscar: "))

   
    indice = buscar_elemento(lista, elemento_buscado)

    
    if indice != -1:
        print(f"El elemento {elemento_buscado} se encuentra en la posicion {indice} de la lista.")
    else:
        print(f"El elemento {elemento_buscado} no esta en la lista.")
