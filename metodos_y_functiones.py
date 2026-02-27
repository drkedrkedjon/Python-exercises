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

# -------- Combinar todos los tipos de argumentos en una function. El orden de args importa.
def hello(time_of_day, *args, **kwargs):
  print(f"Hi {" ".join(args)}, I hope you are well this {time_of_day}.")

  if kwargs:
    print("This is your task for today:")
  for key, value in kwargs.items():
    print(f"{key}: {value}")

hello("morning",
      "Sasa", "Pendejon", "Gonzales",
      first = "Cagar",
      second = "Cocinar",
      third = "Terminar bici")

# -------- LAMBDA FUNCTIONS -> son functiones inline anonimas, parecidas a las arrow de JS
set_name = lambda first, second: f"{first} {second}"
# miArrow = (first, second) => `${first} ${second}` JS arrow version...
print(set_name("Sasa", "Pendejon"))

# -------- PRACTICE => In the code below, create a variable called "greeting" and assign it a lambda function that accepts a name as an argument, and return the string "Hi, name".

def lambda_practice():
  greeting = lambda name: f"Hi, {name}"
  return greeting

print(lambda_practice()("Caty")) # "lambda_practice" retorna "greeting" sin ejecutar la misma. Luego, imediatamente la ejecuta "greeting" con el argumento anidado.

# -------- PRACTICE => FizzBuzz. Print de 1 a 100 y si es divisible por 3 print FIZZ, por 5 BUZZ y por ambos FIZZBUZZ

def fizz_buzz(min_num, max_num):
  for num in range(min_num, max_num + 1):
    fizz = num % 3 == 0
    buzz = num % 5 == 0 
    
    if fizz and buzz:
      print("FizzBuzz")
    elif fizz:
      print("Fizz")
    elif buzz:
      print("Buzz")
    else:
      print(num)

fizz_buzz(1, 100)

# --------


# --------