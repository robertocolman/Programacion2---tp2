from cancion import *
from circulo import Circulo

cancion1 = cancion("One", "1988", "Trash Metal")
cancion2 = cancion("symphony of destruction", "1992", "Pop")
cancion3 = cancion("Crazy Train", "1880", "Heavy Metal")

print("Género de cancion1:", cancion1.obtenerGenero())
print("Género de cancion2:", cancion2.obtenerGenero())
print("Género de cancion3:", cancion3.obtenerGenero())

cancion2.establecerGenero("Heavy Metal")
print("El nuevo genero de la cancion 2 es: ", cancion2.obtenerGenero)

circulo1 = Circulo(5.0)
circulo2 = Circulo(10.0)
circulo3 = Circulo(2.5)

print(f"Diámetro del círculo 1: {circulo1.obtenerDiametro()}")
print(f"Diámetro del círculo 2: {circulo2.obtenerDiametro()}")
print(f"Diámetro del círculo 3: {circulo3.obtenerDiametro()}")
print("-" * 20)

print(f"Valor de PI para el círculo 1: {circulo1.PI}")
print(f"Valor de PI para el círculo 2: {circulo2.PI}")
print(f"Valor de PI para el círculo 3: {circulo3.PI}")

print("-" * 20)

circulo4 = Circulo(8.0)
circulo5 = Circulo(8.0)

print(f"¿Los objetos circulo4 y circulo5 son idénticos? {circulo4 == circulo5}")
print("-" * 20)

print(f"Perímetro de circulo4: {circulo4.obtenerPerimetro()}")
print(f"Perímetro de circulo5: {circulo5.obtenerPerimetro()}")
print(f"¿Los perímetros de circulo4 y circulo5 son idénticos? {circulo4.obtenerPerimetro() == circulo5.obtenerPerimetro()}")
print("-" * 20)