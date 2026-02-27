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

# ---------- Install NUMPY using PIP
import numpy as np
num_range = np.arange(16)
reshaped = num_range.reshape(4, 4)
print(reshaped)