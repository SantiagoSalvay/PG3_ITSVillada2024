def ordenar_de_mayor_a_menor(lista):
    
    lista_ordenada = sorted(lista, reverse=True)
    return lista_ordenada


if __name__ == "__main__":
   
    numeros = [5, 2, 9, 1, 7, 3, 8]

    
    numeros_ordenados = ordenar_de_mayor_a_menor(numeros)

   
    print("Lista ordenada de mayor a menor:", numeros_ordenados)
