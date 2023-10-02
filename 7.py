class Paciente:
    __nombre=str
    __apellido=str
    __edad=int
    def __init__(self, nombre, apellido, edad):
        self.__nombre=nombre
        self.__apellido=apellido
        self.__edad=edad

    def getNombre(self):
        return self.__nombre
    
    def getApellido(self):
        return self.__apellido
    
    def getEdad(self):
        return self.__edad

class Nodo:
    __dato=int
    __paciente=object
    __izq=None
    __der=None
    def __init__(self, dato, paciente):
        self.__paciente=paciente
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

    def insertar(self, objeto, p):
        if self.__cabeza is None:
            nodo=Nodo(objeto, p)
            self.__cabeza=nodo
        else:
            self.insertarRecursion(self.__cabeza, objeto, p)

    def insertarRecursion(self, cab, objeto, p):
        if cab.getValor()==objeto:
            print("Elemento ya existente")
        else:
            if objeto < cab.getValor():
                if cab.getIzq() is None:
                    nodo=Nodo(objeto, p)
                    cab.setIzq(nodo)
                else:
                    self.insertarRecursion(cab.getIzq(), objeto, p)
            else:
                if objeto > cab.getValor():
                    if cab.getDer() is None:
                        nodo=Nodo(objeto, p)
                        cab.setDer(nodo)
                    else:
                        self.insertarRecursion(cab.getDer(), objeto, p)

    def Padre_Hermano(self, valor):
        if self.__cabeza is None:
            print("El árbol está vacío.")
            return
        else:
            if self.__cabeza.getValor() == valor:
                print(f"{valor}: Es la raiz del arbol, no posee padre ni hermano")
                return
            
        padre, hermano = self._encontrar_padre_hermano(self.__cabeza, None, valor)
        print(padre, hermano)
        
        if padre is not None:
            print(f"Padre de {valor}: {padre.getValor()}")
            if hermano is not None:
                print(f"Hermano de {valor}: {hermano.getValor()}")
            else:
                print(f"No hay hermano de {valor}.")
        else:
            print(f"No se encontró el nodo {valor} en el árbol.")

    def _encontrar_padre_hermano(self, nodo, padre, valor):
        if nodo is None:
            return None, None
        if nodo.getIzq() and nodo.getIzq().getValor() == valor:
            hermano = nodo.getDer() if nodo.getDer() else None
            padre = nodo
            return padre, hermano
        if nodo.getDer() and nodo.getDer().getValor() == valor:
            hermano = nodo.getIzq() if nodo.getIzq() else None
            padre = nodo
            return padre, hermano
        
        izquierda_padre, izquierda_hermano = self._encontrar_padre_hermano(nodo.getIzq(), nodo, valor)
        if izquierda_padre is not None:
            return izquierda_padre, izquierda_hermano
        
        derecha_padre, derecha_hermano = self._encontrar_padre_hermano(nodo.getDer(), nodo, valor)
        if derecha_padre is not None:
            return derecha_padre, derecha_hermano
        
        return None, None
    
    def contar_nodos_recursivo(self, nodo):
        if nodo is None:
            return 0
        return 1 + self.contar_nodos_recursivo(nodo.getIzq()) + self.contar_nodos_recursivo(nodo.getDer())

    def contar_nodos(self):
        return self.contar_nodos_recursivo(self.__cabeza)
    
    def Altura(self, nodo):
        if nodo is None:
            return 0
        izquierda = self.Altura(nodo.getIzq())
        derecha = self.Altura(nodo.getDer())
        return max(izquierda, derecha) + 1
    
    def sucesores(self, valor):
        nodo = self.buscarRecursion(self.__cabeza, valor)
        if nodo:
            sucesores = []
            self._encontrar_sucesores(nodo, sucesores,valor)
            return sucesores
    

    def _encontrar_sucesores(self, nodo, sucesores,valor):
        if nodo:
            if nodo.getValor() != valor:
                sucesores.append(nodo.getValor()) 
            self._encontrar_sucesores(nodo.getIzq(), sucesores, valor)
            self._encontrar_sucesores(nodo.getDer(), sucesores, valor)

    def buscarRecursion(self, nodo, valor):
        if nodo is None:
            return None
        if nodo.getValor() == valor:
            return nodo
        if valor < nodo.getValor():
            return self.buscarRecursion(nodo.getIzq(), valor)
        else:
            return self.buscarRecursion(nodo.getDer(), valor)
        
    def InOrden(self, nodo):
        if nodo:
            self.InOrden(nodo.getIzq())
            print(nodo.getValor())
            self.InOrden(nodo.getDer())


if __name__=="__main__":
    mi_arbol = arbol()
    p1=Paciente("miguel", "anguel", 20)
    p2=Paciente("miguel", "anguel", 30)
    p3=Paciente("miguel", "anguel", 10)
    p4=Paciente("miguel", "anguel", 15)
    p5=Paciente("miguel", "anguel", 80)
    p6=Paciente("miguel", "anguel", 2)
    p7=Paciente("miguel", "anguel", 54)

    mi_arbol.insertar(10, p1)
    mi_arbol.insertar(5, p2)
    mi_arbol.insertar(15, p3)
    mi_arbol.insertar(3, p4)
    mi_arbol.insertar(7, p5)
    mi_arbol.insertar(12, p6)
    mi_arbol.insertar(18, p7)
    mi_arbol.InOrden(mi_arbol.getCabeza())


    # Mostrar el nodo padre y hermano de un nodo (ejemplo con nodo 12):
    mi_arbol.Padre_Hermano(18)

    # Mostrar la cantidad de nodos del árbol:
    print("Cantidad de nodos:", mi_arbol.contar_nodos())

    # Mostrar la altura del árbol:
    print("Altura del árbol:", mi_arbol.Altura(mi_arbol.getCabeza()))

    # Mostrar los sucesores de un nodo (ejemplo con nodo 10):
    print("Sucesores de 10:", mi_arbol.sucesores(2))




