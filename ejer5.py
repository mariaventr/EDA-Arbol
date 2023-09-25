class Nodo:
    def __init__(self, key):
        self.key = key
        self.con = 1
        self.bal = 0
        self.izq = None
        self.der = None


def insertar(p, x, h):
    if p is None:
        h[0] = 1
        return Nodo(x)
    
    if x < p.key:
        p.izq = insertar(p.izq, x, h)
        print(h[0])
        if h[0]:
            print(1)
            if p.bal == 1:
                p.bal = 0
                h[0] = 0
            elif p.bal == 0:
                p.bal = -1
            elif p.bal == -1:
                p = balancear_izquierda(p)
    elif x > p.key:
        p.der = insertar(p.der, x, h)
        if h[0]:
            if p.bal == -1:
                p.bal = 0
                h[0] = 0
            elif p.bal == 0:
                p.bal = 1
            elif p.bal == 1:
                p = balancear_derecha(p)
    else:
        p.con += 1
    
    return p


def balancear_izquierda(p):
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


def balancear_derecha(p):
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


def suprimir(p, x, h):
    if p is None:
        print("\nLa llave no está en el árbol")
        return None
    
    if x < p.key:
        p.izq = suprimir(p.izq, x, h)
        if h[0]:
            p = balancear_derecha(p)
    elif x > p.key:
        p.der = suprimir(p.der, x, h)
        if h[0]:
            p = balancear_izquierda(p)
    else:
        if p.con > 1:
            p.con -= 1
        else:
            if p.der is None:
                return p.izq
            if p.izq is None:
                return p.der
            c = encontrar_min(p.der)
            p.key = c.key
            p.con = c.con
            p.der = suprimir(p.der, c.key, h)
            if h[0]:
                p = balancear_izquierda(p)
    return p


def encontrar_min(p):
    while p.izq is not None:
        p = p.izq
    return p


def mostrar(p):
    if p is not None:
        print(f"Clave: {p.key}, Repeticiones: {p.con}")
        print("Izquierda:")
        mostrar(p.izq)
        print("Derecha:")
        mostrar(p.der)


if __name__ == "__main__":
    p = None
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
                h = [0]
                print(h[0])
                p = insertar(p, ele, h)
                print(f"Elemento {ele} insertado en el árbol.")
                ele = int(input("Ingrese elemento a insertar, el ingreso finaliza con 0: "))
        elif op == 2:
            ele = int(input("Ingrese elemento a suprimir, el ingreso finaliza con 0: "))
            while ele != 0:
                h = [0]
                p = suprimir(p, ele, h)
                if h[0]:
                    print(f"Elemento {ele} suprimido del árbol.")
                ele = int(input("Ingrese elemento a suprimir, el ingreso finaliza con 0: "))
        elif op == 3:
            mostrar(p)
