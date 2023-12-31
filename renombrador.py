import os
import shutil

ULTIMO_NOMBRE=0

def mover_archivos(carpeta_origen, carpeta_destino):
    if not os.path.exists(carpeta_destino):
        os.makedirs(carpeta_destino)
    
    archivos = os.listdir(carpeta_origen)
    for archivo in archivos:
        if archivo.endswith(".jpg"):
            ruta_origen = os.path.join(carpeta_origen, archivo)
            ruta_destino = os.path.join(carpeta_destino, archivo)
            shutil.move(ruta_origen, ruta_destino)
            print(f"Moviendo {archivo} a {carpeta_destino}")

carpeta = input("Ingresa la ruta de la carpeta: ")
numero_base = int(input("Ingresa el número base: "))
carpeta_destino = "C:/Users/ramos/OneDrive/Documentos/Mangas/vol30"  # Establece la ruta de la carpeta destino aquí

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
            
            ULTIMO_NOMBRE=nuevo_numero
    
    print("Renombrado completado.")
    
    # Llamada a la función para mover archivos a la carpeta destino
    mover_archivos(carpeta, carpeta_destino)
    print(f"Archivos movidos a {carpeta_destino}.")

print (f"El numero final fue {ULTIMO_NOMBRE} y la carpeta que usaste fue {carpeta}")