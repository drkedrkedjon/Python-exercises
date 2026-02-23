import math
import random
############ LISTAS o arrays

#--------- Crear, add, change
users = ["Sasa", "Caty", "Clau"]
users.insert(0, "Edu")
users.insert(len(users), "Zorka") # Al final .push()
users.append("Miki") # .push()
users[3] = "Pepe"
# print(users)

#--------- Remove items in array/list
users.remove("Sasa")
poped_user = users.pop() # quita el ultimo o si pones .pop(0) quita el primero o cualquier index (index)
del users[1]
# print(users)

#--------- Query List/array
# print(len(users)) # Longitud
# print(users[-1]) # Print last item
# print(users.index("Pepe")) # Print index of "Pepe"

#--------- Sort lists / ordenar las listas/arrays
tags = ["musica", "bicicletas", "esqui", "aviones"]
numbers = [1,2,3,6,5,4,7,-8,8,9,10,0]
numbers.sort() # Ordenar por alfabeto, los numeros tambien. Modifica la lista original y retorna "None"
sorted(numbers) # Ordenar por alfabeto, no modifica la lista original y retorna una nueva lista.
numbers.sort(reverse=True) # Ordenar por alfabeto a revers, tambien los numeros
# print(tags)

#--------- join() function para construir una URL o otra cosa
# https://www.startpage.com/do/search?q=paython+development+tutorial
uri = "www.startpage.com/do/search"
tags = ["paython", "development", "tutorial"]
formated_tags = "+".join(tags) # Unir elementos tipo string de un array/lista con el "+" en el medio
query_url = f"https://{uri}?q={formated_tags}" # Se pueden usar single quotes if only on one line
# print(query_url)

#--------- Ranges - rangos en listas
tags = ["paython", "development", "tutorial", "code"]
tag_range = tags[1:2] # Retorna un array con elemento/s [:2], [1:], [1:3], [2:-1]
# print(tag_range)

#--------- Tehnicas mas avanzadas de range & slice sobre una lista/array
tags = ["paython", "development", "tutorial", "code", "programing", "computer science", "pingazo", "bolazo"]
range_tags = tags[:-1:3] # Empieza en zero, hasta el perultimo y tercer arg. es para sacar cada segundo o tercero...
range_tags = tags[::-1] # Revertira indices de los elemento creando una nueva lista, el primero sera el ultimo y asi...
# print(range_tags)

#--------- Encontrar mediana estadistica de una lista
arr = [100, 83, 220, 40, 100, 400, 10, 1 ,3, 5]
def find_median(sale_prices):
  sorted_sale_prices = sorted(sale_prices)
  print(sorted_sale_prices)
  index_of_median = math.floor(len(sorted_sale_prices) / 2)
  return sorted_sale_prices[index_of_median:index_of_median + 1][0]

# print(find_median(arr))

#--------- Usar slice class para guerdar varios slice values
tags = ["paython", "development", "tutorial", "code", "programing", "computer science", "pingazo", "bolazo"]
slice_para_maria = slice(1, 4, 2) # slice_obj can be reused in app, argumentos son (start, stop, step)
slice_para_pepe = slice(1, 6, 3)
# print(tags[slice_para_maria]) # print(tags[1:4:2]) # Same shit
# print(tags[slice_para_pepe])

#--------- Añadir a una lista con dos processos: Place & Copy
tags = ["paython", "development", "tutorial", "code"]
tags.extend(["capullez"]) # Extiende la lista - parecido a push() de JS, pero si es otra lista, solo extiende con  valores de la lista con cual extendemos.
tags.extend(arr) # Importante: Si es "string", meter el string en su propio []. Retorna: None
new_tags = tags + ["coñazo"] # Asi se crea una nueva lista sin modificar la original.
# print(new_tags)

#---------
data = {
  "winn": 1,
  "igual": 2,
  "lose": 3
}

def random_winner(setings):
  container = []

  for (key, value) in setings.items():
    for _ in range(value):
      container.append(key)
    
  # randon_num = random.randint(0, len(container) - 1)
  # return container[randon_num]
  return random.choice(container)

# print(random_winner(data))

#--------- 







#---------
#---------
#---------