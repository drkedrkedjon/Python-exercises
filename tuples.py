################ TUPLES - what a fuck is tuple?

#--------- Tuple es una colection de elementos ordenada y inmutable. No se puede añadir, modificar o borrar un elemento dentro de tuple.

mi_tuple = ("sasa", [1,2,3], {"name": "Caty"})
# print(mi_tuple[1][1])

nombre, arr, obj = mi_tuple
# print(nombre,"/", arr,"/", obj)

#--------- Como añadir un elemento a una tuple reasignando elementos.
mi_tuple = mi_tuple + ("Ventilador",)
mi_tuple += ("Horno para pita",)
# print(mi_tuple)
# print(id(mi_tuple))

#--------- Listas nidadas en Tuple
mi_tuple += ([1,2,3,4,5],)
# print(mi_tuple[2].get("name")) # Slice funciona

#--------- Slices in Tuples
super_tuple = mi_tuple[1::2]

#--------- Tres manera de eliminar un elemento de un tuple
mi_tuple = mi_tuple[:-1] # ultimo
mi_tuple = mi_tuple[1:] # primero
# en medio - messy - no recomendable
arr_tuple = list(mi_tuple)
arr_tuple.pop(2)
mi_tuple = tuple(arr_tuple)
print(mi_tuple)

#--------- Usar un tuple como una KEY en un dictionario


#--------- 

#--------- 

#--------- 