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
### Actualidad 

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
