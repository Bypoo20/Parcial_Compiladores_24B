import csv
from graphviz import Digraph

class Nodo:
    def __init__(self, etiqueta, identificador):
        self.etiqueta = etiqueta
        self.identificador = identificador
        self.hijos = []

    def agregar_hijo(self, hijo):
        self.hijos.append(hijo)

def cargar_rastreo(nombre_archivo):
    rastreo = []
    with open(nombre_archivo, mode='r') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            rastreo.append(fila)
    return rastreo

def generar_arbol_sintactico(rastreo, nombre_archivo):
    dot = Digraph(comment='Árbol Sintáctico')
    contador_nodos = 0
    nodos = {}
    reglas_diccionario = {}

    # Crear un nodo raíz para comenzar el árbol
    raiz = None

    # Crear nodos usando las reglas de la traza
    for entrada in rastreo:
        regla = entrada['Rule']
        if '->' in regla:
            cabeza, produccion = regla.split('->')
            cabeza = cabeza.strip()
            simbolos_produccion = [simbolo for simbolo in produccion.strip().split() if simbolo != "''"]

            # Almacenar la regla en el diccionario sin sobrescribir reglas existentes
            if cabeza in reglas_diccionario:
                if simbolos_produccion not in reglas_diccionario[cabeza]:
                    reglas_diccionario[cabeza].append(simbolos_produccion)
            else:
                reglas_diccionario[cabeza] = [simbolos_produccion]

            # Crear un nodo para la cabeza si no existe
            if cabeza not in nodos:
                nodo_cabeza = Nodo(cabeza, f"N{contador_nodos}")
                nodos[cabeza] = nodo_cabeza
                dot.node(nodo_cabeza.identificador, cabeza)
                contador_nodos += 1
                if raiz is None:
                    raiz = nodo_cabeza

            # Obtener el nodo cabeza actual
            nodo_cabeza = nodos[cabeza]

            # Crear nodos para cada símbolo en la producción y conectarlos correctamente
            for simbolo in simbolos_produccion:
                identificador_nodo_simbolo = f"{simbolo}_{contador_nodos}"
                nodo_simbolo = Nodo(simbolo, identificador_nodo_simbolo)
                nodos[identificador_nodo_simbolo] = nodo_simbolo
                dot.node(nodo_simbolo.identificador, simbolo)
                contador_nodos += 1

                # Conectar el nodo cabeza con el nodo símbolo
                nodo_cabeza.agregar_hijo(nodo_simbolo)
                dot.edge(nodo_cabeza.identificador, nodo_simbolo.identificador)

                # Asegurarse de que los nodos hijos también puedan tener relaciones correctas
                nodos[simbolo] = nodo_simbolo

    # Verificar y agregar nodo epsilon para nodos hoja sin hijos que estén en no_terminales.txt
    agregar_epsilon_a_hojas_sin_hijos(nodos, 'no_terminales.txt', dot)

    # Resaltar nodos hojas sin hijos con relleno amarillo
    resaltar_hojas_sin_hijos(nodos, dot)

    dot.render(nombre_archivo, format='png', cleanup=True)
    print(f"Árbol sintáctico guardado en {nombre_archivo}.png")

def agregar_epsilon_a_hojas_sin_hijos(nodos, no_terminales_file, dot):
    with open(no_terminales_file, 'r') as file:
        no_terminales = {line.strip() for line in file}
    
    for nodo in nodos.values():
        if not nodo.hijos and nodo.etiqueta in no_terminales:
            # Crear un nodo hijo con el símbolo epsilon
            identificador_nodo_epsilon = f"epsilon_{nodo.identificador}"
            nodo_epsilon = Nodo("ε", identificador_nodo_epsilon)
            nodo.agregar_hijo(nodo_epsilon)
            dot.node(nodo_epsilon.identificador, "ε", style='filled', fillcolor='yellow')
            dot.edge(nodo.identificador, nodo_epsilon.identificador)

def resaltar_hojas_sin_hijos(nodos, dot):
    for nodo in nodos.values():
        if not nodo.hijos:
            # Resaltar el nodo hoja con relleno amarillo
            dot.node(nodo.identificador, nodo.etiqueta, style='filled', fillcolor='yellow')

def main():
    nombre_archivo_rastreo = 'rastreo.csv'
    nombre_archivo_arbol = 'arbol_sintactico'

    rastreo = cargar_rastreo(nombre_archivo_rastreo)
    generar_arbol_sintactico(rastreo, nombre_archivo_arbol)

if __name__ == "__main__":
    main()
