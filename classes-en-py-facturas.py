# Classes en python son iguales como las de JS. Generadores de objetos con metodos, functiones y todo eso parecido...

# Ejemplo basico
class Invoice1:
  def greeting(self): # Se debe incluir un argumento por lo menos. Poner "SELF" - equivalente de THIS en JS
    return "Hi there"
  
test = Invoice1()

# Las clases se componen de datos y comportamientos
# Para añadir data usamo constructor
class Invoice2:
  def __init__(self, client, total): # THIS works but is not to be used, use SELF
    self.client = client
    self.total = total
  
  def cambiar_nombre(self, name):
    self.client = name.upper()
  
  def printer(self):
    return f"This is {self.client} factura y debe pagar {self.total}"

cafler = Invoice2("Pepe Rodriguez", "235€")
cafler._client = "sAsa sAvic"
cafler.cambiar_nombre("pEndejo gOnzales")


# GET and SET data in python class
# Se tiene acceso directo a propiedades o variables dentro del objeto creado de una class obj.name y obj.name = name2
# Las functiones SETTER y GETTER (JS) son necesarias solamente en el caso de necesitar una logica mas compleja.

# The property decorator!
class Invoice3:
  def __init__(self, client, total): # THIS works but is not to be used, use SELF
    self._client = client # un _variable significa PROTECTED, Igual como en JS. No lo hace inmutable, solo forma de declarar.
    self._total = total

  # Property decorator sirve para acudir luego a data PROTEGIDA
  @property # ESTO ES GETTER !!!
  def client(self):
    return self._client
  
  @client.setter # ESTO ES SETTER !!!
  def client(self, client):
    self._client = client

  @property # ESTO ES OTRO GETTER !!!
  def total(self):
    return self._total
  
  def printer(self):
    return f"This is {self._client} factura y debe pagar {self._total}"

  
google = Invoice3("Google", "345")

google.client = "Yahoo"

# Repaso de los metodos DUNDER en python: __init__ 

# Dunder methods (short for “double underscore” methods) in Python are special methods with names that start and end with double underscores, like __init__, __str__, __len__, etc.
# They are also called magic methods and allow you to define how your objects behave with built-in Python operations (such as printing, adding, comparing, etc.).
# __init__(self, ...): Constructor, called when you create a new object.
# __str__(self): Defines the string representation (used by print()).
# __repr__(self): Official string representation, used in debugging.
# __len__(self): Defines behavior for len(obj).
# __eq__(self, other): Defines equality (==) comparison.
# __add__(self, other): Defines addition (+) behavior.
class Example:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"Value is {self.value}"
    
    def __len__(self):
        return len(self.value)
    
    def __repr__(self):
        return f"String que dice algo: <value: client: {self.value} >"

obj = Example([1,2,3,4,5])
# print(obj)  # Output: Value is 5
# print(len(obj)) # Output is 5
# print(repr(obj)) 

