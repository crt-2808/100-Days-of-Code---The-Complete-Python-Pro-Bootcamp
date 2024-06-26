import os
import shutil
import re

ULTIMO_NOMBRE = 100
CONTINUAR = True
CICLO_CAPITULOS= True
CARPETA_DESTINO ="C:/Users/ramos/OneDrive/Documentos/kindle/tomo 11"  # Cambia por la ruta que desees

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

def aumentar_carpeta(ruta):
    # Convertir la ruta a un formato de Windows válido
    partes_ruta = ruta.split("\\")
    ultima_parte = partes_ruta[-1]
    match = re.match(r"(\D*)(\d+)$", ultima_parte)  # Adaptar regex para que coincida con cualquier nombre seguido de números
    if match:
        texto = match.group(1)
        numero = int(match.group(2))
        numero += 1
        nueva_ultima_parte = f"{texto}{numero}"
        partes_ruta[-1] = nueva_ultima_parte
    else:
        # Si la última parte no termina en números, simplemente agregar 1 al final
        partes_ruta[-1] = f"{ultima_parte}1"
    nueva_ruta = "\\".join(partes_ruta)
    return nueva_ruta

def ciclo_principal(carpeta):
    global ULTIMO_NOMBRE
    print(f"Este es el nuevo número que va a utilizar el programa {ULTIMO_NOMBRE}\n") 
    numero_base = ULTIMO_NOMBRE
    if not os.path.exists(carpeta):
        print("La carpeta no existe.")
    else:
        print(f"Esta es la carpeta con la que se va a trabajar: {carpeta}")
        archivos = os.listdir(carpeta)
        for indice, archivo in enumerate(archivos):
            if archivo.endswith(".jpg"):
                nuevo_numero = numero_base + indice
                nuevo_nombre = f"{nuevo_numero}.jpg"
                ruta_antigua = os.path.join(carpeta, archivo)
                ruta_nueva = os.path.join(carpeta, nuevo_nombre)
                os.rename(ruta_antigua, ruta_nueva)
                print(f"Renombrando {archivo} a {nuevo_nombre}")
                ULTIMO_NOMBRE = nuevo_numero
        print("Renombrado completado.")
        mover_archivos(carpeta_origen=carpeta, carpeta_destino=CARPETA_DESTINO)
        print(f"Archivos movidos a {CARPETA_DESTINO}.")
    print(f"El número final fue {ULTIMO_NOMBRE}\ny la carpeta que usaste fue {carpeta}\n")
    ULTIMO_NOMBRE += 1

def main():
    global CONTINUAR
    global CICLO_CAPITULOS
    global CARPETA_DESTINO  # Declaración de la variable global
    while CICLO_CAPITULOS:
        carpeta_usuario = input("Por favor, ingresa la ruta de la carpeta: ")
        ciclo_principal(carpeta_usuario)
        while CONTINUAR:
            respuesta = input("¿Deseas aumentar otro capitulo (si/no)? ").lower()
            if respuesta == "si":
                carpeta_usuario = aumentar_carpeta(carpeta_usuario)
                ciclo_principal(carpeta_usuario)
            elif respuesta == "no":
                otro_tomo = input("¿Deseas procesar otro tomo (si/no)? ").lower()
                if otro_tomo == "si":
                    CARPETA_DESTINO = aumentar_carpeta(CARPETA_DESTINO)
                    print(f"Aumentando la carpeta destino a: {CARPETA_DESTINO}")
                else:
                    CICLO_CAPITULOS=False
                    CONTINUAR = False
            else:
                print("Respuesta inválida. Por favor, ingresa 'si' o 'no'.")

if __name__ == "__main__":
    print(f"Esta es la carpeta a la que lo vas a enviar {CARPETA_DESTINO}")
    main()
