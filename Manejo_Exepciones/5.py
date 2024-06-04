def escribir_en_archivo():
    try:
      
        with open("texto.txt", "w") as archivo:
            archivo.write("Hola, este es un ejemplo.\n")
            texto = ""
            archivo.write(texto)
        print("Operación de escritura completada.")
  
    except TypeError as e:
        print("Error:", e)
        print("Se esperaba una cadena de texto. No se pudo escribir el entero.")
   
    except Exception as e:
        print("Ocurrió un error:", e)


escribir_en_archivo()
