import heapq
import collections
import os

class NodoHuffman:
    def __init__(self, caracter, frecuencia):
        self.caracter = caracter
        self.frecuencia = frecuencia
        self.izquierda = None
        self.derecha = None

    def __lt__(self, otro):
        return self.frecuencia < otro.frecuencia

def calcular_frecuencias(archivo):
    with open(archivo, 'r') as file:
        contenido = file.read()
        frecuencias = collections.Counter(contenido)
    return frecuencias

def construir_arbol_huffman(frecuencias):
    cola_prioridad = [NodoHuffman(caracter, frecuencia) for caracter, frecuencia in frecuencias.items()]
    heapq.heapify(cola_prioridad)

    while len(cola_prioridad) > 1:
        nodo_izq = heapq.heappop(cola_prioridad)
        nodo_der = heapq.heappop(cola_prioridad)
        nuevo_nodo = NodoHuffman(None, nodo_izq.frecuencia + nodo_der.frecuencia)
        nuevo_nodo.izquierda = nodo_izq
        nuevo_nodo.derecha = nodo_der
        heapq.heappush(cola_prioridad, nuevo_nodo)

    return cola_prioridad[0]

def codificar_caracteres(arbol_huffman):
    mapa_codificacion = {}

    def codificar_recursivo(nodo, codigo_actual=""):
        if nodo is not None:
            if nodo.caracter is not None:
                mapa_codificacion[nodo.caracter] = codigo_actual
            codificar_recursivo(nodo.izquierda, codigo_actual + "0")
            codificar_recursivo(nodo.derecha, codigo_actual + "1")

    codificar_recursivo(arbol_huffman)
    return mapa_codificacion

def comprimir_archivo(archivo_entrada, archivo_salida, mapa_codificacion):
    with open(archivo_entrada, 'r') as entrada, open(archivo_salida, 'wb') as salida:
        contenido = entrada.read()
        bits = "".join(mapa_codificacion[caracter] for caracter in contenido)
        bytes_comprimidos = bytearray()
        while bits:
            byte, bits = bits[:8], bits[8:]
            bytes_comprimidos.append(int(byte, 2))
        salida.write(bytes_comprimidos)

def descomprimir_archivo(archivo_comprimido, archivo_descomprimido, arbol_huffman):
    with open(archivo_comprimido, 'rb') as entrada, open(archivo_descomprimido, 'w') as salida:
        bits = "".join(f'{byte:08b}' for byte in entrada.read())
        nodo_actual = arbol_huffman
        for bit in bits:
            if bit == '0':
                nodo_actual = nodo_actual.izquierda
            else:
                nodo_actual = nodo_actual.derecha
            if nodo_actual.caracter is not None:
                salida.write(nodo_actual.caracter)
                nodo_actual = arbol_huffman

if __name__ == "__main__":
    archivo_entrada = "archivo_original.txt"
    archivo_comprimido = "archivo_comprimido.bin"
    archivo_descomprimido = "archivo_descomprimido.txt"

    # Calcular frecuencias de caracteres
    frecuencias = calcular_frecuencias(archivo_entrada)

    # Construir árbol de Huffman
    arbol_huffman = construir_arbol_huffman(frecuencias)

    # Crear mapa de codificación
    mapa_codificacion = codificar_caracteres(arbol_huffman)

    # Comprimir archivo
    comprimir_archivo(archivo_entrada, archivo_comprimido, mapa_codificacion)

    # Descomprimir archivo
    descomprimir_archivo(archivo_comprimido, archivo_descomprimido, arbol_huffman)
      
