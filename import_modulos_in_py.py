#    IMPORTACION DE MODULOS EXTERNOS EN PYTHON

# ---------- Importacion de modulos incrustados en el mismo python
import math
print(math.sqrt(3))

# ---------- Importacion de function desde el otro modulo y TAMBIEN importacion de TODAS las functiones del dicho modulo
from modulos.helper import greeting
import modulos.helper
print(greeting("Sasha"))
print(modulos.helper.greeting("Sasha"))
print(modulos.helper.shitting("Sasha"))

# ---------- 