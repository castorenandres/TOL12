Primer avance:
    Se diseño la primera versión de la sintaxis para el lenguaje de The Only Lonely Project.
    Se generaron los diagramas de sintaxis.
    Se generaron las reglas gramaticales con base a los diagramas de sintaxis.
    Los tokens se tradujeron a ingles y se cambiaron algunos de nombre.
    Implementacion del lexico y sintaxis:
        Lexico version 1 completa
        Parser version 1 parcial
            Donde quede: empezar desarrollo de punto

Segundo avance:
    Implementacion del lexico y sintaxis:
        Parser version 1 completa
    Se hicieron cambios a los diagramas y las reglas de vars, func y programa
    Diseño de puntos neuralgicos en diagrama de sintaxis (completa)
    Diseño de tabla de funciones y de variables (completa)
    Diseño de la tabla de consideracion sematica (parcial)
    Programado:
        aun no se programa nada sobre tablas
        se empezó a jugar con la herramienta para hacer las acciones de los puntos neuralgicos.

Tercer avance:
    Diseño de tabla de consideracion semantica (completa)
    Rediseñar/Dividir reglas debido a la herramienta para hacer acciones. (en proceso)
    Checar puntos neuralgicos de flujos lineales (read, write, etc) (pendiente)
    Checar puntos neuralgicos de flujos no lineales (if, while, etc) (pendiente)
    Programado:
        se borro la regla vars4 porque no se usaba
        seguir experimientando con herramienta, ya se como funcionan las reglas.
        estructura para tabla de funciones y variables (completa)
        metodos para las tablas de funciones y variables (parcial)

Cuarto avance:
    Rediseño y división de reglas para expresiones completa.
    Rediseño y división de reglas para estatutos no lineales en proceso.
    Programado:
        se agregaron reglas para expresiones.
        se pueden agregar funciones y variables a las tablas.
        falta integrar los cuadruplos para expresiones.

Quinto avance:
    Rediseño y división de reglas para estatutos no lineales casi completa, se esta diseñando para el ciclo for.
    Diseñando cuadruplos.
    Programado:
        se agregaron reglas para estatutos no lineales.
        falta integrar los cuadruplos para estatutos no lineales.

Sexto avance:
    Trabajando todavia en el diseño para el ciclo de for.
    Diseñando una tablita para asiganrle un codigo numerico (numero) a los operadores para usar en los cuadruplos.

Septimo avance:
    Se implementaron cuadruplos para expresiones y para estatutos lineales, falta ponerlo con direcciones de memoria.
    Cambio de llaves en las estructuras de las tablas de funciones y variables.
    Diseñando la division para reglas gramaticales para funciones y llamadas a funcion.
    generando metodos y estructuras que se utilizaran para los cuadruplos de funciones y sus llamadas.
    Se implementaron cuadruplos para funciones, falta ponerlo con direcciones de memoria.

Octavo avance:
    Se implementaron cuadruplos para llamadas, falta ponerlo con direcciones de memoria.
    Diseñando las direcciones para los cuadruplos.
    diseño de tabla de constantes
    implementar tabla de constantes
    Agregar direcciones para cuadruplos.
    Agregar funcion de fill de cuadruplos

    Haciendo:
    Diseñar la memoria y sus metodos

    Pendiente:
    Implementar memoria
    Empezar la maquina virtual