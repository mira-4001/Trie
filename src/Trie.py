class Trie:
    def __init__(self): # constructor
        self.root = {}

    def insert(self, word):
        node = self.root 
        for char in word:
            if char not in  node:
                node[char] = {}
            node = node[char]
        node["#"] = True  

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node:
                return False
            node = node[char]
        return "#" in node

    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node:
                return False
            node = node[char]
        return True

    def remove(self, word):
        def _delete(node, i):
            if i == len(word):
                if "#" not in node:
                    return False
                del node["#"]
                return len(node) == 0

            char = word[i]
            if char not in node:
                return False

            if _delete(node[char], i + 1):
                del node[char]
                return len(node) == 0
            return False

        _delete(self.root, 0)


# Ejemplo rápido
t = Trie()
t.insert("algoritmo")
t.insert("alga")

print(t.search("algoritmo"))   # True
print(t.search("algo"))        # False
print(t.starts_with("algo"))   # True

t.remove("algoritmo")
print(t.search("algoritmo"))   # False
print(t.search("alga"))        # True