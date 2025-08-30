from cancion import *

cancion1 = cancion("One", "1988", "Trash Metal")
cancion2 = cancion("symphony of destruction", "1992", "Pop")
cancion3 = cancion("Crazy Train", "1880", "Heavy Metal")

print("Género de cancion1:", cancion1.obtenerGenero())
print("Género de cancion2:", cancion2.obtenerGenero())
print("Género de cancion3:", cancion3.obtenerGenero())

cancion2.establecerGenero("Heavy Metal")
print("El nuevo genero de la cancion 2 es: ", cancion2.obtenerGenero)