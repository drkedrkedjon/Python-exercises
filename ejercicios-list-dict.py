from decimal import Decimal
import math

# Exercise 1: Create a list, tuple, float, integer, decimal, and dictionary.
my_list = ["one", "two", "three"]
my_tuple = (1, 2, 3, [True, False])
my_float = 3.14
my_integrer = 365
my_decimal = Decimal(str(my_float)) # manera recomendada para eliminar inprecision de float
my_dictionary = {
  "españa": {
    "oro": 1,
    "plata": 0,
    "bronce": "1" 
  },
  "Bosnia": None
}
# Exercise 2: Round your float up.
my_ceil = math.ceil(my_decimal)

# Exercise 3: Get the square root of your float.
math.sqrt(my_float)

# Exercise 4: Select the first element from your dictionary.
primer_elemento = my_dictionary["españa"]
primer_elemento_get = my_dictionary.get("españa", "No hay tal elemento en este dictionario")

# Exercise 5: Select the second element from your tuple.
segundo_tuple_elem = my_tuple[1]

# Exercise 6: Add an element to the end of your list.
my_list.append("four")
my_list.extend(["fifth"])

# Exercise 7: Replace the first element in your list.
my_list[0] = "hahaha"

# Exercise 8: Sort your list alphabetically.
my_list.sort()

# Exercise 9: Use reassignment to add an element to your tuple.
my_tuple += ("reasignado",)
print(my_tuple)