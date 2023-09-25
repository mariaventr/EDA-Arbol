class NodoArbolB:
    def __init__(self, hoja=True):
        self.hoja = hoja
        self.claves = []
        self.hijos = []

class ArbolB:
    def __init__(self, t):
        self.raiz = NodoArbolB(True)
        self.t = t

    def insertar(self, k):
        raiz = self.raiz
        if len(raiz.claves) == (2 * self.t) - 1:
            nuevo_nodo = NodoArbolB()
            nuevo_nodo.hijos.append(raiz)
            self.raiz = nuevo_nodo
            self.dividir_nodo(nuevo_nodo, 0)
            self.insertar_no_lleno(nuevo_nodo, k)
        else:
            self.insertar_no_lleno(raiz, k)

    def insertar_no_lleno(self, x, k):
        i = len(x.claves) - 1
        if x.hoja:
            x.claves.append(0)
            while i >= 0 and k < x.claves[i]:
                x.claves[i + 1] = x.claves[i]
                i -= 1
            x.claves[i + 1] = k
        else:
            while i >= 0 and k < x.claves[i]:
                i -= 1
            i += 1
            if len(x.hijos[i].claves) == (2 * self.t) - 1:
                self.dividir_nodo(x, i)
                if k > x.claves[i]:
                    i += 1
            self.insertar_no_lleno(x.hijos[i], k)

    def dividir_nodo(self, x, i):
        t = self.t
        y = x.hijos[i]
        z = NodoArbolB(y.hoja)
        x.hijos.insert(i + 1, z)
        x.claves.insert(i, y.claves[t - 1])
        z.claves = y.claves[t:(2 * t) - 1]
        y.claves = y.claves[0:(t - 1)]
        if not y.hoja:
            z.hijos = y.hijos[t:(2 * t)]
            y.hijos = y.hijos[0:t]

    def eliminar(self, k):
        raiz = self.raiz
        self.eliminar_clave(raiz, k)
        if not raiz.claves and len(raiz.hijos) > 0:
            self.raiz = raiz.hijos[0]

    def eliminar_clave(self, x, k):
        i = 0
        while i < len(x.claves) and k > x.claves[i]:
            i += 1
        if i < len(x.claves) and k == x.claves[i]:
            self.eliminar_clave_de_nodo(x, k, i)
        elif not x.hoja:
            self.eliminar_clave_de_no_hoja(x, k, i)
        elif x.hoja:
            print("La clave", k, "no está en el árbol")

    def eliminar_clave_de_nodo(self, x, k, i):
        if x.hoja:
            del x.claves[i]
        else:
            k = x.claves[i]
            if len(x.hijos[i].claves) >= self.t:
                pred = self.get_predecesor(x.hijos[i])
                x.claves[i] = pred
                self.eliminar_clave(x.hijos[i], pred)
            elif len(x.hijos[i + 1].claves) >= self.t:
                succ = self.get_sucesor(x.hijos[i + 1])
                x.claves[i] = succ
                self.eliminar_clave(x.hijos[i + 1], succ)
            else:
                self.fusionar(x, i)
                self.eliminar_clave(x.hijos[i], k)

    def eliminar_clave_de_no_hoja(self, x, k, i):
        t = self.t
        if len(x.hijos[i].claves) < t:
            if i > 0 and len(x.hijos[i - 1].claves) >= t:
                self.tomar_del_anterior(x, i)
            elif i < len(x.hijos) - 1 and len(x.hijos[i + 1].claves) >= t:
                self.tomar_del_siguiente(x, i)
            else:
                if i < len(x.hijos):
                    self.fusionar(x, i)
                else:
                    self.fusionar(x, i - 1)
            if i == len(x.claves) and len(x.hijos) > i:
                self.eliminar_clave(x.hijos[i], k)
            else:
                self.eliminar_clave(x.hijos[i + 1], k)
        else:
            self.eliminar_clave(x.hijos[i], k)

    def get_predecesor(self, x):
        if x.hoja:
            return x.claves[len(x.claves) - 1]
        return self.get_predecesor(x.hijos[len(x.claves)])

    def get_sucesor(self, x):
        if x.hoja:
            return x.claves[0]
        return self.get_sucesor(x.hijos[0])

    def tomar_del_anterior(self, x, i):
        hijo = x.hijos[i]
        hermano = x.hijos[i - 1]

        hijo.claves.insert(0, x.claves[i - 1])
        if not hijo.hoja:
            hijo.hijos.insert(0, hermano.hijos.pop())

        x.claves[i - 1] = hermano.claves.pop()
        
    def tomar_del_siguiente(self, x, i):
        hijo = x.hijos[i]
        hermano = x.hijos[i + 1]

        hijo.claves.append(x.claves[i])
        if not hijo.hoja:
            hijo.hijos.append(hermano.hijos.pop(0))

        x.claves[i] = hermano.claves.pop(0)

    def fusionar(self, x, i):
        hijo = x.hijos[i]
        hermano = x.hijos[i + 1]

        hijo.claves.append(x.claves[i])
        hijo.claves.extend(hermano.claves)
        if not hijo.hoja:
            hijo.hijos.extend(hermano.hijos)

        x.claves.pop(i)
        x.hijos.pop(i + 1)

    def mostrar_arbol(self, x, nivel=0):
        if x is not None:
            print("Nivel", nivel, ":", x.claves)
            nivel += 1
            if not x.hoja:
                for c in x.hijos:
                    self.mostrar_arbol(c, nivel)

def main():
    t = int(input("Ingrese el grado mínimo del Árbol B: "))
    arbol_b = ArbolB(t)

    while True:
        print("\nMenú:")
        print("1. Insertar clave")
        print("2. Suprimir clave")
        print("3. Mostrar Árbol")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            clave = int(input("Ingrese la clave a insertar: "))
            arbol_b.insertar(clave)
        elif opcion == '2':
            clave = int(input("Ingrese la clave a suprimir: "))
            arbol_b.eliminar(clave)
        elif opcion == '3':
            print("\nÁrbol B:")
            arbol_b.mostrar_arbol(arbol_b.raiz)
        elif opcion == '4':
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
            
