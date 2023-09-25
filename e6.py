class Item:
    def __init__(self, key):
        self.key = key
        self.count = 1
        self.p = None

class Page:
    def __init__(self):
        self.m = 0
        self.p0 = None
        self.e = []

def insert(x, a, h):
    v = None  # Inicializa v con un valor predeterminado
    if a is None:
        h[0] = 1
        v = Item(x)
    else:
        l = 0
        r = a.m
        i = 0
        while l < r:
            i = (l + r) // 2
            if a.e[i].key <= x:
                l = i + 1
            else:
                r = i
        r -= 1
        if r >= 0 and a.e[r].key == x:
            a.e[r].count += 1
            h[0] = 0
        else:
            if r == 0 and a.e[r].key > x:
                p = insert(x, a.p0, h)
            else:
                p = insert(x, a.e[r].p, h)
            if h[0]:
                if a.m < 2 * n:
                    h[0] = 0
                    a.m += 1
                    a.e.insert(r, p)  # Inserta p en la posición correcta
                else:
                    b = Page()
                    if r <= n:
                        for i in range(n):
                            b.e.append(a.e.pop(n))  # Pop en la posición n
                        if r == n:
                            v = a.e.pop(0)  # Pop en la posición 0
                            b.e.insert(0, p)
                        else:
                            if a.e[n - 1].key < x:
                                v = p
                            else:
                                v = a.e[n - 1]
                                if a.e[0].key < x:
                                    a.e.pop(n - 1)  # Pop en la posición n - 1
                                else:
                                    a.e.insert(r, p)  # Inserta p en la posición correcta
                    else:
                        r -= n
                        v = a.e[n]
                        for i in range(r):
                            b.e.append(a.e.pop(n + 1))  # Pop en la posición n + 1
                        b.e.append(p)
                        for i in range(r + 1, n + 1):
                            b.e.append(a.e.pop(n + 1))  # Pop en la posición n + 1
                    a.m = n
                    b.m = n
                    b.p0 = v.p
                    v.p = b
    return v



def vacio(c, a, s, h):
    b = Page()
    mb = c.m
    if s > mb:
        s += 1
        b = c.e[s].p
        mb = b.m
        k = (mb - n + 1) // 2
        a.e.insert(n, c.e[s])
        a.e[n].p = b.p0
        if k > 0:
            for i in range(k - 1):
                a.e.insert(i + n, b.e[i])
            c.e[s] = b.e[k]
            c.e[s].p = b
            mb -= k
            for i in range(mb):
                b.e[i] = b.e[i + k]
            b.m = mb
            a.m = n - 1 + k
            h[0] = 0
        else:
            for i in range(n):
                a.e.insert(i + n, b.e[i])
            b = None
            for i in range(s, mb - 1):
                c.e[i] = c.e[i + 1]
                c.e[i].p = c.e[i + 1].p
            c.m = mb - 1
            h[0] = 0
    else:
        if s == 0:
            b = c.p0
        else:
            b = c.e[s - 1].p
        mb = b.m
        k = (mb - n) // 2
        if k > 0:
            for i in range(n - 1, -1, -1):
                a.e[i + k] = a.e[i]
            a.e[k] = c.e[s]
            a.e[k].p = a.p0
            mb -= k
            for i in range(k - 1, -1, -1):
                a.e[i] = b.e[i + mb]
            a.p0 = b.e[mb].p
            c.e[s] = b.e[mb]
            c.e[s].p = a
            b.m = mb - 1
            a.m = n - 1 + k
            h[0] = 0
        else:
            for i in range(n):
                a.e[i + n] = b.e[i]
            b = None
            for i in range(s, c.m - 1):
                c.e[i] = c.e[i + 1]
                c.e[i].p = c.e[i + 1].p
            a.m = 2 * n
            c.m -= 1
            h[0] = 0

def sup(p, a, h):
    q = p.e[p.m - 1].p
    if q is not None:
        sup(q, p, h)
        if h[0] == 1:
            vacio(p, q, p.m - 1, h)
    else:
        a.e.pop(0)
        p.m -= 1
        if p.m < n:
            h[0] = 1

def eliminar(x, a, h):
    l = 0
    i = 0
    r = a.m
    q = None
    while l < r:
        i = (l + r) // 2
        if a.e[i].key <= x:
            l = i + 1
        else:
            r = i
    r -= 1
    if r >= 0 and a.e[r].key == x:
        if a.e[r].count > 1:
            a.e[r].count -= 1
            h[0] = 0
        else:
            q = a.e[r].p
            if q is not None:
                sup(q, a, h)
                if h[0] == 1:
                    vacio(a, q, r, h)
            else:
                a.e.pop(r)
                a.m -= 1
                if a.m < n:
                    h[0] = 1
    else:
        q = a.e[r].p
        if q is not None:
            eliminar(x, q, h)
            if h[0] == 1:
                vacio(a, q, r, h)

def mostrar(p, niv):
    if p is not None:
        for _ in range(niv):
            print(" ")
        for i in range(p.m):
            print(p.e[i].key, end=" ")
        print()
        mostrar(p.p0, niv + 1)
        for i in range(p.m):
            mostrar(p.e[i].p, niv + 1)

n = 2
raiz = None
h = [0]

while True:
    print("\n\nMenú")
    print("1. Insertar")
    print("2. Eliminar")
    print("3. Mostrar")
    print("4. Salir")
    op = int(input("Ingrese opción: "))

    if op == 1:
        x = int(input("Ingrese clave a insertar (Finaliza con -1): "))
        while x >= 0:
            insert(x, raiz, h)
            if h[0]:
                q = raiz
                raiz = Page()
                raiz.m = 1
                raiz.p0 = q
                raiz.e.append(Item(x))
            x = int(input("Ingrese clave a insertar (Finaliza con -1): "))

    elif op == 2:
        x = int(input("Ingrese clave a eliminar (Finaliza con -1): "))
        while x >= 0:
            eliminar(x, raiz, h)
            if h[0]:
                if raiz.m == 0:
                    q = raiz
                    raiz = q.p0
            mostrar(raiz, 0)
            x = int(input("Ingrese clave a eliminar (Finaliza con -1): "))

    elif op == 3:
        mostrar(raiz, 0)

    elif op == 4:
        break
