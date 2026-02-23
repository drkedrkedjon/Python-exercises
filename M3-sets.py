# La caracteristica de un SET mas importante es que no permite duplicados.

my_set = {1, 2, 3, 4, 5, 20}
# print(my_set) # resultado {1, 2, 3, 4, 5}

query_one = 2 in my_set
# print(query_one) # True

# --------------- Metodos para unir dos set juntos
tags1 = {"CSS", 'HTML', "JS", "HTML"}
tags2 = {"REACT", 'HTML', "JS", "NEXT"}

# Merge two sets in new one
merged_tags = tags1 | tags2
# print(list(merged_tags))
# print(set(merged_tags))

# Solo tags de la primera que no estan en la segunda
first_not_in_second = tags1 - tags2
# print(first_not_in_second)

# Only los elementos que se encuentran en ambos sets
en_ambos = tags1 & tags2
print(en_ambos)
