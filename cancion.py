class cancion:
    def __init__(self, nombre, duracion, genero):
        self.nombre = nombre
        self.duracion = duracion
        self.genero = genero 
    
    def establecerNombre(self, nombre):
        self.nombre = nombre

    def establecerDuracion(self, duracion):
        self.duracion = duracion

    def establecerGenero(self, genero):
        self.genero = genero

    def obtenerNombre(self):
        return self.nombre
    
    def obtenerDuracion(self):
        return self.duracion
    
    def obtenerGenero(self):
        return self.genero