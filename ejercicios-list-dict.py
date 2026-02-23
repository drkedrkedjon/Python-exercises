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
my_sqr = my_ceil ** 2
math.pow(my_ceil, 2)

# Exercise 4: Select the first element from your dictionary.
primer_elemento = my_dictionary["españa"]
print(primer_elemento)
# Exercise 5: Select the second element from your tuple.
# Exercise 6: Add an element to the end of your list.
# Exercise 7: Replace the first element in your list.
# Exercise 8: Sort your list alphabetically.
# Exercise 9: Use reassignment to add an element to your tuple.