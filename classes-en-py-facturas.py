# Classes en python son iguales como las de JS. Generadores de objetos con metodos, functiones y todo eso parecido...

# Ejemplo basico
class Invoice:
  def greeting(self): # Se debe incluir un argumento por lo menos. Si no los tienes poner "self"
    return "Hi there"
  
test = Invoice()
print(test.greeting())

# Las clases se componen de datos y comportamientos
