############### LOOPS EN PYTHON

# -------------- FOR .. IN loop. Sirve para tuples, lists, dictionarios...
personas = ("sasa", "clau", "caty", "simba", "kobu")
personas = ["sasa", "clau", "caty", "simba", "kobu"]
for persona in personas:
  print(persona)

# -------------- FOR ... IN / for dictionarios
personas = {
  "nombre": "sasa",
  "edad": 34,
  "iq": 89
}
for key, value in personas.items():
  print(f"Mi {key} es: {value}")

# -------------- FOR ... IN / for strings
string = "Sasa"
for letra in string:
  print(letra)

# -------------- FOR ... IN / ranges => function range() identico a FOR LOOP en JS
for num in range(1, 10, 2): # Incluye primero pero no el segundo
  print(num)

# -------------- Uso de CONTINUE and BREAK in PY LOOPS
personas = ["sasa", "clau", "caty", "simba", "kobu"]
for persona in personas:
  if persona == "sasa":
    print("vete pa movistar")
    continue # Continue salta el resto de codigo y SIGUE iterando por el loop con el siguiente elemento
  if persona == "simba":
    print(f"{persona}, ladra cabron desde el index: {personas.index(persona)}")
    break # Break, salta y el resto del codigo y tambien PARA el loop y ya.
  else:
    print(f"Paso de ti {persona}")

# -------------- WHILE loop in PY
num = list(range(1, 20)) 
while len(num) > 0:
  print(num.pop()) 

# Guess number game using while loop
def game():
  while True: # Check where FALSE is...
    print("What is your guess?")
    guess = input()

    if guess == "48":
      print("BINGO")
      return False # returning False stops "WHILE TRUE" complitely.
    else:
      print("NOPE")
# game()

# -------------- Combine & flatten LISTS con FOR/IN loop.
old = ["Caty", "Sasa"]
new = ["Simba", "Kobu"]

for cust in old:
  new.append(cust)
print(new)
# Same can be acomplished using new.extend(old)
old.extend(new)
print(old)
