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

## Demostración (Ejemplos de resultados)
Primero formaremos un trie sencillo (sin code), con las letras del abecedario inglés $\sum $ {a,b,c,...,y,z}.
Lo formaremos con las siguientes palabras: [can,monkey,tree,cat,money,pencil,penny]

<img src="./media/Trie_1.png" alt="Alt Text" width="350" height="400">

Podemos ver que por cada nodo, guardaremos a lo mas $|\sum|$ hijos. Entonces en el peor caso la complejidad espacial de un Trie es de $O(N \cdot M \cdot |\sum|)$. Donde $N$ es el número de elementos que hay en el trie y $M$ es la longitud máxima de un string.

Usualmente cuando se use un Trie, $|\sum|$ ya esta definido, por lo que su tamaño es constante, en estos casos tenemos una complejidad de $O(N \cdot M)$


Por último para hacer una demostración resolveremos el problema Leetcode 1268 - Suggestions System :)
<!-- CREO QUE ESTO DE ACA (ANALISIS DE COMPLEJIDADES QUEDARIA MEJOR EN LA PARTE DE ANALISIS DE RESULTADOS)
**Complejidad temporal:** 
- Ordenamiento inicial:$O(N \ log \ N \cdot L)$. N es el número de productos y L su longitud promedio.
- Construir el Trie: $O(S)$. S es la suma total de caracteres de todos los productos
- Búsqueda de sugerencias: $O(M)$. M es la longitud de `searchWord`.  
**Complejidad espacial:** $O(S). Para almacenar los nodos del Trie. Guardar referencias a las cadenas en suggestions no duplica los strings en memoria en Python, solo guarda sus punteros.$



-->


## Análisis de resultados
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

## Conclusiones

## Referencias 
