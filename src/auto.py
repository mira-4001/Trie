class Nodo:
    def __init__(self):
        # Diccionario para guardar las letras siguientes (letra: Nodo)
        self.hijos = {}
        # Marca si aquí termina una palabra completa
        self.fin = False


class Trie:
    def __init__(self):
        self.raiz = Nodo()

    def insertar(self, palabra):
        actual = self.raiz
        for letra in palabra:
            # Si la letra no existe en este nivel, creamos un nodo nuevo
            if letra not in actual.hijos:
                actual.hijos[letra] = Nodo()
            actual = actual.hijos[letra]
        # Marcamos el último nodo como el final de la palabra
        actual.fin = True

    def autocompletar(self, prefijo):
        actual = self.raiz
        # Primero navegamos hasta el final del prefijo
        for letra in prefijo:
            if letra not in actual.hijos:
                return []  # No hay coincidencias
            actual = actual.hijos[letra]

        # Desde ese nodo, recolectamos todas las palabras posibles
        resultados = []
        self._buscar_ramas(actual, prefijo, resultados)
        return resultados

    def _buscar_ramas(self, nodo, palabra_actual, resultados):
        # Si es fin de palabra, la guardamos en la lista
        if nodo.fin:
            resultados.append(palabra_actual)
        
        # Recorremos recursivamente todas las letras hijas
        for letra, hijo in nodo.hijos.items():
            self._buscar_ramas(hijo, palabra_actual + letra, resultados)


# --- Pruebas ---
trie = Trie()
for p in ["casa", "casero", "caso", "castillo", "perro"]:
    trie.insertar(p)

print(trie.autocompletar("cas"))   # ['casa', 'casero', 'caso', 'castillo']
print(trie.autocompletar("caso"))  # ['caso']
print(trie.autocompletar("per"))   # ['perro']