# Trie
## Integrantes
1. [426061748] [Hernandez Lopez Alejandro]
2. [323038320] [Hernandez Soria Miriam]
3. [323135340] [Flores Quero Aarón]
4. [323164029] [Rodríguez Tlapalamatl Diego]
   
## Objetivo 
Analizar el funcionamiento, la estructura interna y la complejidad del Trie, implementando sus operaciones  (inserción, búsqueda,eliminación y búsqueda por prefijo) para demostrar su eficiencia y como lo podemos aplicar en la resolución de problemas de procesamiento de cadenas y autocompletado.

## Concepto 
Un trie es una estructura de datos (una forma de organizar información dentro de un programa) que utiliza las partes de la clave para organizar y buscar entre la colección de datos que almacena. O, dicho de otra manera, un trie es un árbol de prefijos (prefijo proviene del latín praefixus (‘colocado delante’), es el comienzo de las palabras). 

Cuando buscas palabras en un diccionario haces uso de los prefijos, ya que en lugar de buscar en primera instancia la palabra por todas las páginas del diccionario, primero buscas la primera letra, luego la segunda y así sucesivamente hasta obtener la palabra, el trie funciona de forma similar en una computadora. 

## Contexto 
El nombre trie proviene de retrieval, que en inglés significa “recuperación” (recuperar información guardada). Se pronuncia como try para distinguirlo de tree (“árbol” en inglés, es la estructura de datos en la que se basa el trie), porque los dos suenan similar y eso generaba confusiones.

### Antecedentes 
Los tries aparecieron en 1959, el investigador René de la Briandais los propuso de forma independiente, y poco después Edward Fredkin los desarrolló por su cuenta. El nombre trie lo propuso Fredkin hacia 1960.

En esa época, a comparación con la actualidad las computadoras eran muy lentas y tenían poca memoria, por lo que buscar formas de optimizar el manejo de datos, búsquedas y etc. era de suma importancia. Buscar una palabra en una lista enorme de palabras, como en un diccionario, comparándola una a una era sumamente costoso. Se necesitaba por ello una forma de guardar palabras de tal forma que buscarlas fuese más sencillo y rápido, la idea para solventar esta necesidad fue aprovechar los prefijos, ya que muchas palabras los comparten, por ejemplo: "inolvidable", "innombrable" , "insaciable" que comparten el prefijo "in", entonces ya no haria falta guardar in tres veces.

### Desarrollo 
Desde su aparición, el trie fue creciendo y mejorando con el tiempo.

Se volvió una estructura de uso general. Al principio se pensó para guardar palabras, pero después se vio que servía para cualquier clave formada por una secuencia de símbolos de un conjunto limitado (lo que se llama un alfabeto): letras, números, códigos o rutas.

Se formalizó con las matemáticas. Los estudiosos descubrieron que un trie es un caso especial de un autómata finito (un modelo teórico, parecido a un mapa de estados por los que se va pasando según los símbolos que se leen). Esto le dio una base sólida para ser analizado y comparado con otras estructuras.

Se compararon sus ventajas con las de otras estructuras. Frente a otras formas de guardar información, el trie destacó porque su velocidad depende de la longitud de la palabra buscada y no de cuántas palabras haya guardadas. También destacó por permitir búsquedas por prefijo, algo que otras estructuras no hacen bien.

Aparecieron distintas versiones para ahorrar espacio. Con los años se probaron varias maneras de programar un trie, buscando un equilibrio entre rapidez y uso de memoria. Una de las más conocidas es el árbol ternario de búsqueda, que combina la idea del trie con la de otro tipo de árbol.

Nació la versión comprimida: PATRICIA. En 1968, Donald R. Morrison presentó una mejora llamada PATRICIA (siglas en inglés de Practical Algorithm To Retrieve Information Coded In Alphanumeric, que significa “algoritmo práctico para recuperar información codificada en alfanumérico”, es decir, letras y números). Su objetivo fue evitar gastar espacio en partes del árbol donde no hay ninguna ramificación. También se le conoce como radix tree (“árbol de raíces”).

Surgieron variantes para otros problemas. Una de ellas es el trie de sufijos (y su versión comprimida, el árbol de sufijos), que en lugar de guardar palabras guarda todos los finales posibles de un texto largo.

### Actualidad 
Hoy los tries y sus variantes están presentes en muchas cosas que usamos todos los días:

#### Autocompletado.
Cuando la barra de búsqueda te sugiere mientras escribes, o cuando una terminal (la ventana donde se escriben comandos) completa un comando, suele haber un trie detrás.


#### Corrección ortográfica y teclado del celular.
Sirven para saber rápidamente si lo que escribes puede convertirse en una palabra válida y qué sugerencias ofrecer.

#### Juegos de palabras y teclados antiguos.
Los resolutores de Scrabble y el sistema T9 (aquellos teléfonos donde cada tecla representaba varias letras) los usaban para validar palabras.

#### Redes de internet. 
Los routers (aparatos que deciden por dónde viaja cada paquete de datos) usan variantes tipo PATRICIA para elegir la mejor ruta. Tratan cada bit (el 0 o el 1 de una dirección IP, que es como la “dirección postal” de un dispositivo) como si fuera una letra, y buscan la coincidencia de prefijo más larga.

#### DNS y Ethereum.
El DNS (el sistema que convierte “www.wikiejemplo.com” en la dirección real del servidor) y Ethereum (una red de criptomonedas) usan estructuras derivadas de PATRICIA.

#### Buscadores de texto.
Apache Lucene, la base de motores como Elasticsearch y Solr, usa estructuras compactas derivadas de los tries para indexar (organizar el texto para encontrarlo rápido) enormes cantidades de información.

#### Genética y buscadores de código.
Las variantes de sufijos permiten comprobar si una frase o secuencia aparece dentro de un texto larguísimo, como el ADN (el material genético).

Un trie sencillo puede gastar bastante memoria cuando el diccionario es muy grande. Por eso, en el mundo real se usan mucho las versiones comprimidas, y se acostumbra medir el consumo real antes de decidir cuál usar.

## Teoría 
### Paso a paso teórico

Un trie, también llamado árbol de prefijos, es una estructura de datos con forma de árbol construida sobre un alfabeto, que sirve para guardar y recuperar cadenas de manera eficiente, sobre todo cuando muchas de ellas comparten el mismo inicio. En un trie las aristas son las que representan los caracteres, y los nodos representan los estados. Cada nodo corresponde al prefijo que se ha leído hasta ese punto, y su profundidad indica cuántos caracteres se llevan. La raíz representa la cadena vacía, y cada palabra se obtiene leyendo las etiquetas de las aristas del camino que va desde la raíz hasta el nodo donde termina.

Cada nodo almacena dos elementos. El primero es la información de sus hijos, es decir, a qué nodo se llega con cada carácter posible. El segundo es una bandera booleana que indica si en ese nodo termina una palabra guardada. Esta bandera es necesaria porque llegar a un nodo no implica que la palabra exista. Si se guarda “casa”, el nodo del prefijo “cas” forma parte del árbol, pero “cas” no es una palabra almacenada, solo es el inicio de otra. Por la misma razón, un nodo marcado como final de palabra no tiene por qué ser una hoja, ya que una palabra puede ser prefijo de otra más larga.

Los hijos de un nodo se pueden implementar de dos formas. La primera es un arreglo de tamaño |Σ|, con una posición por cada carácter del alfabeto. Por ejemplo, con las letras minúsculas el arreglo tiene 26 posiciones y el hijo de la letra “c” se encuentra en el índice que resulta de restarle “a”. Esta forma da acceso directo en tiempo constante en el peor caso, pero cada nodo reserva |Σ| posiciones aunque casi todas estén vacías, y eso desperdicia memoria cuando el alfabeto es grande. La segunda es una tabla hash, o diccionario, que asocia cada carácter con su nodo hijo y solo guarda los hijos que existen. Con ella cada nodo ocupa únicamente lo que necesita, y además permite alfabetos arbitrarios, como caracteres Unicode, sin definir un tamaño fijo. A cambio, el acceso es constante en promedio y no en el peor caso, y la tabla tiene algo de sobrecarga propia. En ambos casos la lógica de las operaciones es la misma, y lo único que cambia es cómo se consulta y se crea un hijo.

La inserción de una palabra comienza en la raíz y recorre la palabra carácter por carácter. Si el nodo actual ya tiene una arista con ese carácter, el recorrido avanza por ella. Si no la tiene, se crea un nodo nuevo, se enlaza con una arista etiquetada con ese carácter y el recorrido avanza hacia él. Al procesar el último carácter, se marca el nodo en el que se terminó como final de palabra. Gracias a este procedimiento, las palabras que comparten un prefijo comparten también los nodos de ese prefijo, de modo que cada prefijo común se almacena una sola vez. Por ejemplo, “casa” y “caso” comparten los nodos de los prefijos “c”, “ca” y “cas”, y solo se diferencian en el último nodo.

La búsqueda de una palabra completa sigue el mismo recorrido desde la raíz. Si en algún momento no existe una arista con el carácter que se está procesando, la palabra no está en el trie. Si se logra recorrer toda la palabra, queda una última comprobación, que consiste en revisar la bandera del último nodo. La palabra existe únicamente si esa bandera está activada.

La búsqueda por prefijo es igual, pero omite esa comprobación final, porque basta con poder recorrer todo el prefijo para asegurar que existe al menos una palabra guardada que empieza con él. Esta es la operación que hace posible el autocompletado, ya que una vez ubicado el nodo del prefijo, todas las palabras que lo completan están en el subárbol que cuelga de ese nodo.

La eliminación de una palabra comienza igual que la búsqueda, recorriendo el camino desde la raíz. Si en algún momento falta una arista, o si el último nodo no está marcado como final de palabra, la palabra no estaba guardada y no se hace nada. Si la palabra existe, primero se desactiva la bandera de fin de palabra del último nodo. Después se regresa por el camino hacia la raíz, borrando cada nodo que ya no sea necesario. Un nodo se puede borrar solo si no tiene hijos y no es final de otra palabra. Por eso, al eliminar “casa” estando también guardada “caso”, solo se borra el nodo del prefijo “casa”, y los nodos de “c”, “ca” y “cas” se conservan porque “caso” todavía los usa. De la misma forma, al eliminar “cas” cuando existe “casa”, no se borra ningún nodo y solo se desactiva la bandera.

En cuanto a la complejidad, la inserción, la búsqueda, la búsqueda por prefijo y la eliminación tienen un costo de O(|s|), donde |s| es la longitud de la cadena que se procesa. Este costo no depende de cuántas palabras haya almacenadas, lo que distingue al trie de otras estructuras y responde al objetivo del tema. En espacio, el peor caso con arreglos es O(N · M · |Σ|), donde N es el número de cadenas, M es la longitud de la cadena más larga y |Σ| es el tamaño del alfabeto, ya que cada nodo reserva espacio para |Σ| hijos. Como en la mayoría de los problemas el alfabeto es fijo, por ejemplo las letras minúsculas, |Σ| se puede considerar constante y el espacio queda en O(N · M). Con tablas hash el espacio es proporcional al número de nodos y aristas realmente creados, que también es O(N · M) en el peor caso sin importar el tamaño del alfabeto. En la práctica el trie suele ocupar menos que ese límite, porque las palabras comparten prefijos.

Una tabla hash que guarda las palabras completas busca una palabra en tiempo O(|s|) en promedio, porque primero debe calcular el hash de toda la cadena. Es un costo parecido al del trie, pero no permite la búsqueda por prefijo, ya que el hash de “cas” no tiene ninguna relación con el de “casa”, y por eso habría que revisar todas las palabras guardadas. En un árbol binario de búsqueda, cada comparación entre cadenas puede costar O(|s|) y se hacen cerca de log N comparaciones, así que cada operación cuesta O(|s| · log N) y depende de cuántas palabras haya guardadas. Además, las palabras que comparten prefijo se guardan completas y repetidas, mientras que en el trie ese prefijo se almacena una sola vez. En cambio, el trie crea un nodo por carácter, por lo que puede gastar más memoria que una tabla hash o un árbol binario cuando las palabras casi no comparten prefijos. Entonces, el trie conviene cuando se necesitan operaciones por prefijo o cuando muchas palabras comparten su inicio, y una tabla hash conviene si solo se buscan palabras completas.

## Demostración (Ejemplos de resultados)
Primero formaremos un trie sencillo (sin code), con las letras del abecedario inglés $\sum $ {a,b,c,...,y,z}.
Lo formaremos con las siguientes palabras: [can,monkey,tree,cat,money,pencil,penny]

<img src="./media/Trie_1.png" alt="Alt Text" width="350" height="400">

Podemos ver que por cada nodo, guardaremos a lo mas $|\sum|$ hijos. Entonces en el peor caso la complejidad espacial de un Trie es de $O(N \cdot M \cdot |\sum|)$. Donde $N$ es el número de elementos que hay en el trie y $M$ es la longitud máxima de un string.

Usualmente cuando se use un Trie, $|\sum|$ ya esta definido, por lo que su tamaño es constante, en estos casos tenemos una complejidad de $O(N \cdot M)$

**OPERACIONES DEL TRIE**
Los códigos de las operaciones del trie están en `src/Trie.py`

Por último para hacer una demostración resolveremos el problema Leetcode 1268 - Suggestions System :)
<!-- CREO QUE ESTO DE ACA (ANALISIS DE COMPLEJIDADES QUEDARIA MEJOR EN LA PARTE DE ANALISIS DE RESULTADOS)
**Complejidad temporal:** 
- Ordenamiento inicial:$O(N \ log \ N \cdot L)$. N es el número de productos y L su longitud promedio.
- Construir el Trie: $O(S)$. S es la suma total de caracteres de todos los productos
- Búsqueda de sugerencias: $O(M)$. M es la longitud de `searchWord`.  
**Complejidad espacial:** $O(S). Para almacenar los nodos del Trie. Guardar referencias a las cadenas en suggestions no duplica los strings en memoria en Python, solo guarda sus punteros.$



-->


## Análisis de resultados

## En base a "Leetcode1268"
### 1. La Estructura del Nodo (`TrieNode`)

**En la teoría:**
Cada nodo almacena dos elementos:
1. La información de sus hijos (un arreglo o una tabla hash).
2. Una bandera booleana que indica si en ese nodo termina una palabra.
Usa una tabla hash que asocia cada carácter con su nodo hijo, guardando solo los que existen para ahorrar memoria.

**En el código:**
```python
class TrieNode:
    def __init__(self) -> None:
        self.children: dict[str, TrieNode] = {}
        self.suggestions: list[str] = []
```
*   **Correlación directa:** Se utiliza exactamente la aproximación de la tabla hash mediante un diccionario de Python (`dict[str, TrieNode]`). Esto hace que el nodo ocupe solo la memoria necesaria para las letras que realmente le siguen.
*   **Adaptación práctica:** La "bandera booleana" de fin de palabra ha sido reemplazada por una lista `self.suggestions`. Como el objetivo del codigo es devolver hasta 3 sugerencias por prefijo, es mucho más eficiente guardar las respuestas directamente en el nodo durante la construcción del árbol, en lugar de usar una bandera booleana y tener que recorrer todo el subárbol cada vez que se hace una búsqueda.

### 2. Inserción paso a paso (`insert`)

**En la teoría:**
Se explica que la inserción comienza en la raíz y recorre la palabra carácter por carácter. Si el nodo actual no tiene una arista con ese carácter, se crea un nodo nuevo. Gracias a esto, las palabras que comparten un prefijo comparten los mismos nodos.

**En el código:**
```python
def insert(self, word: str) -> None:
    node = self.root
    for char in word:
        if char not in node.children:
            node.children[char] = TrieNode()
        node = node.children[char]
        
        if len(node.suggestions) < 3:
            node.suggestions.append(word)
```
*   **Correlación directa:** El bucle `for char in word:` es la representación exacta del recorrido por la cadena paso a paso. La comprobación `if char not in node.children:` es el momento en que se crean los nuevos nodos (aristas) si no existen.
*   **El "Truco" del Autocompletado:** Mientras se baja por el árbol creando los prefijos comunes, el código inserta la palabra completa (`word`) en la lista de `suggestions` del nodo actual (limitado a 3). Esto materializa el concepto de que el trie es ideal para autocompletado, ya que pre-calcula los resultados de manera directa.

### 3. Búsqueda por Prefijo (`get_suggestions`)

**En la teoría:**
La búsqueda por prefijo recorre el camino desde la raíz y que omite la comprobación final, porque basta con poder recorrer todo el prefijo para asegurar que existe al menos una palabra todas las palabras que lo completan están en el subárbol.

**En el código (`leetcode1268.py`):**
```python
def get_suggestions(self, prefix: str) -> List[List[str]]:
    result: List[List[str]] = []
    node: TrieNode | None = self.root
    
    for char in prefix:
        if node and char in node.children:
            node = node.children[char]
            result.append(node.suggestions)
        else:
            node = None
            result.append([])
            
    return result
```
*   **Correlación directa:** Se recorre el prefijo ingresado `searchWord` en el contexto del problema, letra por letra. Si la arista (carácter) existe, avanzamos `node = node.children[char]`.
*   **Optimización de Búsqueda:** En lugar de recorrer el subárbol entero para encontrar qué palabras hay debajo (lo cual aumentaría la complejidad temporal), el código simplemente extrae `node.suggestions`, que ya fueron guardadas durante la inserción. 
*   **Manejo de prefijos inexistentes:** Si se teclea una letra que rompe el camino (`else:`), el nodo se vuelve nulo y para ese carácter (y los siguientes) simplemente se devuelven listas vacías `[]`, tal como dicta la lógica de un sistema de autocompletado real.

### 4. Construcción General y Ordenamiento (`suggestedProducts`)

**En el código:**
```python
def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
    products.sort() # <-- CRUCIAL
    # ...
```
*   **Conexión con el concepto teórico:** Anteriormente se menciona que un trie almacena información basándose en alfabetos y secuencias. En el codigo, se piden las palabras ordenadas lexicográficamente(en este caso, orden alfabético). Al ordenar el arreglo inicial (`products.sort()`), nos garantizamos que cuando pasamos por un nodo y guardamos las palabras en `node.suggestions`, las primeras 3 palabras que pasen por ahí siempre serán, por defecto, las 3 menores lexicográficamente. Esta es una optimización que une el concepto de ordenamiento de cadenas con la estructura en árbol del Trie.

### 5. Análisis de Resultados en Terminal (Ejecución Práctica)

Para visualizar cómo interactúa el código con los datos, simulemos la ejecución en consola.

**Datos de entrada:**
*   `products`: `["mobile", "mouse", "moneypot", "monitor", "mousepad"]`
*   `searchWord`: `"mouse"`

### Paso 1: Ordenamiento Interno
El método `suggestedProducts` primero ejecuta `products.sort()`. Internamente, el arreglo queda así:
`["mobile", "moneypot", "monitor", "mouse", "mousepad"]`

### Paso 2: Creación del Trie e Inserción
El código inserta las palabras. Debido a la línea `if len(node.suggestions) < 3:`, el Trie almacena esto en sus nodos al recorrer la letra **'m'** y **'o'** (prefijo `"mo"`):
*   Inserta "mobile" -> `node.suggestions` tiene `["mobile"]`
*   Inserta "moneypot" -> `node.suggestions` tiene `["mobile", "moneypot"]`
*   Inserta "monitor" -> `node.suggestions` tiene `["mobile", "moneypot", "monitor"]`
*   Inserta "mouse" -> *El límite de 3 se alcanzó, se ignora en este nodo.*
*   Inserta "mousepad" -> *El límite de 3 se alcanzó, se ignora en este nodo.*

### Paso 3: Salida en la Terminal
Al evaluar el `searchWord` ("mouse") letra por letra, el código retorna el siguiente resultado en la terminal:

```console
[
  ["mobile","moneypot","monitor"],    # Al escribir 'm'
  ["mobile","moneypot","monitor"],    # Al escribir 'm' -> 'o'
  ["mouse","mousepad"],               # Al escribir 'm' -> 'o' -> 'u'
  ["mouse","mousepad"],               # Al escribir 'm' -> 'o' -> 'u' -> 's'
  ["mouse","mousepad"]                # Al escribir 'm' -> 'o' -> 'u' -> 's' -> 'e'
]
```

**Análisis de esta salida:**
1. **Límites exactos:** Observamos perfectamente la restricción de máximo 3 sugerencias en los prefijos `"m"` y `"mo"`. Aunque hay 5 productos que empiezan con `"mo"`, la terminal arroja exactamente los 3 primeros alfabéticamente.
2. **Filtrado dinámico:** Al teclear la letra `"u"`, los productos `"mobile"`, `"moneypot"` y `"monitor"` ya no coinciden. El Trie avanza a un nuevo subárbol donde solo se insertaron `"mouse"` y `"mousepad"`.
3. **Eficiencia en memoria y tiempo:** Tal como se promete en la teoría, el programa no tuvo que buscar entre todos los productos de nuevo cada vez que se escribió una letra; solo extrajo la lista pre-calculada (`node.suggestions`) que encontró en cada nodo.

## Rendimiento y Casos de Uso del Trie

### 1. ¿Por qué el Trie es tan rápido?
El Trie es extremadamente rápido porque elimina las comparaciones redundantes. Cuando buscas en una lista o incluso en un Árbol Binario de Búsqueda (BST), tienes que comparar la cadena completa o gran parte de ella varias veces. En un Trie cada paso que das por el árbol confirma la coincidencia de un carácter. No hay necesidad de comparar prefijos repetidamente, el camino que tomas es la confirmación de que el prefijo coincide. El acceso directo a los hijos ya sea por índice de un arreglo o por llave de un diccionario/hash permite saltar de estado en estado en tiempo constante O(1) por cada carácter.

### 2. El tiempo de inserción y búsqueda solo dependen de la longitud de s y no de la longitud del diccionario
Esto se debe a la naturaleza estructurada del árbol. Imagina que estás buscando la palabra "gato" de longitud 4 en un diccionario de un millón de palabras. 
* En el primer paso, buscas el nodo hijo 'g' desde la raíz. No importa si hay un millón de palabras, la búsqueda de 'g' en el diccionario o arreglo del nodo raíz toma O(1). 
* En el segundo paso, buscas 'a' desde el nodo 'g'. De nuevo, toma O(1).
* Lo haces 4 veces, la longitud de s. 

Como las ramas agrupan automáticamente todas las palabras que comparten el mismo prefijo, nunca tienes que iterar a través del resto de palabras del diccionario. Tu camino está dictado exclusivamente por las letras de la palabra s que estás insertando o buscando, resultando en un tiempo O(|s|).

### 3. En dónde es malo y porqué
El punto débil del Trie es el consumo de memoria. 
Es malo cuando se trata de almacenar palabras largas que no comparten prefijos generando un arbol disperso. Si se implementa usando arreglos fijos para los hijos como un arreglo de 27 posiciones para las letras del abecedario español, cada nodo reserva espacio para todo el alfabeto, incluso si solo tiene un hijo. Esto genera una cantidad masiva de espacio desperdiciado en memoria. Incluso usando tablas hash, la sobrecarga de crear tantos nodos y punteros para cada letra individual de cada palabra puede ser muy superior a simplemente guardar las cadenas en una lista plana o un HashSet.

### 4. Cuándo es recomendable usarlo y cuándo no

**Recomendable usarlo cuando:**
* Necesitas hacer búsquedas por prefijo como autocompletado, sugerencias de búsqueda, enrutamientos IP.
* Quieres encontrar la coincidencia de prefijo más larga.
* Tienes un diccionario donde las palabras comparten muchísimos prefijos.
* Necesitas implementar correctores ortográficos o resolver juegos de palabras como Scrabble buscando ramificaciones válidas rápidamente.

**NO es recomendable usarlo cuando:**
* **Solo necesitas búsquedas exactas:** Si solo quieres saber si una palabra existe o no sin importar los prefijos, una Tabla Hash es mucho mejor, da búsquedas exactas en O(1) real y gasta mucha menos memoria.
* **La memoria RAM es muy limitada:** El overhead de los punteros/nodos puede causar problemas de memoria.
* **El alfabeto es enorme y variable:** Como en textos que mezclan múltiples lenguajes sin compartir raíces.

### 5. ¿Por qué en el problema del código es mejor el Trie y no solo se usa otro approach?
El problema pide devolver sugerencias de productos a medida que el usuario teclea cada carácter de una palabra de búsqueda. 
Si usáramos otro enfoque, como iterar sobre la lista de productos por cada prefijo nuevo, el tiempo sería muy alto $O(N \cdot M)$ por cada letra tecleada. 
Otra opción común es ordenar la lista y usar Búsqueda Binaria (`Binary Search` / `bisect`). Aunque la búsqueda binaria es buena, requiere ejecutar un algoritmo $O(\log N)$ para encontrar el inicio del prefijo por cada carácter que se escribe, y luego extraer las siguientes 3 palabras.

**El Trie es superior aquí porque:**
1. El usuario teclea letra por letra, el Trie avanza nodo por nodo por cada letra, guardando el estado. Si ya buscó "mo", para buscar "mou" solo baja un nodo más, no reinicia la búsqueda desde cero.
2. La implementación guarda los top 3 resultados directamente en los nodos durante la inserción, al momento de buscar, la extracción de las sugerencias es instantánea O(1) por carácter tecleado. El tiempo de consulta se reduce a $O(L)$ donde L es la longitud de `searchWord`, siendo esta la forma más rápida teóricamente posible de responder a la consulta en tiempo real.

## Conclusiones
El trie cumple con el objetivo para el que fue creado es rápido sin importar el tamaño del diccionario. Las operaciones de inserción, búsqueda, búsqueda por prefijo y eliminación cuestan O(|s|), es decir, dependen solo de la longitud de la cadena procesada y no de cuántas palabras haya almacenadas. En la demostración se vio con claridad, para cada letra escrita, el programa avanzó un solo paso en el árbol sin volver a revisar la lista completa de productos.

Compartir prefijos es lo que hace eficiente al trie. Como las palabras que empiezan igual comparten los mismos nodos), cada prefijo común se guarda una sola vez. Así se ahorra espacio y se facilita buscar todo lo que empieza con un mismo comienzo.

La estructura interna es sencilla, pero cada decisión de diseño tiene su costo. Un nodo solo necesita saber quiénes son sus hijos y si ahí termina una palabra. Elegir entre un arreglo de tamaño fijo o una tabla hash (diccionario) para los hijos cambia el equilibrio entre velocidad y memoria. En nuestra implementación se usó un diccionario de Python, porque guarda solo los hijos que existen y no depende del tamaño del alfabeto.

Se comprobó su utilidad en un caso real de autocompletado. Al resolver Leetcode, el trie devolvió las sugerencias correctas letra por letra, respetó el límite de 3 resultados y dejó listas vacías cuando el prefijo dejó de existir. Esto muestra cómo funcionan en la práctica las barras de búsqueda que sugieren mientras escribimos.

El trie no es la solución para todo. Gasta bastante memoria si hay muchas palabras largas con poco en común, y no ayuda si solo se necesita saber si una clave existe exactamente. Para esos casos existen versiones comprimidas como PATRICIA, o estructuras como la tabla hash. Elegir bien depende del problema, el trie funciona especialmente  cuando las claves son secuencias y se necesitan operaciones por prefijo. 

Es una idea con más de seis décadas que sigue vigente. Nació en 1959 para resolver el problema de buscar rápido con computadoras lentas y de poca memoria, y hoy está, directa o mediante sus variantes, en el autocompletado, los correctores ortográficos, el enrutamiento de internet, el DNS y los buscadores de texto. 

En resumen, se alcanzó el objetivo planteado, se explicó cómo funciona el trie, cómo está construido y cuál es su complejidad, y se demostró su eficiencia en un problema de procesamiento de cadenas y autocompletado. 
## Referencias 

- 5.2 Tries, Algorithms 4th Edition, Sedgewick y Wayne - Ayudó a comprender cómo se guardan los hijos de un nodo con un arreglo y cómo funciona la eliminación, ya sea quitando la marca de fin de palabra o borrando los nodos que sobran. https://algs4.cs.princeton.edu/52trie
  
- Árboles lexicográficos (o tries), Lección 17, Estructuras de Datos y Algoritmos, Universidad de Zaragoza -Ayudó a comprender el concepto de árbol de prefijos, las formas de implementarlo. https://webdiis.unizar.es/asignaturas/EDA/curso_26-27/lecciones/leccion_17.pdf 

- Árboles trie en informática estructura y uso. - Ayudo a tener el conocimiento de por que nacio el Trie y quien lo invento. https://www.ai-futureschool.com/es/informatica/introduccion-a-los-arboles-trie-en-informatica.php

- data-structures: Trie (árbol de prefijo / árbol de radix)- Ayudo a obtener ejemplos visuales de como funciona el Trie y como se implementa en codigo. https://learntutorials.net/es/data-structures/topic/7178/trie--arbol-de-prefijo---arbol-de-radix-

- Implementing Patricia Trie in Java. Sirvio para conocer a Patricia, una de las variantes de los Tries. https://www.geeksforgeeks.org/java/implementing-patricia-trie-in-java/

- Prefijo. - Ayudo a conocer la definición de la palabra prefijo. https://etimologias.dechile.net/?prefijo
  
- Trie: la estructura de datos detras del autocompletado - Ayudó a comprender la definición formal del trie, su comparación con árboles binarios de búsqueda y tablas hash, y sus aplicaciones en diccionarios y corrección ortográfica. https://elsolitario.org/2026/08/17/trie-arbol-prefijos-autocompletado/

- Tries- Ayudo a comprender de forma mas compacta el Trie y a comprender mejor su funcionamiento, a saber la complejidad y también a conocer mejor cuando usarlo.https://aprende.olimpiada-informatica.org/algoritmia-tries
  
- trie (data structure), Dictionary of Algorithms and Data Structures, NIST - Ayudó a confirmar la definición del trie, donde cada prefijo común se guarda una sola vez. https://www.nist.gov/dads/HTML/trie.html

- Time complexity of operations on built-in types, Python documentation - Ayudó a conocer que el acceso a un diccionario cuesta O(1) en promedio, que es lo que se usa para guardar los hijos con una tabla hash. https://docs.python.org/3/library/time-complexity.html
  
- Trie memory, Edward Fredkin, Communications of the ACM, 1960 - Ayudó a conocer el origen del trie y quién lo propuso. https://doi.org/10.1145/367390.367400

- Trie (Prefix Tree), CPCFI Academic Team, Facultad de Ingeniería, UNAM, 2025. Diapositivas del equipo de programación competitiva CPCFI, sin enlace público - Ayudó a comprender la definición del trie, su vista como autómata con aristas y estados, las operaciones de inserción, búsqueda y eliminación, y la complejidad en tiempo y espacio.

- CPCFI: Strings (UNAM) - Trie (Prefix Tree), CPCFI Academic Team, Facultad de Ingeniería, UNAM (21 de octubre de 2025) [Presentación en PDF] - Ayudó a comprender la implementación del Trie en C++ mediante arreglos de punteros y bandera de fin de palabra, el cálculo de complejidad espacial/temporal y las operaciones de inserción, búsqueda y eliminación.

