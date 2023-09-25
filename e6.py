class Item:
    def __init__(self, key):
        self.key = key
        self.count = 1
        self.p = None

class Pagina:
    def __init__(self):
        self.m = 0
        self.p0 = None
        self.e = []

orden = 2
raiz = None

def buscar(a, x):
    if a is None:
        return None

    l, r = 0, a.m - 1

    while l <= r:
        i = (l + r) // 2
        if a.e[i].key < x:
            l = i + 1
        else:
            r = i - 1

    return l

def insertar(x, a):
    global raiz
    if a is None:
        v = Item(x)
        raiz = Pagina()
        raiz.m = 1
        raiz.e.append(v)
        return

    index = buscar(a, x)

    if index < a.m and a.e[index].key == x:
        a.e[index].count += 1
    else:
        insertar_pagina(x, a, index)

def insertar_pagina(x, a, index):
    global raiz
    v = Item(x)
    if a.m < 2 * orden:
        a.e.insert(index, v)
        a.m += 1
    else:
        dividir_pagina(x, a, index)

def dividir_pagina(x, a, index):
    global raiz
    b = Pagina()
    mid = orden

    if index <= orden:
        mid -= 1

    b.e = a.e[mid + 1:]
    a.e = a.e[:mid]
    a.m = len(a.e)

    if index <= orden:
        insertar_pagina(x, a, index)
    else:
        insertar_pagina(x, b, index - mid - 1)

    if a is raiz:
        raiz = Pagina()
        raiz.m = 1
        raiz.e.append(b)
        raiz.p0 = a

def buscar_elemento(x, a):
    if a is None:
        return None

    index = buscar(a, x)

    if index < a.m and a.e[index].key == x:
        return a.e[index]

    if index <= a.m:
        return buscar_elemento(x, a.e[index].p)

def eliminar(x, a):
    if a is None:
        return

    index = buscar(a, x)

    if index < a.m and a.e[index].key == x:
        if a.e[index].count > 1:
            a.e[index].count -= 1
        else:
            eliminar_entrada(x, a, index)
    else:
        eliminar(x, a.e[index].p)

def eliminar_entrada(x, a, index):
    global raiz
    if a.m > orden:
        if index > 0:
            a.e[index - 1].count -= 1
        else:
            a.e[index + 1].count -= 1
    else:
        eliminar_combinacion(x, a, index)

def eliminar_combinacion(x, a, index):
    global raiz
    if a is raiz:
        if a.m == 1 and a.p0 is not None:
            raiz = a.p0
        return

    prev = a.e[index - 1]
    next = a.e[index + 1]

    if prev.m > orden:
        tomar_de_anterior(x, a, prev, index)
    elif next.m > orden:
        tomar_de_siguiente(x, a, next, index)
    else:
        combinar(a, index)

def tomar_de_anterior(x, a, prev, index):
    hijo = a.e[index].p
    hermano = a.e[index - 1].p
    hijo.e.insert(0, hermano.e.pop())
    a.e[index - 1] = prev.e.pop()
    a.e.insert(index, hijo.e.pop(0))

def tomar_de_siguiente(x, a, next, index):
    hijo = a.e[index].p
    hermano = a.e[index + 1].p
    hijo.e.append(next.e.pop(0))
    a.e[index + 1] = next.e[0]
    a.e[index] = hijo.e.pop()

def combinar(a, index):
    global raiz
    if index == a.m:
        index -= 1

    hijo = a.e[index].p
    hermano = a.e[index + 1].p
    hijo.e.append(a.e[index])
    hijo.e.extend(hermano.e)
    a.e.pop(index + 1)
    a.m -= 1

def imprimir_arbol(nodo, nivel=0):
    if nodo:
        print("Nivel", nivel, ":", end=" ")
        for item in nodo.e:
            print(item.key, end=" ")
        print()
        nivel += 1
        if nodo.e:
            for hijo in nodo.e:
                imprimir_arbol(hijo.p, nivel)

while True:
    print("\n\n Menú ")
    print("\n 1_ Insertar ")
    print("\n 2_ Eliminar ")
    print("\n 3_ Mostrar ")
    print("\n 4_ Salir ")
    print("\n")
    op = int(input("Ingrese opción: "))

    if op == 1:
        print("\n Ingrese clave a insertar (Finaliza con -1) ")
        x = int(input())

        while x >= 0:
            insertar(x, raiz)
            print("\n Ingrese clave a insertar (Finaliza con -1) ")
            x = int(input())
    elif op == 2:
        print("Ingrese clave a eliminar (Finaliza con -1) ")
        x = int(input())

        while x >= 0:
            eliminar(x, raiz)
            print("\n Ingrese clave a eliminar (Finaliza con -1) ")
            x = int(input())
    elif op == 3:
        imprimir_arbol(raiz)
    elif op == 4:
        break
                   
