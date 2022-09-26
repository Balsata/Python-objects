class Vehiculo:
    color = "Blanco"
    ruedas = 4
    puertas = 4

class Coche (Vehiculo):
    velocidad = 230
    cilindrada = 6

c = Coche()
print( "Ruedas = "  ,c.ruedas)
print( "Color = ", c.color)
print( "Velocidad = ", c.velocidad)
print( "Puertas = ", c.puertas)
print( "Cilindrada = ", c.cilindrada)