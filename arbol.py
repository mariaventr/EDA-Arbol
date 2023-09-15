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
            self.recursion(self.__cabeza, objeto)

    def recursion(self, cab, objeto):
        if cab.getValor()==objeto:
            print("Elemento ya existente")
        else:
            if objeto < cab.getValor():
                if cab.getIzq() is None:
                    nodo=Nodo(objeto)
                    cab.setIzq(nodo)
                else:
                    self.recursion(cab.getIzq(), objeto)
            else:
                if objeto > cab.getValor():
                    if cab.getDer() is None:
                        nodo=Nodo(objeto)
                        cab.setDer(nodo)
                    else:
                        self.recursion(cab.getDer(), objeto)

    def recorrer(self, nodo):
        if nodo:
            self.recorrer(nodo.getIzq())
            print(nodo.getValor())
            self.recorrer(nodo.getDer())



                    
if __name__=="__main__":
    a=arbol()
    a.insertar(1)
    a.insertar(3)
    a.insertar(2)
    a.insertar(1)
    a.insertar(10)
    a.insertar(4)
    nodo=a.getCabeza()
    a.recorrer(nodo)
