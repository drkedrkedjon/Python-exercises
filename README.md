### Activate virtual enviroment

source venv/bin/activate
deactivate
El "nombre" o "nombre accesible" (accName) de un elemento es una cadena de texto que está asociada programáticamente con un elemento, y está expuesta por el navegador a las tecnologías de asistencia a través del árbol de accesibilidad. Este nombre se utiliza para proporcionar una etiqueta para el elemento a los usuarios de tecnologías de asistencia.

### Diferencia entre accesible label y name

- En teoria se recomienda que son identicos. En practica siempre deben ser indenticos
- Para los componentes de la interfaz de usuario con etiquetas que incluyen texto o imágenes de texto, el nombre contiene el texto que se presenta visualmente.
- La parte de "texto que se presenta visualmente" se refiere a la etiqueta de un elemento. El "nombre" se refiere a la cadena de texto que se presenta a las tecnologías de asistencia.
- El hecho de que un elemento tenga una etiqueta no garantiza que tenga un nombre accesible. Debes asegurarte de que lo haga.
  Ejemplo:

```html
<!-- this input field has a visible label but no name -->
<label>Username</label>
<input type="text" />
<!-- Ahora si lo tiene -->
<label for="username">Username</label>
<input
  type="text"
  id="username"
/>
```

Icon button ejemplo:

```html
<!-- this link has a graphical label, but no (pronouncable) name -->
<a href="https://twitter.com/SaraSoueidan">
  <i class="fa-brands fa-twitter"></i>
</a>

<!-- this link has a graphical label, and an accessible name -->
<a href="https://twitter.com/SaraSoueidan">
  <span class="visually-hidden">Twitter</span>
  <i class="fa-brands fa-twitter"></i>
</a>
```

- Si es interactivo, debe tener un nombre accesible.
- Todos los form elementos
- La información que se presenta visualmente pueda determinarse programáticamente para que los usuarios de tecnología de asistencia puedan percibir la misma información que se transmite visualmente. Cuando se proporcionan etiquetas visibles, estas etiquetas deben asociarse programáticamente con sus elementos.
- Para todos los componentes de la interfaz de usuario (incluidos, entre otros: elementos de formulario, enlaces y componentes generados por scripts), el nombre y el rol se pueden determinar mediante programación.

Algunos elementos no interactivos se pueden beneficiar de tener accessibles names

- Cuando tiene varios de la misma región de referencia, estas regiones se benefician de nombres accesibles que identifican el propósito de cada región, lo que ayuda al usuario a navegar por la página de manera más eficiente.
- Cuando proporciona un nombre a un grupo de controles en un formulario, el nombre del grupo proporciona contexto que ayuda a identificar aún más el propósito de estos controles.

```html
<fieldset>
  <legend>I want to receive</legend>
  <div>
    <input
      type="checkbox"
      name="newsletter"
      id="check_1"
    />
    <label for="check_1">The weekly newsletter</label>
  </div>
  <div>
    <input
      type="checkbox"
      name="promotions"
      id="check_2"
    />
    <label for="check_2">Offers and promotions</label>
  </div>
  […]
</fieldset>
```

- No todos los elementos HTML pueden tener un nombre.
- divs y spans son contenedores genéricos. Si recuerdas del capítulo de semántica HTML, dijimos que el rol genérico crea un elemento contenedor sin nombre que no tiene significado semántico por sí mismo. Así que los contenedores genéricos no están destinados a tener un nombre accesible. Y esto se aplica a todos los elementos que se asignan a un rol genérico. Si el papel de un elemento no es significativo, no obtiene un nombre accesible. Esto significa que poner una etiqueta aria en divs y spans no solucionará los problemas de accesibilidad causados por el mal uso de estos elementos.
- Si está utilizando un div como contenedor para una región que debería tener un nombre, tendrá que darle al div un rol significativo que describa su propósito para que califique para un nombre accesible.

### Accesible description

Además de un nombre accesible que identifica un componente, algunos componentes de la interfaz de usuario pueden beneficiarse de una "descripción" o una "descripción accesible".

Una descripción accesible (accDesc) es similar a un nombre accesible en que:

- También ayuda al usuario a entender cómo usar un componente, y
- Está expuesto por el navegador a tecnologías de asistencia en el árbol de accesibilidad cuando está asociado programáticamente con un elemento.\

La diferencia entre description y name

- Un nombre accesible suele ser corto y conciso. Mientras que una descripción accesible a menudo es más larga y proporciona pistas adicionales que pueden describir cómo usar el componente. Por ejemplo, los requisitos del campo de formulario y los mensajes de error proporcionan información adicional al usuario sobre el tipo de entrada que espera el campo de entrada. Estas descripciones se pueden asociar mediante programación con el campo de entrada utilizando el atributo `aria-describedby`:

```html
<label for="passw0rd">Password</label>
<input
  type="password"
  id="passw0rd"
  aria-describedby="passw0rd-description"
/>
<p id="passw0rd-description">
  Your password should be at least 8 characters long and contain at least one
  special character.
</p>
```

- El accDesc de un elemento se adje al nombre y rol del elemento y se presenta al usuario como una cadena plana de texto.
- Por ejemplo, error message de un formulario

# Tehnicas para proporcional los nombres y descriptiones usando HTML y ARIA

## Usando HTML

- Del contenido de un elemento,
- De un atributo, o
- De otro elemento.

### Del contenido de un elemento

```html
<button>Download PDF</button>
```

Si el elemento tiene ::before or ::after el contenido sera incluyido. Tambien icinos y emojis. Usar `svg` inline icons y ocultar con `aria-hidden`

### Usando otro elemento

Algunos elementos pueden obtener su nombre accesible de otros elementos. Por ejemplo, un campo de entrada de formulario obtiene su nombre accesible de un elemento `label` cuando la etiqueta se asocia programáticamente con él utilizando los atributos for e id:

```html
<!-- the for attribute associates the label with the input, making sure it is used as an accessible name -->
<label for="email">Email address</label>
<input
  type="email"
  id="email"
  autocomplete="email"
/>
```

El elemento label no es el único elemento que proporciona un nombre accesible para otro elemento. Cuando el primer hijo de un grupo `fieldset` es un `legend`, el navegador utiliza el contenido del legend como un accName para el grupo:

```html
<!-- The group’s accName is "Shipping address" -->
<fieldset>
  <legend>Shipping address</legend>
  ...
</fieldset>
```

De manera similar: `caption` para una `table`

### Con un attributo

Algunos elementos HTML obtienen su nombre accesible de un atributo.

```html
<!-- De value -->
<input
  type="submit"
  value="Send message"
/>
<!-- De alt -->
<img
  src="./path/to/image.png"
  alt="A cat sleeping on a bed."
/>
```

Hay otro atributo que se puede usar para proporcionar un nombre accesible a la mayoría de los elementos HTML: el atributo de título. Pero generalmente no debe usar el atributo de título para proporcionar nombres accesibles a los elementos. La única excepción a esto es `iframe`

```html
<iframe
  src=".."
  frameborder="0"
  title="[ frame accName ]"
></iframe>
```

## Usando ARIA

Casi siempre quieres proporcionar información de accesibilidad usando HTML nativo cuando puedes hacerlo. Pero hay casos en los que puede necesitar usar atributos de ARIA, ya sea para:

- Asociar explícitamente un elemento con otro cuando no hay una forma nativa de hacerlo,
- Usar múltiples elementos como un nombre accesible para otro, o
- Corregir nombres accesibles en una base de código existente sin cambiar el marcado. Por ejemplo, desea proporcionar accNames a elementos que no tienen uno, pero no puede hacerlo cambiando el marcado de esos elementos.

Hay dos atributos ARIA que se pueden usar para proporcionar o anular el nombre accesible de un elemento: aria-labelledby y aria-label.

### aria-labeledby

El atributo aria-labelledby se utiliza cuando el texto que desea utilizar como nombre accesible ya está presente en otra parte de la página.

```html
<nav aria-labelledby="heading2_ID">
  <h3 id="heading2_ID">Find us elsewhere</h3>
  ..
</nav>

<input
  type="search"
  aria-labelledby="search-btn"
/>
<button id="search-btn">Search</button>
```

aria-labeledby tiene la mas alta prioridad para dar nombre

### aria-label

El atributo aria-label es similar en efecto a aria-labelledby en el sentido de que proporciona un accName para el elemento en el que se utiliza. Pero a diferencia de aria-labelledby, que utiliza el texto calculado de otro elemento como nombre accesible, el atributo aria-label toma una cadena de texto como valor, y esta cadena se convierte en el nombre accesible del elemento.

```html
<!-- This button os treated as empty; it gets its accName from the aria-label attribute; otherwise, it would not have one. -->
<button aria-label="Settings">
  <i></i>
</button>
```

Aria-label debe reservarse para cuando no haya texto visible en la página para hacer referencia o cuando realizar un seguimiento de los valores de identificación sería demasiado difícil.

Hay un par de follones con eso:

- No se traduce bien por maquinas
- Si el elemento para el que está proporcionando un nombre accesible no tiene una etiqueta visible (como es el caso de los botones de iconos, por ejemplo), puede usar un `visualy-hidden` class o `hidden` attributo

```html
<button>
  <span class="visually-hidden">Compose Message</span>
  <svg
    viewBox=".."
    aria-hidden="true"
  >
    ...
  </svg>
</button>

<!-- OR -->
<button aria-labelledby="btn-label">
  <span
    id="btn-label"
    hidden
    >Compose Message</span
  >
  <svg
    viewBox=".."
    aria-hidden="true"
  >
    ...
  </svg>
</button>
```

- Aria-label y aria-labelledby no funcionan en todos los elementos
- Aria-labelledby y aria-label tienen la mayor prioridad en el cálculo de accName de un elemento. Esto significa que el accName proporcionado por aria-label o aria-labelledby anulará el contenido del elemento en el cálculo accName.

## ARIA descriptiones

### aria-describedby

El atributo `aria-describedby` es similar a aria-labelledby, excepto que se utiliza para proporcionar una descripción accesible (accDesc) a un elemento en lugar de un accName. También acepta uno o más ID de elementos que juntos proporcionan un accDesc al elemento en el que se utiliza.

```html
<label for="passw0rd">Password</label>
<input
  type="password"
  id="passw0rd"
  aria-describedby="passw0rd-description"
/>
<p id="passw0rd-description">
  You password should be at least 8 characters long and contain at least one
  special character.
</p>
```

El contenido descriptivo al que se hace referencia en aria-describedby se aplana a una cadena de texto. Esta cadena se apunta, como texto descriptivo, después de que el lector de pantalla haya anunciado el nombre accesible y la función de un elemento.
Si la description contiene otros elementos su semantica disaparecera. Solo `alt` de imagen sera anunciada

### aria-description

ARIA 1.3 define un nuevo atributo llamado aria-description. aria-description no está actualmente completamente implementado en todos los navegadores, por lo que aún no está listo para una amplia adopción. Tambien puede no ser traducido por traductores

### aria-details

- Puede haber situaciones en las que necesite proporcionar más detalles sobre un elemento de los que normalmente serían adecuados para un accDesc. Soporte en navegador es flojo...
- Por lo tanto, su propósito es hacer saber al usuario que hay información adicional asociada con el elemento con el que están interactuando, y que es posible que quieran revisar esta información.

```html
<label for="cvv">CVV</label>
<input
  type="text"
  id="cvv"
  aria-details="cvv-details"
/>

<details id="cvv-details">
  <summary><strong>What is CVV?</strong></summary>

  <p>
    The Card Verification Value (CVV) or Card Verification Code (CVC) is a code
    printed on your debit or credit card.
  </p>
</details>
```

- No se aplana a una cadena de texto, y también es la razón por la que no es anunciado automáticamente por el lector de pantalla. El lector de pantalla solo anunciará la presencia de esta información al usuario. Pero eso es todo lo que hace. Tampoco moverá el enfoque del usuario a la información.

## Orden de como se asigna accName a un elemento por el navegador

Cuando el navegador busca determinar el nombre accesible de un elemento:

- Comprueba si el elemento tiene un atributo aria-labelledby. Si lo hace, y si el ID en el atributo es una referencia válida a un elemento en la página, utiliza el texto calculado del elemento referenciado para proporcionar el nombre accesible para el elemento.
- De lo contrario (si aria-labelledby no está presente) comprueba si el elemento tiene un atributo aria-label. Si lo hace, utiliza el valor del atributo aria-label como nombre accesible.
- De lo contrario, y a menos que el elemento esté marcado como presentacional usando role="presentation" o role="none" (en cuyo caso el elemento ya no acepta un accName), el navegador comprueba si el elemento puede obtener su nombre:
  - De un atributo HTML (como título o alt),
  - De otro elemento (como etiqueta o legend),
  - O de su contenido.

Evitar poner dos nombres, se lia olimpicamente...

### El resto, osea detalles de cada elemento por separado - wer curso

https://practical-accessibility.today/chapters/accName-computation/

- Así que lo primero que recomiendo es considerar si necesitas o no usar ARIA.
- Debido a que HTML proporciona formas nativas de proporcionar accNames a la mayoría de los elementos a los que se les permite tener uno, intente usarlos siempre que pueda.
- Y cuando utilice técnicas HTML nativas para proporcionar un accName, evite usar el atributo title. Utilice una de las otras técnicas disponibles para cada elemento. Hay al menos 3 formas diferentes de proporcionar un nombre accesible a la mayoría de los elementos que pueden tener uno. Y casi siempre hay un método de nomenclatura que es mejor que el título, que, como ya sabes, debes evitar usar siempre que tengas una opción.
- Por supuesto, habrá ocasiones en las que necesitará buscar atributos de ARIA para proporcionar un nombre accesible, ya sea porque no hay un mecanismo HTML nativo para hacerlo, o porque necesita arreglar los componentes existentes y ARIA es la única manera de hacerlo.
- Cuando use ARIA, pregúntese si el texto que desea proporcionar como nombre accesible ya existe en otra parte de la página. Si es así, use aria-labelledby para asociar ese texto con su elemento o componente para el que está proporcionando un accName.
- Si no hay ningún elemento que se pueda usar para proporcionar un nombre accesible, haga uno. Si no puedes, entonces tal vez tengas que usar aria-label.
- Como regla general, prefiera usar contenido de texto sobre texto en atributos siempre que sea posible.

Cuando necesito proporcionar un accName a un elemento, sigo un orden de prioridad para qué método alcanzar por defecto. El orden o prioridad es:

- Utilice contenido HTML (como texto en un a o texto en un button
- De lo contrario, utilice un atributo o elemento HTML (como alt o label).
- De lo contrario, use aria-labelled haciendo referencia a un elemento que ya está en la página.
- De lo contrario, cuando ninguno de los métodos anteriores sea posible, use aria-label.
