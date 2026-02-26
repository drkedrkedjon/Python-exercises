# ############## METHODOS Y FUNCTIONES EN PY

# -------- Crear una function
def mi_function(arg_uno, arg_two):
  return f"{arg_uno} {arg_two}"

mi_function("pinga", "coño")

# -------- Nidar functiones
def printer(arg1, arg2):
  def mi_function():
    return f"{arg1} {arg2}"
  print(mi_function())

printer("Hola", "Caracola")

# -------- Default arguments in JS
def feee (arg = "FALTA ARGUMENTO IDIOTA"): # Same as in JS
  print(arg)
feee("sasa")

# Eso es un problema en PY porque usando lista o dictionario como default da error mas alla cuando reutilizamos la function, siempre se refiere al misma lista u no crea una nueva como en JS
def funct(arg = []):
  arg.append(1)
  return arg

print(funct())
print(funct())

# Named arguments no tienen estar en orden de argumentos en la function, escribiendo asi se asignan corectamente.
def fuuuunct(apellido, nombre ):
  print(f"{nombre} {apellido}")

fuuuunct(nombre = "Sasa", apellido = "Gonzales")


# -------- 

# --------

# --------

# --------

# --------

# --------

# --------