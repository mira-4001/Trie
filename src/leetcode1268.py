from typing import List
class TrieNode:
    def __init__(self) -> None:
        self.children: dict[str, TrieNode] = {}
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
            
            if len(node.suggestions) < 3:
                node.suggestions.append(word)

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


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        
        trie = Trie()
        for product in products:
            trie.insert(product)
            
        return trie.get_suggestions(searchWord)