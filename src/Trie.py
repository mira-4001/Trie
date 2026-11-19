class Trie:
    def __init__(self): # constructor
        # Inicializa el nodo raíz como un diccionario vacío
        self.root = {}

    def insert(self, word):
        # Empieza desde la raíz para insertar cada letra de la palabra
        node = self.root 
        for char in word:
            # Si la letra no existe en el nivel actual, crea un nuevo nodo
            if char not in  node:
                node[char] = {}
            # Avanza al siguiente nodo
            node = node[char]
        # Marca el final de la palabra
        node["#"] = True  

    def search(self, word):
        # Recorre el árbol letra por letra buscando la palabra completa
        node = self.root
        for char in word:
            # Si falta una letra, la palabra no existe
            if char not in node:
                return False
            node = node[char]
        # Confirma que exista la marca de fin de palabra
        return "#" in node

    def starts_with(self, prefix):
        # Verifica si existe al menos una palabra con el prefijo dado
        node = self.root
        for char in prefix:
            # Si se rompe la secuencia de letras, no existe el prefijo
            if char not in node:
                return False
            node = node[char]
        # Devuelve True si se recorrió todo el prefijo sin problemas
        return True

    def remove(self, word):
        # Función auxiliar recursiva para borrar la palabra y limpiar nodos vacíos
        def _delete(node, i):
            # Caso base: se llegó al final de la palabra
            if i == len(word):
                # Si no está marcada como palabra, no hay nada que borrar
                if "#" not in node:
                    return False
                # Elimina la marca de fin de palabra
                del node["#"]
                # Devuelve True si el nodo quedó vacío y puede eliminarse
                return len(node) == 0

            char = word[i]
            # Si la letra no existe, la palabra no está en el Trie
            if char not in node:
                return False

            # Avanza recursivamente y elimina el nodo hijo si quedó vacío
            if _delete(node[char], i + 1):
                del node[char]
                return len(node) == 0
            return False

        # Inicia el proceso de eliminación desde la raíz en el índice 0
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