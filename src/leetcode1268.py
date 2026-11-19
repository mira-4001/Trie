class TrieNode:
    def __init__(self):
        # Diccionario para guardar los nodos hijos (siguiente letra)
        self.children = {}
        # Lista para guardar hasta 3 palabras sugeridas que pasan por este nodo
        self.suggestion = []

class Trie:
    def __init__(self):
        # Inicializa el nodo raíz del Trie
        self.root = TrieNode()

    def insert(self,word):
        # Empieza desde la raíz para insertar la palabra
        node = self.root
        for char in word:
            # Si la letra no existe como hijo, crea un nuevo nodo
            if char not in node.children:
                node.children[char] = TrieNode()
            # Avanza al nodo de la letra actual
            node = node.children[char]
            # Si el nodo aún tiene menos de 3 sugerencias, guarda la palabra
            if len(node.suggestion) < 3:
                node.suggestion.append(word)

    def get_suggestion(self,prefix):
        # Lista donde se guardarán las sugerencias por cada letra escrita
        res = []
        node = self.root
        for char in prefix:
            # Si seguimos dentro de un camino válido y existe la letra, avanza y guarda sugerencias
            if node and char in node.children:
                node = node.children[char]
                res.append(node.suggestion)
            else:
                # Si se pierde el camino, marca el nodo como None y agrega lista vacía
                node = None
                res.append([])
        # Devuelve las sugerencias acumuladas para cada prefijo
        return res


class Solution:
    def suggestedProducts(self, products: list[str], searchWord: str) -> list[list[str]]:
        # Ordena los productos alfabéticamente para insertar siempre los mejores 3 primero
        products.sort()

        # Crea el Trie
        trie = Trie()

        # Inserta cada producto en el Trie
        for product in products:
            trie.insert(product)
        # Busca y retorna las sugerencias letra por letra de searchWord
        return trie.get_suggestion(searchWord)