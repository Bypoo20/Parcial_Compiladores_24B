class ObjetoTablaSimbolos:
    def __init__(self, lexema, tipo_dato="void", tipo="var", ambito="global"):
        self.lexema = lexema
        self.tipo_dato = tipo_dato
        self.tipo = tipo
        self.ambito = ambito

class TablaSimbolos:
    def __init__(self):
        self.pila = []

    def agregar_objeto(self, objeto):
        self.pila.append(objeto)

    def imprimir_pila(self):
        for obj in self.pila:
            print(f"Lexema: {obj.lexema}, Tipo Dato: {obj.tipo_dato}, Tipo: {obj.tipo}, Ámbito: {obj.ambito}")

    def agregar_objetos(self, nodo_raiz, ambito="global"):
        self._buscar_varfun(nodo_raiz, ambito)

    def _buscar_varfun(self, nodo, ambito):
        if nodo.etiqueta == "FUNCION":
            # Crear un objeto para la función
            identificador = next((hijo for hijo in nodo.hijos if hijo.etiqueta == "IDENTIFICADOR"), None)
            if identificador:
                nuevo_objeto = ObjetoTablaSimbolos(lexema=identificador.valor, tipo="function", ambito=ambito)
                self.agregar_objeto(nuevo_objeto)
                # Truncar el recorrido si se encuentra una función
                return
        elif nodo.etiqueta == "ASIGNACION":
            # Crear un objeto para la variable
            identificador = next((hijo for hijo in nodo.hijos if hijo.etiqueta == "IDENTIFICADOR"), None)
            if identificador:
                nuevo_objeto = ObjetoTablaSimbolos(lexema=identificador.valor, tipo="var", ambito=ambito)
                self.agregar_objeto(nuevo_objeto)
        # Continuar recorriendo los hijos
        for hijo in nodo.hijos:
            self._buscar_varfun(hijo, ambito)

# Ejemplo de uso con el árbol generado
from Generar_Arbol import cargar_rastreo, generar_arbol_sintactico

def main():
    # Cargar el archivo de rastreo y generar el árbol sintáctico
    nombre_archivo_rastreo = 'rastreo.csv'
    nombre_archivo_arbol = 'arbol_sintactico'
    rastreo = cargar_rastreo(nombre_archivo_rastreo)
    raiz, nodos, dot = generar_arbol_sintactico(rastreo, nombre_archivo_arbol)

    # Crear la tabla de símbolos
    if raiz:
        tabla_simbolos = TablaSimbolos()
        tabla_simbolos.agregar_objetos(raiz)

        # Imprimir la pila de la tabla de símbolos
        tabla_simbolos.imprimir_pila()

if __name__ == "__main__":
    main()
