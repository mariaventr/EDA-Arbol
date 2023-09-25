class NodoB:
    def __init__(self, hoja=True):
        self.hoja = hoja
        self.claves = []
        self.hijos = []

    def es_hoja(self):
        return self.hoja


class ArbolB:
    def __init__(self):
        self.raiz = NodoB()

    def insertar(self, valor):
        nodo_actual = self.raiz
        if len(nodo_actual.claves) == 2:
            nueva_raiz = NodoB(hoja=False)
            nueva_raiz.hijos.append(self.raiz)
            self.dividir(nueva_raiz, 0)
            self.raiz = nueva_raiz
        self.insertar_no_lleno(self.raiz, valor)

    def insertar_no_lleno(self, nodo, valor):
        i = len(nodo.claves) - 1
        if nodo.es_hoja():
            nodo.claves.append(None)
            while i >= 0 and valor < nodo.claves[i]:
                nodo.claves[i + 1] = nodo.claves[i]
                i -= 1
            nodo.claves[i + 1] = valor
        else:
            while i >= 0 and valor < nodo.claves[i]:
                i -= 1
            i += 1
            if len(nodo.hijos[i].claves) == 2:
                self.dividir(nodo, i)
                if valor > nodo.claves[i]:
                    i += 1
            self.insertar_no_lleno(nodo.hijos[i], valor)

    def dividir(self, padre, indice):
        nuevo_nodo = NodoB()
        nodo_dividido = padre.hijos[indice]
        padre.claves.insert(indice, nodo_dividido.claves[1])
        padre.hijos.insert(indice + 1, nuevo_nodo)
        nuevo_nodo.claves.append(nodo_dividido.claves[2])
        nodo_dividido.claves = nodo_dividido.claves[:1]
        if not nodo_dividido.es_hoja():
            nuevo_nodo.hijos.extend(nodo_dividido.hijos[2:])
            nodo_dividido.hijos = nodo_dividido.hijos[:2]

    def suprimir(self, valor):
        self.suprimir_recursivo(self.raiz, valor)

    def suprimir_recursivo(self, nodo, valor):
        if not nodo:
            return False

        i = 0
        while i < len(nodo.claves) and valor > nodo.claves[i]:
            i += 1

        if i < len(nodo.claves) and valor == nodo.claves[i]:
            if nodo.es_hoja():
                nodo.claves.pop(i)
            else:
                pred = self.obtener_predecesor(nodo, i)
                nodo.claves[i] = pred
                self.suprimir_recursivo(nodo.hijos[i], pred)
        else:
            es_hoja = nodo.es_hoja()
            if len(nodo.hijos) > i and not es_hoja:
                if len(nodo.hijos[i].claves) == 1:
                    if i > 0 and len(nodo.hijos[i - 1].claves) > 1:
                        self.redistribuir_hijos(nodo, i - 1, i)
                    elif i < len(nodo.hijos) - 1 and len(nodo.hijos[i + 1].claves) > 1:
                        self.redistribuir_hijos(nodo, i, i + 1)
                    else:
                        if i == len(nodo.hijos) - 1:
                            self.fusionar_nodos(nodo, i - 1, i)
                        else:
                            self.fusionar_nodos(nodo, i, i + 1)
                self.suprimir_recursivo(nodo.hijos[i], valor)
            elif es_hoja:
                print(f"El valor {valor} no se encuentra en el árbol.")

    def redistribuir_hijos(self, padre, i, j):
        nodo_i = padre.hijos[i]
        nodo_j = padre.hijos[j]
        nodo_i.claves.append(padre.claves[i])
        padre.claves[i] = nodo_j.claves[0]
        nodo_j.claves.pop(0)
        if not nodo_i.es_hoja():
            nodo_i.hijos.append(nodo_j.hijos[0])
            nodo_j.hijos.pop(0)

    def fusionar_nodos(self, padre, i, j):
        nodo_i = padre.hijos[i]
        nodo_j = padre.hijos[j]
        nodo_i.claves.append(padre.claves[i])
        nodo_i.claves.extend(nodo_j.claves)
        if not nodo_i.es_hoja():
            nodo_i.hijos.extend(nodo_j.hijos)
        padre.claves.pop(i)
        padre.hijos.pop(j)

    def obtener_predecesor(self, nodo, i):
        nodo_actual = nodo.hijos[i]
        while not nodo_actual.es_hoja():
            nodo_actual = nodo_actual.hijos[-1]
        return nodo_actual.claves[-1]

    def mostrar(self):
        self.mostrar_recursivo(self.raiz)

    def mostrar_recursivo(self, nodo, prefijo=""):
        if nodo:
            print(prefijo + str(nodo.claves))
            if not nodo.es_hoja():
                for i in range(len(nodo.hijos)):
                    self.mostrar_recursivo(nodo.hijos[i], prefijo + "  ")

if __name__ == "__main__":
    arbol_b = ArbolB()

    while True:
        print("\nMenu:")
        print("1. Insertar")
        print("2. Suprimir")
        print("3. Mostrar")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            valor = int(input("Ingrese el valor a insertar: "))
            arbol_b.insertar(valor)
        elif opcion == "2":
            valor = int(input("Ingrese el valor a suprimir: "))
            arbol_b.suprimir(valor)
        elif opcion == "3":
            arbol_b.mostrar()
        elif opcion == "4":
            break
        else:
            print("Opción no válida. Intente de nuevo.")
            
