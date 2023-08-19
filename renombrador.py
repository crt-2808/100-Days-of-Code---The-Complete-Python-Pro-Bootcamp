import os

carpeta = input("Ingresa la ruta de la carpeta: ")
numero_base = int(input("Ingresa el número base: "))

if not os.path.exists(carpeta):
    print("La carpeta no existe.")
else:
    archivos = os.listdir(carpeta)
    for indice, archivo in enumerate(archivos):
        if archivo.endswith(".jpg"):
            nuevo_numero = numero_base + indice
            nombre_sin_extension = os.path.splitext(archivo)[0]
            nuevo_nombre = str(nuevo_numero) + ".jpg"
            ruta_antigua = os.path.join(carpeta, archivo)
            ruta_nueva = os.path.join(carpeta, nuevo_nombre)
            os.rename(ruta_antigua, ruta_nueva)
            print(f"Renombrando {archivo} a {nuevo_nombre}")
    
    print("Renombrado completado.")
