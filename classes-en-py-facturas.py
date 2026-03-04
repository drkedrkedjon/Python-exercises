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
class Invoice:
  def __init__(self, client, total): # THIS works but is not to be used, use SELF
    self._client = client # un _ significa PROTECTED, Igual como en JS. No cambia nada, solo forma de declarar.
    self._total = total

  # Property decorator sirve para acudir luego a data PROTEGIDA
  @property
  def client(self):
      return self._client
  
  def printer(self):
    return f"This is {self._client} factura y debe pagar {self._total}"

  
google = Invoice("Google", "345")
print(google.client)