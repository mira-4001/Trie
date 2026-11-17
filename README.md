# Trie
## Integrantes
1. [426061748] [Hernandez Lopez Alejandro]
2. [323038320] [Hernandez Soria Miriam]
3. [Num cuenta ] [Nombre]
4. [Num cuenta ] [Nombre]
   
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

## Conclusiones

## Referencias 
