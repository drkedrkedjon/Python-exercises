from decimal import Decimal
import math
from functools import reduce

########## Working with Decimal library

precio = 88.40
comision = 0.08
unidades = 44

precio += (precio * comision)
precio *= unidades

# print(precio) #4200.768

precio = Decimal(88.40)
comision = Decimal(0.08)
unidades = 44

precio += (precio * comision)
precio *= unidades

# print(precio) #4200.768000000000276597411641

########## Conversion entre integrers, floats, decimals y numeros complejos

precio = 88.40
comision = 0.08
unidades = 44
# print(int(precio)) # 88
# print(float(unidades)) # 44.0
# print(Decimal(precio)) # 88.400000000000005684341886080801486968994140625
# print(complex(comision)) # (0.08+0j)

########## Funciones populares de Math

perdida = -20.25
precio_producto = 89.99
# print(abs(perdida)) # 20.25 - quita negativo
# print(math.floor(precio_producto)) # 89
# print(math.ceil(precio_producto)) # 90
# print(math.floor(abs(perdida))) # 20
# print(round(precio_producto)) # Round arriba o abajo en .50
# print(math.sqrt(precio_producto)) # 9.486305919587455
# print(math.pow(5, 5)) # 3125.0

def power_function(num, pow):
  return math.pow(num, pow)

# print(power_function(5, 6))
# print(power_function(3, 5))

########## Function de retornar exponencial de un numero (ejercicio)

def exponent_manual(num, exp):
  # # MANUAL VERSION
  # counter = exp - 1
  # total = num
  # while counter > 0:
  #   total *= num
  #   counter -= 1

  # return total

  # REDUCER VERSION - Primer elemento de array es TOTAL por defecto, si no queremos eso - podemos declarar como tercer argumento de reducer.
  array = [num] * exp
  return reduce(lambda total, element: total * element ,array) 

print(exponent_manual(2, 10))

########## 