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

# -------- Default arguments in PY
def feee (arg = "FALTA ARGUMENTO IDIOTA"): # Same as in JS
  print(arg)
feee("sasa")

# Eso es un problema en PY porque usando lista o dictionario como default da error mas alla cuando reutilizamos la function, siempre se refiere al misma lista u no crea una nueva como en JS
def funct(arg = []):
  arg.append(1)
  return arg

print(funct())
print(funct())

# -------- Named arguments in PY
# Named arguments no tienen estar en orden de argumentos en la function, escribiendo asi se asignan corectamente.
def fuuuunct(apellido, nombre ):
  print(f"{nombre} {apellido}")

fuuuunct(nombre = "Sasa", apellido = "Gonzales")

# -------- Unpacking function argument (rest operator *) - cuando tienes desconocido el numero de argumentos
def greeting(*args): # Comon costumbre en PY es llamar ARGS. EN JS: "function greeting(...args){}" usando parametro rest ...
  print("Hi " + " ".join(args))

greeting("Sasa", "Savic", "Perusina", "Pendejon")

# -------- Named arguments unidos con el rest "JS" operator (Unpacking arguments)
def greeet(**kwargs):
  if kwargs:
    print(f"Hi {kwargs["first"]} el peo viejo de la familija {kwargs["second"]}")
  else:
    print("Ups, shit happens")
greeet(first = "Sasa", second="Savichi")

# -------- 

# --------

# --------

# --------

# --------