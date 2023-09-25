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

n = 2
raiz = None

def binary_search(a, x):
    l, r = 0, a.m - 1

    while l <= r:
        i = (l + r) // 2
        if a.e[i].key < x:
            l = i + 1
        else:
            r = i - 1

    return l

def insert(x, a):
    global raiz
    if a is None:
        v = Item(x)
        raiz = Page()
        raiz.m = 1
        raiz.e.append(v)
        return

    index = binary_search(a, x)

    if index < a.m and a.e[index].key == x:
        a.e[index].count += 1
    else:
        insert_page(x, a, index)

def insert_page(x, a, index):
    global raiz
    v = Item(x)
    if a.m < 2 * n:
        a.e.insert(index, v)
        a.m += 1
    else:
        split_page(x, a, index)

def split_page(x, a, index):
    global raiz
    b = Page()
    mid = n

    if index <= n:
        mid -= 1

    b.e = a.e[mid + 1:]
    a.e = a.e[:mid]
    a.m = len(a.e)

    if index <= n:
        insert_page(x, a, index)
    else:
        insert_page(x, b, index - mid - 1)

    if a is raiz:
        raiz = Page()
        raiz.m = 1
        raiz.e.append(b)
        raiz.p0 = a

def search(x, a):
    if a is None:
        return None

    index = binary_search(a, x)

    if index < a.m and a.e[index].key == x:
        return a.e[index]

    if index <= a.m:
        return search(x, a.e[index].p)

def delete(x, a):
    if a is None:
        return

    index = binary_search(a, x)

    if index < a.m and a.e[index].key == x:
        if a.e[index].count > 1:
            a.e[index].count -= 1
        else:
            delete_entry(x, a, index)
    else:
        delete(x, a.e[index].p)

def delete_entry(x, a, index):
    if a.m > n:
        if index > 0:
            a.e[index - 1].count -= 1
        else:
            a.e[index + 1].count -= 1
    else:
        delete_merge(x, a, index)

def delete_merge(x, a, index):
    global raiz
    if a is raiz:
        if a.m == 1 and a.p0 is not None:
            raiz = a.p0
        return

    prev = a.e[index - 1]
    next = a.e[index + 1]

    if prev.m > n:
        borrow_from_prev(x, a, prev, index)
    elif next.m > n:
        borrow_from_next(x, a, next, index)
    else:
        merge(a, index)

def borrow_from_prev(x, a, prev, index):
    child = a.e[index].p
    sibling = a.e[index - 1].p
    child.e.insert(0, sibling.e.pop())
    a.e[index - 1] = prev.e.pop()
    a.e.insert(index, child.e.pop(0))

def borrow_from_next(x, a, next, index):
    child = a.e[index].p
    sibling = a.e[index + 1].p
    child.e.append(next.e.pop(0))
    a.e[index + 1] = next.e[0]
    a.e[index] = child.e.pop()

def merge(a, index):
    global raiz
    if index == a.m:
        index -= 1

    child = a.e[index].p
    sibling = a.e[index + 1].p
    child.e.append(a.e[index])
    child.e.extend(sibling.e)
    a.e.pop(index + 1)
    a.m -= 1

def print_tree(node, level=0):
    if node:
        print("Level", level, ":", end=" ")
        for item in node.e:
            print(item.key, end=" ")
        print()
        level += 1
        if node.e:
            for child in node.e:
                print_tree(child.p, level)

while True:
    print("\n\n Menú ")
    print("\n 1_ Insertar ")
    print("\n 2_ Suprimir ")
    print("\n 3_ Mostrar ")
    print("\n 4_ Salir ")
    print("\n")
    op = int(input("Ingrese opción: "))

    if op == 1:
        print("\n Ingrese clave a insertar (Finaliza con -1) ")
        x = int(input())

        while x >= 0:
            insert(x, raiz)
            print("\n Ingrese clave a insertar (Finaliza con -1) ")
            x = int(input())
    elif op == 2:
        print("Ingrese clave a suprimir (Finaliza con -1) ")
        x = int(input())

        while x >= 0:
            delete(x, raiz)
            print("\n Ingrese clave a suprimir (Finaliza con -1) ")
            x = int(input())
    elif op == 3:
        print_tree(raiz)
    elif op == 4:
        break
        
