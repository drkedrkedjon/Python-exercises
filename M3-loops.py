############### LOOPS EN PYTHON

# -------------- FOR .. IN loop. Sirve para tuples, lists, dictionarios, sets... todo 
personas = ("sasa", "clau", "caty", "simba", "kobu")
personas = ["sasa", "clau", "caty", "simba", "kobu"]
for persona in personas:
  print(persona)

# -------------- FOR ... IN for Dictionarios
personas = {
  "nombre": "sasa",
  "edad": 34,
  "iq": 89
}
for key, value in personas.items():
  print(f"Mi {key} es: {value}")

 