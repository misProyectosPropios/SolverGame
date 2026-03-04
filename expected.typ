#let project_title = "Análisis de Enumerabilidad en Juegos Aritméticos"

= #project_title

== Definición del Espacio de Búsqueda
Sea $S$ el conjunto de todos los números alcanzables. Definimos la gramática:
$ E := n | E op_b E | op_u (E) $

== Implementación
El sistema utiliza un enfoque de *fuerza bruta inteligente*:
- *Generación de ASTs*: Para $n$ términos, se evalúan todas las topologías de árboles binarios.
- *Funciones Unarias*: Se establece un límite de profundidad $d$ para evitar ciclos triviales (ej. $cos(cos(...))$).

#quote(block: true)[
  *Nota sobre Computabilidad:* El sistema es un semidecisor. Si $x in S$, el programa retorna la secuencia de pasos. Si $x cancel(in) S$, la búsqueda podría no terminar.
]

#box(fill: luma(240), inset: 10pt, radius: 5pt)[
  *El Reto:* Dado el esquema $ 1 space square space 1 space square space 1 = X $, 
  encontrar la configuración de operadores tal que la igualdad sea válida.
]

En este proyecto, expandimos las reglas tradicionales permitiendo:
- *Funciones Unarias:* $f(x)$ donde $f \in \{
  #text("sin"), #text("cos"), #text("tan"), #text("!"), #text("sqrt"), dots.h \}$
- *Anidamiento Infinito:* Aplicación recursiva de funciones.

Para averiguar después: 
- Ver si se puede hacer total computable o no 