import csv
from graphviz import Digraph

class Nodo:
    def __init__(self, etiqueta, identificador, valor=None):
        self.etiqueta = etiqueta
        self.identificador = identificador
        self.valor = valor  # Valor del nodo, como el valor del identificador
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
        input_tokens = entrada['Input'].split()
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
                valor_nodo = None

                # Buscar el valor del símbolo en la entrada
                for token in input_tokens:
                    if simbolo in token:
                        tipo, valor = token.split(':')
                        if tipo == simbolo:
                            valor_nodo = valor
                            break

                if valor_nodo:
                    nodo_simbolo = Nodo(simbolo, identificador_nodo_simbolo, valor=valor_nodo)
                    dot.node(nodo_simbolo.identificador, f"{simbolo}\nValor: {valor_nodo}")
                else:
                    nodo_simbolo = Nodo(simbolo, identificador_nodo_simbolo)
                    dot.node(nodo_simbolo.identificador, f"{simbolo}")

                nodos[identificador_nodo_simbolo] = nodo_simbolo
                contador_nodos += 1

                # Conectar el nodo cabeza con el nodo símbolo
                nodo_cabeza.agregar_hijo(nodo_simbolo)
                dot.edge(nodo_cabeza.identificador, nodo_simbolo.identificador)

                # Asegurarse de que los nodos hijos también puedan tener relaciones correctas
                nodos[simbolo] = nodo_simbolo

    # Renderizar el árbol sintáctico
    dot.render(nombre_archivo, format='png', cleanup=True)
    print(f"Árbol sintáctico guardado en {nombre_archivo}.png")
    return raiz, nodos, dot

def agregar_nodo_epsilon_a_hojas(raiz, no_terminales, nodos, dot):
    # Recorrer todos los nodos para encontrar hojas sin hijos
    def recorrer_nodos(nodo):
        if not nodo.hijos:  # Es una hoja
            etiqueta_normalizada = nodo.etiqueta.strip("' ")
            if etiqueta_normalizada in no_terminales:  # Verificar si es un no terminal
                # Agregar un nodo hijo con el símbolo epsilon
                nodo_epsilon = Nodo('ε', f"N{len(nodos)}")
                nodo.agregar_hijo(nodo_epsilon)
                nodos[nodo_epsilon.identificador] = nodo_epsilon
                dot.node(nodo_epsilon.identificador, 'ε')
                dot.edge(nodo.identificador, nodo_epsilon.identificador)
        else:
            for hijo in nodo.hijos:
                recorrer_nodos(hijo)

    recorrer_nodos(raiz)

def cargar_no_terminales(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        return [line.strip("'\n ") for line in archivo]

def main():
    nombre_archivo_rastreo = 'rastreo.csv'
    nombre_archivo_arbol = 'arbol_sintactico'
    nombre_archivo_no_terminales = 'no_terminales.txt'

    rastreo = cargar_rastreo(nombre_archivo_rastreo)
    no_terminales = cargar_no_terminales(nombre_archivo_no_terminales)
    raiz, nodos, dot = generar_arbol_sintactico(rastreo, nombre_archivo_arbol)

    # Agregar nodos epsilon a las hojas que sean no terminales
    if raiz:
        agregar_nodo_epsilon_a_hojas(raiz, no_terminales, nodos, dot)

    # Renderizar nuevamente el árbol con los nodos epsilon agregados
    dot.render("arbol_sintactico", format='png', cleanup=True)

if __name__ == "__main__":
    main()
