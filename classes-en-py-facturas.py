# Classes en python son iguales como las de JS. Generadores de objetos con metodos, functiones y todo eso parecido...

# Ejemplo basico
class Invoice1:
  def greeting(self): # Se debe incluir un argumento por lo menos. Poner "SELF" - equivalente de THIS en JS
    return "Hi there"
  
test = Invoice1()

# Las clases se componen de datos y comportamientos
# Para añadir data usamo constructor
class Invoice:
  def __init__(self, client, total): # THIS works but is not to be used, use SELF
    self.client = client
    self.total = total
  
  def client_seter(self, name):
    self.client = name.upper()
  
  def printer(self):
    return f"This is {self.client} factura y debe pagar {self.total}"

cafler = Invoice("Pepe Rodriguez", "235€")
print(cafler.printer())

cafler.client = "sAsa sAvic"
print(cafler.printer())

cafler.client_seter("pEndejo gOnzales")
print(cafler.printer())

# GET and SET data in python class
