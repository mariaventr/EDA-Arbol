import heapq
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
    frecuencias = {}
    with open(archivo, 'r') as f:
        texto = f.read()
        for caracter in texto:
            if caracter in frecuencias:
                frecuencias[caracter] += 1
            else:
                frecuencias[caracter] = 1
    return frecuencias

def construir_arbol_huffman(frecuencias):
    cola_prioridad = [NodoHuffman(caracter, frecuencia) for caracter, frecuencia in frecuencias.items()]
    heapq.heapify(cola_prioridad)

    while len(cola_prioridad) > 1:
        nodo_izquierda = heapq.heappop(cola_prioridad)
        nodo_derecha = heapq.heappop(cola_prioridad)
        nodo_padre = NodoHuffman(None, nodo_izquierda.frecuencia + nodo_derecha.frecuencia)
        nodo_padre.izquierda = nodo_izquierda
        nodo_padre.derecha = nodo_derecha
        heapq.heappush(cola_prioridad, nodo_padre)

    return cola_prioridad[0]

def codificar_caracteres(arbol, prefijo="", codificaciones={}):
    if arbol is not None:
        if arbol.caracter is not None:
            codificaciones[arbol.caracter] = prefijo
        codificar_caracteres(arbol.izquierda, prefijo + "0", codificaciones)
        codificar_caracteres(arbol.derecha, prefijo + "1", codificaciones)

def comprimir_archivo(archivo_entrada, archivo_salida):
    frecuencias = calcular_frecuencias(archivo_entrada)
    arbol = construir_arbol_huffman(frecuencias)
    codificaciones = {}
    codificar_caracteres(arbol, "", codificaciones)

    with open(archivo_entrada, 'r') as entrada, open(archivo_salida, 'wb') as salida:
        bits = ""
        while True:
            caracter = entrada.read(1)
            if not caracter:
                break
            bits += codificaciones[caracter]
            while len(bits) >= 8:
                byte = bits[:8]
                bits = bits[8:]
                salida.write(bytes([int(byte, 2)]))

        if bits:
            padding = 8 - len(bits)
            bits += "0" * padding
            salida.write(bytes([int(bits, 2)]))
            salida.write(bytes([padding]))

if __name__ == "__main__":
    archivo_entrada = "texto.txt"  # Cambia esto al nombre de tu archivo de entrada
    archivo_salida = "comprimido.bin"
    comprimir_archivo(archivo_entrada, archivo_salida)
        
