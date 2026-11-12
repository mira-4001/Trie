# Trie
## Integrantes
1. [426061748] [Hernandez Lopez Alejandro]
2. [Num cuenta ] [Nombre]
3. [Num cuenta ] [Nombre]
4. [Num cuenta ] [Nombre]
   
## Objetivo 
Analizar el funcionamiento, la estructura interna y la complejidad del Trie, implementando sus operaciones  (inserción, búsqueda,eliminación y búsqueda por prefijo) para demostrar su eficiencia y como lo podemos aplicar en la resolución de problemas de procesamiento de cadenas y autocompletado.
## Concepto 

## Contexto 
### Antecedentes 
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
