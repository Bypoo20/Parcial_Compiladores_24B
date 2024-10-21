
# Proyecto de Análisis Sintáctico y Léxico

Este proyecto contiene la implementación de un analizador léxico y sintáctico basado en Python, con ejemplos y la visualización de árboles sintácticos generados a partir de una gramática específica. Además, incluye scripts relacionados con la generación de tablas sintácticas LL(1) y el rastreo del análisis.

## Estructura del Proyecto

La estructura del proyecto es la siguiente:

```
├── Codigos
│   ├── AnalizadorSintactico.py
│   ├── arbol_sintactico.png
│   ├── Generar_Arbol.py
│   ├── Gramatica.txt
│   ├── Lexer_Python_ES.py
│   ├── ll1_table.csv
│   ├── no_terminales.txt
│   ├── rastreo.csv
│   ├── Tabla_Sintactica.py
│   └── tokens.txt
│
├── Ejemplos
│   ├── Ejemplo01
│   │   ├── arbol_sintactico.png
│   │   ├── CodigoPrueba.txt
│   │   ├── rastreo.csv
│   │   └── tokens.txt
│   ├── Ejemplo02
│   │   ├── arbol_sintactico.png
│   │   ├── CodigoPrueba.txt
│   │   ├── rastreo.csv
│   │   └── tokens.txt
│   ├── Ejemplo03
│   │   ├── arbol_sintactico.png
│   │   ├── CodigoPrueba.txt
│   │   ├── rastreo.csv
│   │   └── tokens.txt
│   └── Ejemplo04
│       ├── arbol_sintactico.png
│       ├── CodigoPrueba.txt
│       ├── rastreo.csv
│       └── tokens.txt
│
└── Latex
    ├── ExamenParcialCompiladores.pdf
    └── ExamenParcialCompiladores.zip
```


## Descripción de Carpetas

### 1. **[Codigos](./Codigos)**
Esta carpeta contiene los scripts principales del proyecto:
- **[AnalizadorSintactico.py](./Codigos/AnalizadorSintactico.py)**: Implementación del analizador sintáctico basado en la gramática LL(1).
- **[arbol_sintactico.png](./Codigos/arbol_sintactico.png)**: Imagen que muestra el árbol sintáctico generado.
- **[Generar_Arbol.py](./Codigos/Generar_Arbol.py)**: Script para generar el árbol sintáctico en formato gráfico.
- **[Gramatica.txt](./Codigos/Gramatica.txt)**: Archivo de texto que contiene la definición de la gramática utilizada.
- **[Lexer_Python_ES.py](./Codigos/Lexer_Python_ES.py)**: Implementación del analizador léxico para el lenguaje definido.
- **[ll1_table.csv](./Codigos/ll1_table.csv)**: Tabla LL(1) generada a partir de la gramática.
- **[no_terminales.txt](./Codigos/no_terminales.txt)**: Lista de no terminales de la gramática.
- **[rastreo.csv](./Codigos/rastreo.csv)**: Archivo CSV que contiene el rastreo del análisis sintáctico.
- **[Tabla_Sintactica.py](./Codigos/Tabla_Sintactica.py)**: Script para generar y manejar la tabla sintáctica LL(1).
- **[tokens.txt](./Codigos/tokens.txt)**: Archivo que contiene los tokens generados por el lexer.

### 2. **[Ejemplos](./Ejemplos)**
Cada subcarpeta en **Ejemplos** contiene:
- **arbol_sintactico.png**: Visualización del árbol sintáctico generado.
- **CodigoPrueba.txt**: Código fuente utilizado como entrada de prueba para el analizador.
- **rastreo.csv**: Rastreo de las reglas sintácticas aplicadas.
- **tokens.txt**: Tokens generados durante el análisis léxico.

### 3. **[Latex](./Latex)**
Esta carpeta contiene los archivos relacionados con la documentación del proyecto:
- **[ExamenParcialCompiladores.pdf](./Latex/ExamenParcialCompiladores.pdf)**: Documento PDF generado como parte de los exámenes o pruebas parciales del curso.
- **[ExamenParcialCompiladores.zip](./Latex/ExamenParcialCompiladores.zip)**: Archivo comprimido con los archivos LaTeX y otros recursos.

## Requisitos del Sistema

- Python 3.x
- Biblioteca `ply` para el análisis léxico y sintáctico.
- `graphviz` para la generación de gráficos de árboles sintácticos.

## Instrucciones de Uso

1. Clona el repositorio en tu máquina local:
   ```bash
   git clone https://github.com/usuario/proyecto-analisis-sintactico.git
   cd proyecto-analisis-sintactico

2. Instala las dependencias necesarias:
   ```bash
   pip install ply graphviz
   ```

3. Para ejecutar el analizador léxico:
   ```bash
   python Codigos/Lexer_Python_ES.py
   ```

4. Para generar un árbol sintáctico a partir de un rastreo:
   ```bash
   python Codigos/Generar_Arbol.py
   ```

5. Para ejecutar el analizador sintáctico:
   ```bash
   python Codigos/AnalizadorSintactico.py
   ```
