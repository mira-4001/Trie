from typing import List


class TrieNode:
    def __init__(self) -> None:
        self.children: dict[str, TrieNode] = {}
        # Guardamos hasta 3 sugerencias directo en cada nodo para no recorrer después
        self.suggestions: list[str] = []


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            
            # Como ya ordenamos los productos, los primeros 3 que pasen por aquí son los mejores
            if len(node.suggestions) < 3:
                node.suggestions.append(word)

    def get_suggestions(self, prefix: str) -> List[List[str]]:
        result: List[List[str]] = []
        node: TrieNode | None = self.root
        
        for char in prefix:
            # Si seguimos dentro del árbol y existe la letra, bajamos y tomamos sus sugerencias
            if node and char in node.children:
                node = node.children[char]
                result.append(node.suggestions)
            else:
                # Si se rompe la coincidencia, el resto de letras ya no tendrá resultados
                node = None
                result.append([])
                
        return result


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        # Ordenamos alfabéticamente para cumplir con el orden lexicográfico
        products.sort()
        
        trie = Trie()
        for product in products:
            trie.insert(product)
            
        return trie.get_suggestions(searchWord)