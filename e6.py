class NodoB:
    def __init__(self, hoja=True):
        self.claves = []
        self.hijos = []
        self.hoja = hoja

    def insertar(self, clave):
        if self.hoja:
            self.claves.append(clave)
            self.claves.sort()
        else:
            i = 0
            while i < len(self.claves) and clave > self.claves[i]:
                i += 1
            self.hijos[i].insertar(clave)
            if len(self.hijos[i].claves) > 2:
                self.dividir_hijo(i)

    def dividir_hijo(self, i):
        nuevo_nodo = NodoB(hoja=self.hijos[i].hoja)
        medio = self.hijos[i].claves.pop(1)
        if not self.hijos[i].hoja:
            nuevo_nodo.hijos = self.hijos[i].hijos[2:]
            self.hijos[i].hijos = self.hijos[i].hijos[:2]
        self.claves.insert(i, medio)
        self.hijos.insert(i + 1, nuevo_nodo)

    def eliminar(self, clave):
        if clave in self.claves:
            index = self.claves.index(clave)
            if self.hoja:
                self.claves.remove(clave)
            else:
                self.hijos[index].eliminar(clave)
                if len(self.hijos[index].claves) < 1:
                    self.fusionar_hijo(index)
        else:
            i = 0
            while i < len(self.claves) and clave > self.claves[i]:
                i += 1
            if i < len(self.claves):
                self.hijos[i].eliminar(clave)
                if len(self.hijos[i].claves) < 1:
                    self.fusionar_hijo(i)

    def fusionar_hijo(self, i):
        hijo_actual = self.hijos[i]
        if i > 0:
            hermano_izquierdo = self.hijos[i - 1]
            hermano_izquierdo.claves.append(self.claves.pop(i - 1))
            hermano_izquierdo.claves += hijo_actual.claves
            hermano_izquierdo.hijos += hijo_actual.hijos
            self.hijos.pop(i)
        else:
            hermano_derecho = self.hijos[i + 1]
            hermano_derecho.claves.insert(0, self.claves.pop(i))
            hermano_derecho.claves = hijo_actual.claves + hermano_derecho.claves
            hermano_derecho.hijos = hijo_actual.hijos + hermano_derecho.hijos
            self.hijos.pop(i)
    
    def mostrar(self, nivel=0):
        print("Nivel", nivel, ":", str(self.claves))
        nivel += 1
        if len(self.hijos) > 0:
            for i in range(len(self.hijos)):
                self.hijos[i].mostrar(nivel)


class ArbolB:
    def __init__(self):
        self.raiz = None

    def insertar(self, clave):
        if self.raiz is None:
            self.raiz = NodoB()
        self.raiz.insertar(clave)
        if len(self.raiz.claves) > 2:
            nueva_raiz = NodoB(hoja=False)
            nueva_raiz.hijos.append(self.raiz)
            nueva_raiz.dividir_hijo(0)
            self.raiz = nueva_raiz

    def eliminar(self, clave):
        if self.raiz:
            self.raiz.eliminar(clave)
            if len(self.raiz.claves) == 0:
                if self.raiz.hoja:
                    self.raiz = None
                else:
                    self.raiz = self.raiz.hijos[0]

    def mostrar(self):
        if self.raiz:
            self.raiz.mostrar()


# Crear un árbol B de orden 2
arbol = ArbolB()

# Insertar los valores dados
valores = [10, 25, 7, 30, 8, 15, 40, 5, 42, 20, 32]
for valor in valores:
    arbol.insertar(valor)

# Mostrar el árbol B
arbol.mostrar()

# Eliminar un valor (por ejemplo, 15)
valor_a_eliminar = 15
arbol.eliminar(valor_a_eliminar)

# Mostrar el árbol B después de la eliminación
arbol.mostrar()
