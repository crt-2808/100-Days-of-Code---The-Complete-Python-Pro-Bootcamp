import simplekml
import math

def crear_poligono_kml(latitud_centro, longitud_centro, altura, radio, num_vertices, nombre_archivo):
    # Crea un objeto KML
    kml = simplekml.Kml()
    
    # Calcula el ángulo de separación entre cada vértice del polígono
    angulo_separacion = 360.0 / num_vertices
    
    # Crea una lista para almacenar las coordenadas del polígono
    coords = []
    
    # Itera sobre el número de vértices para calcular las coordenadas
    for i in range(num_vertices):
        # Calcula el ángulo para este vértice
        angulo = math.radians(i * angulo_separacion)
        
        # Calcula las coordenadas del vértice usando la fórmula del círculo
        latitud_vertice = latitud_centro + (radio * math.cos(angulo))
        longitud_vertice = longitud_centro + (radio * math.sin(angulo))
        
        # Agrega las coordenadas del vértice a la lista
        coords.append((longitud_vertice, latitud_vertice, altura))
    
    # Crea el polígono usando las coordenadas calculadas
    poligono = kml.newpolygon(name="Mi Polígono", outerboundaryis=coords)
    
    # Configura el modo de altitud para dibujar el polígono por encima del suelo
    poligono.altitudemode = 'relativeToGround'
    
    # Guarda el archivo KML
    kml.save(nombre_archivo)
    print(f"Archivo KML '{nombre_archivo}' creado correctamente.")

# Coordenadas del centro del polígono (ejemplo)
latitud_centro = 37.42228990140251
longitud_centro = -122.0822035425683

# Altura del polígono sobre el suelo (ejemplo)
altura = 100  # 100 metros

# Radio del polígono en kilómetros (ejemplo)
radio = 0.05  # 50 metros de radio

# Número de vértices del polígono (ejemplo)
num_vertices = 8

# Nombre del archivo KML
nombre_archivo = "poligono_en_google_earth.kml"

# Crea el polígono KML
crear_poligono_kml(latitud_centro, longitud_centro, altura, radio, num_vertices, nombre_archivo)
