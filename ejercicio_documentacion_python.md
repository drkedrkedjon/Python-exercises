# Documentacion Python

## ¿Qué es un condicional?

Un condicional en Python permite ejecutar diferentes acciones según si se cumple o no una condición. Se usan las sentencias `if`, `elif` y `else`.

Ejemplo:

```python
edad = 18
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
```

## ¿Cuáles son los diferentes tipos de bucles en Python? ¿Por qué son útiles?

En Python hay dos tipos principales de bucles: `for` y `while`. Los bucles permiten repetir acciones varias veces, lo que es útil para procesar listas, realizar cálculos repetitivos o automatizar tareas.

- **Bucle for:** Se usa para recorrer elementos de una secuencia (como una lista o un rango).
- **Bucle while:** Se repite mientras una condición sea verdadera.

Ejemplo de bucle for:

```python
for letra in "Python":
    print(letra)
```

## ¿Qué es una lista por comprensión en Python?

Una lista por comprensión es una forma sencilla y compacta de crear listas en Python usando una sola línea de código. Permite generar listas aplicando una expresión a cada elemento de una secuencia y, opcionalmente, filtrando elementos con una condición.

Ejemplo:

```python
numeros = [x for x in range(5)]
print(numeros)  # [0, 1, 2, 3, 4]

pares = [x for x in range(10) if x % 2 == 0]
print(pares)  # [0, 2, 4, 6, 8]
```

## ¿Qué es un argumento en Python?

Un argumento es un valor que se pasa a una función para que la función lo utilice en su ejecución. Los argumentos permiten que las funciones sean más flexibles y reutilizables.

Ejemplo:

```python
def saludar(nombre):
    print(f"Hola, {nombre}!")

saludar("Ana")  # Hola, Ana!
saludar("Luis") # Hola, Luis!
```

## ¿Qué es una función Lambda en Python?

Una función lambda en Python es una función pequeña y anónima que se define en una sola línea. Se usa para operaciones simples y rápidas, normalmente cuando necesitas una función corta y no quieres definirla con `def`.

Ejemplo:

```python
sumar = lambda x, y: x + y
print(sumar(3, 5))  # 8
```

## ¿Qué es un paquete pip?

`pip` es el gestor de paquetes de Python. Sirve para instalar, actualizar y eliminar librerías externas que puedes usar en tus proyectos.

Ejemplo de uso en la terminal:

```bash
pip install requests
```
