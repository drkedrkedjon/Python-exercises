# •    Cree un bucle For de Python.

for num in range(10):
  print(num)


#     •    Cree una función de Python llamada suma que tome 3 argumentos y devuelva la suma de los 3.

def suma(uno, dos, tres):
  return uno + dos + tres

print(suma(2,4,6))


#     •    Cree una función lambda con la misma funcionalidad que la función de suma que acaba de crear.

lambda_suma = lambda uno, dos, tres: uno + dos + tres
print(lambda_suma(2,4,8))


# -Utilizando la siguiente lista y variable, determine si el valor de la variable coincide o no con un valor de la lista. *Sugerencia, si es necesario, utilice un bucle for in y el operador in.
# nombre = 'Enrique'
# lista_nombre = 'Jessica', 'Paul', 'George', 'Henry', 'Adán'

nombre = 'Paul'
lista_nombre = 'Jessica', 'Paul', 'George', 'Henry', 'Adán'

coincide = False

for huesped in lista_nombre:
    if huesped == nombre:
       coincide = True

if coincide:
    print(f"El {nombre} SI esta en la lista de huespedes.")
else:
    print(f"El {nombre} NO esta en la lista de huespedes.")

# Opcion mas concisa pero sin for in loop
if nombre in lista_nombre:
    print(f"El {nombre} SI esta en la lista de huespedes.")
else:
    print(f"El {nombre} NO esta en la lista de huespedes.")