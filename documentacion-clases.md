# Documentación sobre lo conceptos fundamentales de Python, APIs y DB.

# ¿Para qué usamos Clases en Python?

Las clases en Python son una herramienta fundamental de la programación orientada a objetos. Nos permiten crear nuestros propios tipos de datos, agrupando variables (llamadas atributos) y funciones (llamadas métodos) que tienen sentido juntas. Así, podemos modelar cosas del mundo real o conceptos abstractos de forma ordenada y reutilizable. Se puede decir que son como un molde o una plantilla a partir de cual podemos crear los diferentes objetos que comparten funcionalidades heredadas.

**¿Por qué se usan?**

- Para organizar el código y evitar repeticiones.
- Para reutilizar funcionalidades en diferentes partes del programa.
- Para modelar entidades complejas (por ejemplo: un auto, un usuario, una factura).
- Para facilitar el mantenimiento y la ampliación del código.

**Analogía:**

Piensa en una clase como un plano para construir casas. El plano define cómo será la casa (puertas, ventanas, habitaciones), pero cada casa construida a partir de ese plano puede tener detalles propios (color, dueño, dirección). Cada casa es un objeto (instancia) de la clase "Casa".

**Sintaxis básica:**

```python
class NombreDeLaClase:
	def __init__(self, atributo1, atributo2):
		self.atributo1 = atributo1
		self.atributo2 = atributo2

	def metodo(self):
		# Código del método
		pass
```

**Ejemplo paso a paso:**

```python
# Definimos la clase Persona
class Persona:
	def __init__(self, nombre, edad):  # Método especial para crear la persona / constructor
		self.nombre = nombre            # Guardamos el nombre
		self.edad = edad                # Guardamos la edad

	def saludar(self):                 # Método para saludar
		print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")

# Creamos una persona (objeto/instancia) llamando la Classe y passando los atributos
p1 = Persona("Caty", 25)
# Usamos el método saludar
p1.saludar()  # Salida: Hola, mi nombre es Ana y tengo 25 años.
```

**¿Qué es `self`?**

En Python, `self` es una palabra que se usa dentro de las clases para referirse al propio objeto que se está creando o usando. Es como decir "yo mismo" dentro de la clase. Gracias a `self`, cada objeto puede tener sus propios datos y métodos.

Por ejemplo, cuando escribimos `self.nombre`, estamos accediendo al atributo `nombre` del objeto actual. Es obligatorio poner `self` como primer parámetro en los métodos de la clase.

**Ejemplo sencillo:**

```python
class Ejemplo:
	def mostrar(self):
		print("Este objeto es:", self)

e = Ejemplo()
e.mostrar()  # Muestra la dirección en memoria del objeto 'e'
```

**Resumen:**

- `self` permite que cada objeto tenga sus propios datos.
- Es necesario en todos los métodos de instancia.
- No es una palabra reservada, pero es una convención universal en Python.

**Buenas prácticas:**

- El nombre de la clase debe empezar con mayúscula.
- Los métodos y atributos suelen ir en minúscula y con guiones bajos si tienen varias palabras.
- Usa clases cuando necesites agrupar datos y comportamientos relacionados.

**Advertencia común:**

No olvides poner `self` como primer parámetro en los métodos de la clase. `self` representa al propio objeto.

**Enlaces a documentación:**

[Clases en Python](https://docs.python.org/es/3/tutorial/classes.html): Explica cómo crear y usar clases, atributos, métodos, herencia y conceptos fundamentales de la programación orientada a objetos en Python. Incluye ejemplos y buenas prácticas.

# ¿Qué método se ejecuta automáticamente cuando se crea una instancia de una clase?

El método especial `__init__` (llamado constructor) se ejecuta automáticamente cada vez que creamos un nuevo objeto de una clase. Su función es inicializar los atributos del objeto, es decir, darle sus valores iniciales.

**¿Cómo funciona?**

Cuando escribimos `objeto = Clase(valor1, valor2)`, Python llama internamente a `__init__` y le pasa esos valores.

**Ejemplo explicado:**

```python
class Animal:
	def __init__(self, especie):
		self.especie = especie  # Guardamos la especie en el objeto

a = Animal("Perro")  # Aquí se ejecuta __init__ automáticamente
print(a.especie)      # Salida: Perro
```

**¿Qué pasa si no defines `__init__`?**

Python crea uno vacío por defecto, pero no podrás inicializar atributos personalizados al crear el objeto.

**Enlaces a documentación:**

[Método **init**](https://docs.python.org/es/3/reference/datamodel.html#object.__init__): Detalla el método constructor de Python, su sintaxis, cuándo se ejecuta y cómo inicializa los atributos de una instancia. Esencial para entender la creación de objetos.

# ¿Cuáles son los tres verbos de API?

En el contexto de las APIs web (especialmente las APIs REST), los "verbos" son las acciones principales que podemos realizar sobre los datos. Los más usados son:

- **GET**: Solicita datos al servidor. No modifica nada, solo pide información.
- **POST**: Envía datos al servidor para crear un nuevo recurso (por ejemplo, un nuevo usuario).
- **PUT**: Envía datos para modificar o reemplazar un recurso existente.
- (También existe **DELETE** para eliminar recursos.)

**Ejemplo práctico:**
Supongamos que tienes una API de usuarios:

- `GET /usuarios` → Devuelve la lista de usuarios.
- `POST /usuarios` → Crea un nuevo usuario.
- `PUT /usuarios/1` → Modifica el usuario con ID 1.
- `DELETE /usuarios/1` → Elimina el usuario con ID 1.

**Ejemplos simples usando requests en Python:**

```python
import requests

# GET: Obtener la lista de usuarios
respuesta = requests.get('https://api.ejemplo.com/usuarios')
print(respuesta.json())

# POST: Crear un nuevo usuario
nuevo_usuario = {"nombre": "Caty", "edad": 25}
respuesta = requests.post('https://api.ejemplo.com/usuarios', json=nuevo_usuario)
print(respuesta.json())

# PUT: Modificar un usuario existente
actualizacion = {"nombre": "Caty", "edad": 26}
respuesta = requests.put('https://api.ejemplo.com/usuarios/1', json=actualizacion)
print(respuesta.json())

# DELETE: Eliminar un usuario
respuesta = requests.delete('https://api.ejemplo.com/usuarios/1')
if respuesta.status_code == 204:
	print('Usuario eliminado')
else:
	print('No se pudo eliminar')
```

Cada ejemplo muestra cómo usar la librería requests para interactuar con una API usando los verbos principales. Recuerda instalar requests con `pip install requests` si no la tienes.

**¿Por qué es importante?**

Estos verbos permiten que diferentes aplicaciones se comuniquen de forma estándar y predecible.

**Enlaces a documentación:**

[Verbos de API (requests)](https://docs.python-requests.org/en/latest/): Documenta la librería requests, cómo realizar peticiones HTTP (GET, POST, PUT, DELETE), manejo de respuestas, autenticación y envío de datos en APIs.

# ¿Es MongoDB una base de datos SQL o NoSQL?

MongoDB es una base de datos **NoSQL**. Esto significa que no utiliza tablas ni el lenguaje SQL tradicional, sino que almacena la información en documentos con formato similar a JSON (llamado BSON). A diferencia de las bases de datos SQL, MongoDB ofrece una estructura mucho más flexible y está diseñada para manejar grandes volúmenes de datos y cambios rápidos en los esquemas.

**Diferencias principales entre SQL y NoSQL:**

- **SQL** (como MySQL, PostgreSQL):
  - Usa tablas, filas y columnas con una estructura fija (esquema rígido).
  - Requiere definir el esquema antes de insertar datos.
  - Utiliza el lenguaje SQL para consultas y manipulación de datos.
  - Es ideal para aplicaciones donde la integridad y las relaciones entre datos son críticas (por ejemplo, sistemas bancarios).
  - Soporta transacciones complejas y relaciones entre tablas (JOINs).

- **NoSQL** (como MongoDB):
  - Usa documentos (similar a JSON) y colecciones, con estructura flexible (esquema dinámico).
  - Permite guardar diferentes tipos de datos en un mismo lugar, incluso si tienen campos distintos.
  - No requiere definir el esquema previamente; puedes agregar o quitar campos según lo necesites.
  - Utiliza consultas específicas de MongoDB, que son más intuitivas para trabajar con datos anidados.
  - Es ideal para aplicaciones que requieren escalabilidad, flexibilidad y cambios frecuentes en los datos.

**Ventajas de MongoDB:**

- **Flexibilidad:** Puedes guardar documentos con diferentes campos y estructuras en la misma colección.
- **Escalabilidad horizontal:** Es fácil distribuir los datos en varios servidores (sharding) para manejar grandes volúmenes.
- **Alto rendimiento:** Optimizado para operaciones rápidas de lectura y escritura.
- **Facilidad de integración:** Muy usado en aplicaciones modernas (por ejemplo, Node.js, Python, microservicios).
- **Soporte para datos complejos:** Permite almacenar arrays, objetos anidados y datos semiestructurados.

**¿Por qué se usa MongoDB?**

- Es flexible: puedes guardar diferentes tipos de datos sin una estructura fija.
- Escala fácilmente para grandes volúmenes de información.
- Es ideal para aplicaciones modernas que cambian rápido.
- Permite prototipar y desarrollar aplicaciones rápidamente, sin preocuparse por el esquema.
- Es útil para proyectos donde los requisitos de datos pueden cambiar con frecuencia.

**Casos de uso comunes:**

- Aplicaciones web y móviles que requieren alta disponibilidad y escalabilidad.
- Sistemas de gestión de contenido (CMS).
- Plataformas de análisis de datos en tiempo real.
- Almacenamiento de registros, logs y datos de sensores.
- Proyectos de big data y machine learning.

**Ejemplo de documento en MongoDB:**

```json
{
  "nombre": "Ana",
  "edad": 25,
  "hobbies": ["leer", "bailar"],
  "direccion": {
    "ciudad": "Madrid",
    "pais": "España"
  }
}
```

Este documento puede tener campos adicionales o faltar algunos, y MongoDB lo aceptará sin problemas.

**Comparación visual:**

| Característica       | SQL (MySQL, PostgreSQL) | NoSQL (MongoDB)         |
| -------------------- | ----------------------- | ----------------------- |
| Estructura           | Tablas, filas, columnas | Documentos, colecciones |
| Esquema              | Fijo                    | Flexible                |
| Relaciones           | JOINs                   | Referencias/Embebidos   |
| Escalabilidad        | Vertical                | Horizontal              |
| Lenguaje de consulta | SQL                     | Propio de MongoDB       |

**En resumen:**

MongoDB es una base de datos NoSQL que destaca por su flexibilidad, escalabilidad y facilidad de uso en proyectos modernos. Es una excelente opción cuando necesitas manejar datos variados, grandes volúmenes o cambios frecuentes en la estructura de la información.

**Enlaces a documentación:**

[MongoDB (PyMongo)](https://pymongo.readthedocs.io/en/stable/): Guía oficial para conectar, consultar, insertar y manipular datos en MongoDB desde Python usando PyMongo. Explica conceptos NoSQL, colecciones y documentos.

# ¿Qué es una API?

Una API (Interfaz de Programación de Aplicaciones) es un conjunto de reglas y definiciones que permite que dos programas, aplicaciones o sistemas diferentes se comuniquen entre sí. Piensa en una API como un "puente" o un "menú" que te dice qué puedes pedirle a otro programa y cómo hacerlo, sin necesidad de saber cómo funciona internamente ese programa.

**¿Cómo funciona una API?**

Cuando usas una API, tu programa (el cliente) envía una solicitud a otro programa (el servidor), pidiendo información o que realice una acción. El servidor responde con los datos o el resultado solicitado. Todo esto ocurre siguiendo reglas y formatos bien definidos, para que ambos programas se entiendan.

**Tipos de API:**

- **APIs locales:** Permiten que diferentes partes de un mismo programa o sistema operativo se comuniquen (por ejemplo, la API de Windows).
- **APIs web:** Permiten que aplicaciones en internet se comuniquen usando la red, normalmente a través de HTTP. Son las más comunes hoy en día.

**¿Para qué sirve una API?**

- Permite que aplicaciones, páginas web o dispositivos se conecten y compartan datos.
- Facilita la integración entre sistemas diferentes, aunque estén hechos en lenguajes distintos.
- Permite automatizar tareas y conectar servicios (por ejemplo, una app de mensajería que usa la API de Google Maps para mostrar ubicaciones).
- Hace posible que desarrolladores creen nuevas aplicaciones usando servicios ya existentes (por ejemplo, apps que muestran el clima usando la API de un servicio meteorológico).

**Ejemplo cotidiano:**

Cuando usas una app de clima, esta consulta una API para obtener la información del tiempo de un servidor externo. Tú solo ves el resultado, pero por detrás la app está "preguntando" a la API y recibiendo una respuesta.

**Ejemplo visual:**

Imagina que una API es como el menú de un restaurante. Tú (el cliente) eliges del menú (la API) lo que quieres pedir. El camarero (la API) lleva tu pedido a la cocina (el servidor) y luego te trae la comida (la respuesta). No necesitas saber cómo se cocina, solo cómo pedirlo.

**Ejemplo en Python usando la librería requests:**

```python
import requests
# Hacemos una petición GET a una API pública
respuesta = requests.get("https://api.chucknorris.io/jokes/random")
if respuesta.status_code == 200:
	datos = respuesta.json()
	print(datos["value"])
else:
	print("Error al consultar la API")
```

En este ejemplo, tu programa pide un chiste a la API de Chuck Norris. Si la respuesta es exitosa, muestra el chiste.

**¿Qué es una API REST?**

REST es un estilo de arquitectura para diseñar APIs web. Las APIs REST usan los "verbos" HTTP (GET, POST, PUT, DELETE) para interactuar con los datos. Son muy populares porque son simples y funcionan bien con la web.

**¿Cómo se crea una API en Python?**

En Python, una de las formas más sencillas y populares de crear una API web es usando el framework **Flask**. Flask permite definir rutas (endpoints) que responden a solicitudes HTTP y es ideal para aprender y construir proyectos pequeños o medianos.

Sin embargo, en aplicaciones más completas, es común combinar Flask con otras librerías para manejar bases de datos y validar datos:

- **SQLAlchemy:** Es una librería que facilita la conexión y manipulación de bases de datos SQL (como SQLite, MySQL o PostgreSQL) desde Python. Permite definir modelos de datos como clases y realizar consultas de forma sencilla y segura.
- **Marshmallow:** Es una librería que ayuda a validar, serializar (convertir objetos Python a JSON) y deserializar (convertir JSON a objetos Python) los datos que entran y salen de la API. Es muy útil para asegurarse de que los datos cumplen con el formato esperado.

**Ejemplo básico solo con Flask:**

```python
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/saludo')
def saludo():
	return jsonify({'mensaje': '¡Hola desde la API!'})

if __name__ == '__main__':
	app.run(debug=True)
```

En este ejemplo, si visitas `http://localhost:5000/saludo` en tu navegador o con un programa, recibirás una respuesta en formato JSON.

**Ventajas de usar APIs:**

- Permiten reutilizar servicios y datos existentes.
- Facilitan la colaboración entre equipos y aplicaciones.
- Hacen posible la automatización y la integración de sistemas.

**En resumen:**
Una API es una herramienta fundamental para que los programas se comuniquen, compartan datos y funciones, y para construir aplicaciones modernas y conectadas. Aprender a usar y crear APIs es esencial para cualquier programador actual.

**Enlaces a documentación:**

[API definición](https://docs.python.org/es/3/glossary.html#term-api): Define qué es una API, su función como interfaz entre aplicaciones, ejemplos de uso y términos relacionados en el ecosistema Python.

# ¿Qué es Postman?

Postman es una aplicación (gratuita y de pago, la descargamos desde la web de postman y se instala con un doble click) que ayuda a programadores, testers y estudiantes a trabajar con APIs de manera visual, sencilla e interactiva. Es una de las herramientas más populares para aprender, probar y documentar APIs, ya que no requiere conocimientos avanzados de programación para empezar a usarla.

Con Postman puedes:

- Enviar peticiones a APIs (GET, POST, PUT, DELETE, etc.) y ver las respuestas de forma clara y ordenada.
- Probar cómo responde una API ante diferentes datos o errores.
- Guardar y organizar tus pruebas en colecciones para reutilizarlas o compartirlas con otros.
- Automatizar pruebas y validar que una API funciona correctamente a lo largo del tiempo.
- Generar documentación automática de tus pruebas y peticiones.

**Ventajas para principiantes:**

- No necesitas saber programar para empezar a probar APIs y entender cómo funcionan.
- Puedes ver fácilmente los datos que envías y recibes, lo que ayuda a comprender el formato de las respuestas (por ejemplo, JSON).
- Permite experimentar con APIs públicas (como la de clima, chistes, etc.) y aprender cómo se comunican las aplicaciones modernas.

**Ejemplo de uso básico:**

1. Abres Postman y escribes la URL de la API (por ejemplo, https://api.chucknorris.io/jokes/random).
2. Seleccionas el verbo (GET, POST, etc.).
3. Envías la petición y ves la respuesta en pantalla, que puede ser un texto, un JSON o un error.

Esto te permite practicar y entender cómo funcionan las APIs antes de programar tus propias aplicaciones.

**¿Para qué se usa?**

- Probar endpoints de una API sin necesidad de programar.
- Verificar respuestas, errores y tiempos de respuesta.
- Automatizar pruebas de servicios web.
- Documentar y compartir ejemplos de uso de una API.

**Enlaces a documentación:**

[Postman](https://learning.postman.com/docs/getting-started/introduction/): Manual para usar Postman, herramienta para probar, automatizar y documentar APIs. Incluye tutoriales, ejemplos y casos de uso.

# ¿Qué es el polimorfismo?

El polimorfismo es una característica fundamental de la programación orientada a objetos. Permite que diferentes clases tengan métodos con el mismo nombre, pero con comportamientos distintos. Así, podemos usar el mismo nombre de función para objetos diferentes y cada uno responderá a su manera, según su propia implementación.

**¿Qué significa polimorfismo?**
La palabra "polimorfismo" viene del griego y significa "muchas formas". En programación, se refiere a la capacidad de un mismo método o función de comportarse de manera diferente según el objeto que lo invoque.

**Tipos de polimorfismo:**

- **Polimorfismo de sobreescritura (override):** Cuando una subclase redefine un método de su clase padre para darle un comportamiento propio.
- **Polimorfismo por herencia:** Permite tratar objetos de diferentes clases derivadas como si fueran de la clase base, usando el mismo método pero con resultados distintos.
- **Polimorfismo por duck typing (en Python):** En Python, no importa el tipo exacto del objeto, sino que tenga el método esperado. "Si camina como un pato y suena como un pato, es un pato".

**Analogía:**
Piensa en la acción "hablar". Una persona, un perro y un loro pueden "hablar", pero cada uno lo hace de forma diferente. Si le pides a cada uno que hable, la respuesta será distinta según el tipo de objeto.

**Ejemplo explicado:**

```python
class Ave:
	def hablar(self):
		print("Pío")

class Perro:
	def hablar(self):
		print("Guau")

def hacer_hablar(animal):
	animal.hablar()  # No importa si es Ave o Perro, ambos tienen hablar()

hacer_hablar(Ave())    # Salida: Pío
hacer_hablar(Perro())  # Salida: Guau
```

**¿Por qué es útil?**

- Permite escribir código más flexible y reutilizable.
- Facilita trabajar con colecciones de objetos diferentes que comparten métodos.

**Enlaces a documentación:**

[Polimorfismo/herencia](https://docs.python.org/es/3/tutorial/classes.html#inheritance): Explica cómo funciona la herencia y el polimorfismo en Python, permitiendo reutilizar código y crear clases especializadas. Incluye ejemplos prácticos.

# ¿Qué es un método dunder?

Un método dunder (de "double underscore", doble guion bajo) es un método especial de Python que empieza y termina con dos guiones bajos, por ejemplo: `__init__`, `__str__`, `__len__`, `__add__`, etc. Estos métodos permiten personalizar el comportamiento de los objetos en situaciones específicas y son fundamentales para que los objetos se integren bien con el lenguaje Python.

**¿Por qué se llaman dunder?**
La palabra "dunder" viene de "double underscore" (doble guion bajo). En inglés, se pronuncia "dunder" y es una forma rápida de referirse a estos métodos especiales.

**¿Cómo funcionan?**
Cuando usas ciertas operaciones en Python (como sumar, imprimir, comparar, acceder a la longitud, etc.), el intérprete busca si tu objeto tiene un método dunder correspondiente y lo ejecuta. Así puedes definir cómo se comporta tu clase en esas situaciones.

**¿Para qué sirven?**

- Para definir cómo se crea un objeto (`__init__`).
- Para definir cómo se muestra como texto (`__str__`).
- Para definir cómo se comporta con operadores (`__add__`, `__eq__`, etc.).

**Ejemplo explicado:**

```python
class Libro:
	def __init__(self, titulo):
		self.titulo = titulo
	def __str__(self):
		return f"Libro: {self.titulo}"

ejemplo = Libro("1984")
print(l)  # Salida: Libro: 1984
```

**¿Qué pasa en el ejemplo?**
Cuando usamos `print(ejemplo)`, Python llama automáticamente a `ejemplo.__str__()`, que devuelve el texto personalizado. Osea, el `__str__` se ejecuta automaticamente con print() sin que tener que dar el nombre al metodo y llamarlo directamente.

**Lista de métodos dunder comunes:**

- `__init__`: inicialización del objeto.
- `__str__`: representación en texto.
- `__len__`: longitud del objeto.
- `__add__`: suma de objetos.

**Enlaces a documentación:**

[Métodos dunder](https://docs.python.org/es/3/reference/datamodel.html#special-method-names): Lista y describe los métodos especiales de Python (como **init**, **str**, **add**), su propósito y cómo personalizar el comportamiento de los objetos.

# ¿Qué es un decorador de python?

Un decorador en Python es una función especial que "envuelve" a otra función o método para modificar o ampliar su comportamiento, sin cambiar su código original. Los decoradores permiten añadir funcionalidades extra de forma sencilla y reutilizable. Se usan anteponiendo el símbolo `@` al nombre del decorador, justo antes de la función que queremos modificar.

**¿Cómo funcionan los decoradores?**
Cuando aplicas un decorador, Python ejecuta la función decoradora y le pasa la función original como argumento. El decorador puede devolver una nueva función que añade, modifica o controla el comportamiento de la original.

**Ventajas de los decoradores:**

- Permiten añadir funcionalidades a funciones o métodos sin modificar su código.
- Ayudan a evitar repetir código y a mantener el programa organizado.
- Facilitan la separación de responsabilidades (por ejemplo, validación, registro, permisos).

**¿Para qué se usan?**

- Para añadir funcionalidades extra a funciones o métodos (por ejemplo: medir el tiempo de ejecución, verificar permisos, registrar llamadas, etc.).
- Para evitar repetir código.

**Sintaxis básica:**

```python
@nombre_del_decorador
def mi_funcion():
	pass
```

**Ejemplo explicado:**

```python
def mayusculas(func):
	def wrapper():
		resultado = func()
		return resultado.upper()
	return wrapper

@mayusculas
def saludar():
	return "hola mundo"

print(saludar())  # Salida: HOLA MUNDO
```

**¿Qué pasa en el ejemplo?**

- Definimos un decorador `mayusculas` que convierte el resultado de la función a mayúsculas.
- Al decorar `saludar`, cada vez que la llamamos, el texto se transforma automáticamente.

**Decoradores comunes en Python:**

- `@staticmethod` y `@classmethod` para métodos de clase.
- `@property` para crear atributos calculados.

**Enlaces a documentación:**

[Decoradores](https://docs.python.org/es/3/glossary.html#term-decorator): Explica qué son los decoradores, cómo se usan para modificar funciones y métodos, ejemplos de uso y ventajas en la programación Python.
