import simplekml

def crear_punto_kml(latitud, longitud, altitud, nombre_archivo):
    # Crea un objeto KML
    kml = simplekml.Kml()
    
    # Crea un punto en las coordenadas especificadas
    punto = kml.newpoint(name="Mi Punto",
                         coords=[(longitud, latitud, altitud)])  # longitud, latitud, altitud
    
    # Guarda el archivo KML
    kml.save(nombre_archivo)
    print(f"Archivo KML '{nombre_archivo}' creado correctamente.")

# Coordenadas del punto (ejemplo)
latitud = 37.42228990140251
longitud = -122.0822035425683
altitud = 0.0

# Nombre del archivo KML
nombre_archivo = "punto_en_google_earth.kml"

# Crea el punto KML
crear_punto_kml(latitud, longitud, altitud, nombre_archivo)
