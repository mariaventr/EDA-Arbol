
class Nodo:
    __dato=int
    __izq=None
    __der=None
    def __init__(self, dato):
        self.__dato = dato
        self.__izq = None
        self.__der = None

    def getValor(self):
        return self.__dato
    
    def getIzq(self):
        return self.__izq
    
    def getDer(self):
        return self.__der
    
    def setIzq(self, objeto):
        self.__izq=objeto

    def setDer(self, objeto):
        self.__der=objeto

    def setValor(self, objeto):
        self.__dato=objeto
    
class arbol:
    __cabeza=None
    def __init__(self):
        self.__cabeza=None

    def getCabeza(self):
        return self.__cabeza

    def insertar(self, objeto):
        if self.__cabeza is None:
            nodo=Nodo(objeto)
            self.__cabeza=nodo
        else:
            self.insertarRecursion(self.__cabeza, objeto)

    def insertarRecursion(self, cab, objeto):
        if cab.getValor()==objeto:
            print("Elemento ya existente")
        else:
            if objeto < cab.getValor():
                if cab.getIzq() is None:
                    nodo=Nodo(objeto)
                    cab.setIzq(nodo)
                else:
                    self.insertarRecursion(cab.getIzq(), objeto)
            else:
                if objeto > cab.getValor():
                    if cab.getDer() is None:
                        nodo=Nodo(objeto)
                        cab.setDer(nodo)
                    else:
                        self.insertarRecursion(cab.getDer(), objeto)

    def suprimir(self, valor):
        if self.__cabeza is None:
            print("El árbol está vacío. No se puede eliminar el elemento.")
        else:
            self.__cabeza = self.suprimirRecursion(self.__cabeza, valor)

    def suprimirRecursion(self, nodo, valor):
        if nodo is None:
            print(f"El elemento {valor} no existe en el árbol.")
        else:
            if valor < nodo.getValor():
                nodo.setIzq(self.suprimirRecursion(nodo.getIzq(), valor))
            elif valor > nodo.getValor():
                nodo.setDer(self.suprimirRecursion(nodo.getDer(), valor))
            else:
                if nodo.getIzq() is None and nodo.getDer() is None:
                    nodo = None
                elif nodo.getIzq() is None:
                    nodo = nodo.getDer()
                elif nodo.getDer() is None:
                    nodo = nodo.getIzq()
                else:
                    max_izquierdo = self.maximo(nodo.getIzq())
                    nodo.setValor(max_izquierdo.getValor())
                    nodo.setIzq(self.suprimirRecursion(nodo.getIzq(), max_izquierdo.getValor()))
        return nodo

    def maximo(self, nodo):
        while nodo.getDer() is not None:
            nodo = nodo.getDer()
        return nodo

    def Hoja(self, nodo, valor):
        if nodo is None:
            return False
        if nodo.getValor() == valor and nodo.getIzq() is None and nodo.getDer() is None:
            return True
        return self.Hoja(nodo.getIzq(), valor) or self.Hoja(nodo.getDer(), valor)

    def Nivel(self, nodo, valor, nivel_actual):
        if nodo is None:
            return -1  # Valor no encontrado
        if nodo.getValor() == valor:
            return nivel_actual
        nivel_izq = self.Nivel(nodo.getIzq(), valor, nivel_actual + 1)
        if nivel_izq != -1:
            return nivel_izq
        nivel_der = self.Nivel(nodo.getDer(), valor, nivel_actual + 1)
        return nivel_der

    def Hijo(self, nodo, padre_valor, hijo_valor):
        if nodo is None:
            return False
        if nodo.getValor() == padre_valor:
            if nodo.getIzq() and nodo.getIzq().getValor() == hijo_valor:
                return True
            if nodo.getDer() and nodo.getDer().getValor() == hijo_valor:
                return True
        return self.Hijo(nodo.getIzq(), padre_valor, hijo_valor) or self.Hijo(nodo.getDer(), padre_valor, hijo_valor)

    def Padre(self, nodo, padre, hijo_valor):
        if nodo is None:
            return None  # Valor no encontrado
        if nodo.getValor() == hijo_valor:
            return padre.getValor() if padre else None
        izquierda = self.Padre(nodo.getIzq(), nodo, hijo_valor)
        if izquierda:
            return izquierda
        derecha = self.Padre(nodo.getDer(), nodo, hijo_valor)
        return derecha


    def Camino(self, inicio_valor, final_valor):
        camino = self.encontrarCamino(self.__cabeza, [], inicio_valor, final_valor)
        if camino:
            return camino

    def encontrarCamino(self, nodo, camino_actual, inicio_valor, final_valor):
        if nodo is None:
            return None
        camino_actual.append(nodo.getValor())
        if nodo.getValor() == final_valor:
            return camino_actual
        izquierda = self.encontrarCamino(nodo.getIzq(), camino_actual.copy(), inicio_valor, final_valor)
        if izquierda:
            return izquierda
        derecha = self.encontrarCamino(nodo.getDer(), camino_actual.copy(), inicio_valor, final_valor)
        return derecha

    def Altura(self, nodo):
        if nodo is None:
            return 0
        izquierda = self.Altura(nodo.getIzq())
        derecha = self.Altura(nodo.getDer())
        return max(izquierda, derecha) + 1
    
    def InOrden(self, nodo):
        if nodo:
            self.InOrden(nodo.getIzq())
            print(nodo.getValor())
            self.InOrden(nodo.getDer())

    def preOrdenRecursion(self, nodo):
        if nodo:
            print(nodo.getValor())  # Imprimir el valor del nodo en lugar de agregarlo a la lista
            self.preOrdenRecursion(nodo.getIzq())
            self.preOrdenRecursion(nodo.getDer())


    def postOrdenRecursion(self, nodo):
        if nodo:
            resultado = []
            resultado += self.postOrdenRecursion(nodo.getIzq())
            resultado += self.postOrdenRecursion(nodo.getDer())
            resultado.append(nodo.getValor())
            return resultado
        return []


    def buscarRecursion(self, nodo, valor):
        if nodo is None:
            return "Error - Elemento Inexistente"
        if nodo.getValor() == valor:
            return "Éxito - Elemento existente"
        elif valor < nodo.getValor():
            return self.buscarRecursion(nodo.getIzq(), valor)
        else:
            return self.buscarRecursion(nodo.getDer(), valor)
            
                    
if __name__=="__main__":
    a=arbol()
    print(a.getCabeza())
    a.insertar(1)
    a.insertar(3)
    a.insertar(10)
    a.insertar(40)
    a.insertar(20)
    print(f"Despues de insertar: ")
    a.InOrden(a.getCabeza())
    a.suprimir(1)
    print(f"Despues de Suprmir:")
    a.InOrden(a.getCabeza())

    print(f"Hoja: {a.Hoja(a.getCabeza(), 3)}")
    print(f"Padre: {a.Padre(a.getCabeza(),None, 4)}")
    print(f"Camino: {a.Camino(0, 10)}")
    print(f"Altura: {a.Altura(a.getCabeza())}")
    print(f"Buscar 1: {a.buscarRecursion(a.getCabeza(),1)}")

    print("PreOrden")
    a.preOrdenRecursion(a.getCabeza())

    print("PostOrden")
    print(a.postOrdenRecursion(a.getCabeza()))

