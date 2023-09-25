class Nodo:
    def __init__(self, key):
        self.key = key
        self.con = 1
        self.bal = 0
        self.izq = None
        self.der = None


class Arbol:
    def __init__(self):
        self.raiz = None

    def insertar(self, x):
        h = [0]
        print(self.raiz)
        self.raiz = self._insertar(self.raiz, x, h)

    def _insertar(self, p, x, h):
        if p is None:
            h[0] = 1
            print(h)
            return Nodo(x)
        
        if x < p.key:
            p.izq = self._insertar(p.izq, x, h)
            if h[0]:
                if p.bal == 1:
                    p.bal = 0
                    h[0] = 0
                elif p.bal == 0:
                    p.bal = -1
                elif p.bal == -1:
                    p = self._balancear_izquierda(p)
        elif x > p.key:
            p.der = self._insertar(p.der, x, h)
            if h[0]:
                if p.bal == -1:
                    p.bal = 0
                    h[0] = 0
                elif p.bal == 0:
                    p.bal = 1
                elif p.bal == 1:
                    p = self._balancear_derecha(p)
        else:
            p.con += 1
        
        return p

    def _balancear_izquierda(self, p):
        p1 = p.izq
        if p1.bal == -1:
            p.izq = p1.der
            p1.der = p
            p.bal = 0
            p = p1
        else:
            p2 = p1.der
            p1.der = p2.izq
            p2.izq = p1
            p.izq = p2.der
            p2.der = p
            if p2.bal == -1:
                p.bal = 1
            else:
                p.bal = 0
            if p2.bal == 1:
                p1.bal = -1
            else:
                p1.bal = 0
            p = p2
        p.bal = 0
        return p

    def _balancear_derecha(self, p):
        p1 = p.der
        if p1.bal == 1:
            p.der = p1.izq
            p1.izq = p
            p.bal = 0
            p = p1
        else:
            p2 = p1.izq
            p1.izq = p2.der
            p2.der = p1
            p.der = p2.izq
            p2.izq = p
            if p2.bal == 1:
                p.bal = -1
            else:
                p.bal = 0
            if p2.bal == -1:
                p1.bal = 1
            else:
                p1.bal = 0
            p = p2
        p.bal = 0
        return p

    def suprimir(self, x):
        h = [0]
        self.raiz = self._suprimir(self.raiz, x, h)

    def _suprimir(self, p, x, h):
        if p is None:
            print("\nLa llave no está en el árbol")
            return None
        
        if x < p.key:
            p.izq = self._suprimir(p.izq, x, h)
            if h[0]:
                p = self._balancear_derecha(p)
        elif x > p.key:
            p.der = self._suprimir(p.der, x, h)
            if h[0]:
                p = self._balancear_izquierda(p)
        else:
            if p.con > 1:
                p.con -= 1
            else:
                if p.der is None:
                    return p.izq
                if p.izq is None:
                    return p.der
                c = self._encontrar_min(p.der)
                p.key = c.key
                p.con = c.con
                p.der = self._suprimir(p.der, c.key, h)
                if h[0]:
                    p = self._balancear_izquierda(p)
        return p

    def _encontrar_min(self, p):
        while p.izq is not None:
            p = p.izq
        return p

    def mostrar(self):
        print("\nÁrbol AVL:")
        self._mostrar(self.raiz)

    def _mostrar(self, p):
        if p is not None:
            print(f"Clave: {p.key}, Repeticiones: {p.con}")
            print("Izquierda:")
            self._mostrar(p.izq)
            print("Derecha:")
            self._mostrar(p.der)


if __name__ == "__main__":
    arbol = Arbol()
    op = 0
    while op != 4:
        print("\n\nMenú\n")
        print("1_ Insertar")
        print("2_ Suprimir")
        print("3_ Mostrar")
        print("4_ Salir")
        op = int(input("Ingrese opción: "))
        if op == 1:
            ele = int(input("Ingrese elemento a insertar, el ingreso finaliza con 0: "))
            while ele != 0:
                arbol.insertar(ele)
                print(f"Elemento {ele} insertado en el árbol.")
                ele = int(input("Ingrese elemento a insertar, el ingreso finaliza con 0: "))
        elif op == 2:
            ele = int(input("Ingrese elemento a suprimir, el ingreso finaliza con 0: "))
            while ele != 0:
                arbol.suprimir(ele)
                print(f"Elemento {ele} suprimido del árbol.")
                ele = int(input("Ingrese elemento a suprimir, el ingreso finaliza con 0: "))
        elif op == 3:
            arbol.mostrar()
