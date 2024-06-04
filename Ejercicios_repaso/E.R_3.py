def create_recta(ancho, alto, caracter):
    for i in range(alto):
        print(caracter * ancho)

def create_tri(base, caracter):
    for i in range(1, base + 1):
        print(caracter * i)


while True:
    opcion = input(" R para rectángulo, T para triángulo o salir (salir) \n >>> ")
    
    if opcion.upper() == 'R':
        ancho_rectangulo = int(input(" Ancho del rectángulo \n >>> "))
        alto_rectangulo = int(input(" Alto del rectángulo \n >>> "))
        caracter_rectangulo = input(" Carácter para el rectángulo \n >>> ")
        create_recta(ancho_rectangulo, alto_rectangulo, caracter_rectangulo)
    
    elif opcion.upper() == 'T':
        base_triangulo = int(input(" Base del triángulo \n >>> "))
        caracter_triangulo = input("Carácter para el triángulo \n >>>")
        print("\nTriángulo:")
        create_tri(base_triangulo, caracter_triangulo)
    else:
        print("Opción no válida. Por favor, selecciona R para rectángulo o T para triángulo.")
    
    if opcion.upper() == 'S':
        print("Saliendo...")
        break
    else:
        print("Opción no válida. Por favor, seleccionar la letra R, para rectángulo o T para triángulo. Tambien para salir(Salir)")
