
# Exercise 1: Create a string, number, list, and boolean, each stored in their own variable.

string = "Sasa es un pendejo gonzales"
numero = 20
lista = ["zero", "uno", "dos", "tres"]
boleano = True

# Exercise 2: Use an index to grab the first 3 letters in your string, store that in a variable.

primeras_tres_letras = string[:3]
print(primeras_tres_letras)

# Exercise 3: Use an index to grab the first element from your list.

primer_elemento = lista[0]
print(primer_elemento)

# Exercise 4: Create a new number variable that adds 10 to your original number.

nuevo_numero = numero + 10
print(nuevo_numero)

# Exercise 5: Use an index to get the last element in your list.

ultimo_elemento = lista[-1]
print(ultimo_elemento)

# Exercise 6: Use split to transform the following string into a list.
names = 'harry,alex,susie,jared,gail,conner'

names_lista = names.split(",")
print(names_lista)

# Exercise 7: Get the first word from your string using indexes. Use the upper function to
# transform the letters into uppercase. Create a new string that takes the uppercase word and the
# rest of the original string.

primera_palabra = string.split(" ")[0]
new_string = primera_palabra.upper() + string.lstrip(primera_palabra)
print(new_string)

# Exercise 8: Use string interpolation to print out a sentence that contains your number variable.

interpolation = f"""Esta frase contiene el numero: {numero}"""
print(interpolation)

# Exercise 9: Print “hello world”
print("hello world")

# Extra ejercicio: Además necesito que me crees una cadena que contenga la palabra "Hola". Usando la palabra clave en el método de búsqueda o el índice, busque y seleccione "Hola" en su cadena. Y usando la función de reemplazo, reemplace "Hola" en su cadena con "adiós".

cadena = "Hola profesor Carlos"
indice_hola = cadena.find("Hola")
seleccionar_hola = cadena[indice_hola: indice_hola + 4]
print(seleccionar_hola)

nueva_cadena = cadena.replace("Hola", "Adios")
print(nueva_cadena)