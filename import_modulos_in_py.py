#    IMPORTACION DE MODULOS EXTERNOS EN PYTHON

# ---------- Importacion de modulos incrustados en el mismo python
import math
print(math.sqrt(3))

# ---------- Importacion de function desde el otro modulo / documento
from modulos.helper import greeting
print(greeting("Sasha"))