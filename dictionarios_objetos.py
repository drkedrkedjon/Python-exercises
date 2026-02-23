################## Dictionarios / Objetos en JS

#--------- Basic about dictionarys
deportistas = {
  "ski": "Sasha",
  "bici electrica": "Caty",
  "sofa": "Clau",
}
# print(deportistas["bici electrica"])

#--------- Nested dictionaries & lists
personas = {
  "ski": ["Sasha"],
  "bici electrica": "Caty",
  "sofa": {
    "boss": "Sasa"
  }
}
# print(personas["sofa"]["boss"])
# print(personas["ski"][0])

#--------- Añadir un key/value par a un dictionario
personas = {
  "panadero": "Sasa"
}
personas["pingas"] = ["Serbios", "Croatas"]
personas["panadero"] = "Caty"
# print(personas)

#--------- Use of get() metodo to get keys values si existen i si no return something...
new_personas = personas.get("ventiladores", [1,2,3,4])
# print(new_personas)

#--------- Uso de .keys(), .values() & .items() => lo mismo como Object.keys(), Object.values &  Object.entrees() en JS.
# Nuevo es que el dictionary view es dinamico, osea si los dos usuarios ejecutan lo mismo y uno cambia el valor se va dinamicamente actualizar en el otro usuario.

# print(personas.keys())
# print(personas.values())
items_personas = personas.items()
# print(items_personas) # items() retorna tuple...

# # La manera de convertir un dictionary view a un array es asi. [1] es array.slice()
lala_personas = list(personas.keys())[1]
# print(lala_personas)

# Para evitar lo de actualisacion dinamica de una dictionary view debemos hacer la copia local y asi desconectar del dictionario original. Usamos .copy() para este fin
personas_copy = list(personas.copy().keys()) # Lo de list() es opcional.
# print(personas_copy)

# Tuple se trata casi como una lista/array
items_personas = list(personas.items())
# print(items_personas[1][1][1])

#--------- Diferentes metodos para borrar elementos de un dictionario
user = {
  "name": "Sasa",
  "age": 120,
  "iq": "low",
  "coches": ["ficho", "peugi"],
}
del user["iq"] # Problema igual como user["noesta"], si no existe "iq" da error
pop_user = user.pop("ages", "Fallo de cojones") # La solucion, retorna el segundo argumento si no exicte lo que buscamo
# print(pop_user)

#--------- Como trabajar con listas/arrays con varios dictinarios/objects dentro
teams = [
  {"LPA": {
    "primero": "Pepe",
    "segundo": "Juan",
    "tercero": "Jose"
    }
  },
  {"BIO": {
    "primero": "mitxutxi",
    "segundo": "savitx",
    "tercero": "sirimiri"
    }
  }
]
# print(teams[0])
bilbao = teams[1].get("BIO", "No existe")
# print(list(bilbao.values())[1])

#--------- Ejercicio: crear un histograma con PY
ventas = {
  "mashala": 12,
  "apple": 4,
  "tandaramandara": 16,
}
print("M: ", ventas.get("mashala", "no esta") * "*")
print("A: ", ventas.get("apple", "no esta") * "*")
print("T: ", ventas.get("tandaramandara", "no esta") * "*")