#Algoritmos a comprobar

#Suma de la subsecuencia máxima (por conveniencia, la suma de la subsecuencia máxima es 0 si todos los enteros son negativos): 

#Se pide:
#1. Implemente en PYTHON los algoritmos propuestos:

#Algoritmo 1: O(n^2)
def sumaSubMax1(v:list) -> int: # v es el arreglo de entrada
    n=len(v)                    # n es la longitud del arreglo
    sumaMax=0                   # Inicializa la suma máxima en 0

    for i in range(0,n):            # Itera a través de todos los índices de inicio del subarreglo (0....n-1)
        estaSuma = 0                # Inicializa la suma actual en 0

        for j in range(i,n):        # Itera a través de todos los índices de fin del subarreglo (0...n-1)
            estaSuma += v[j]        # Agrega el valor del elemento v[j] a la suma actual

            if estaSuma > sumaMax:  # Si la suma actual es mayor que la suma máxima registrada
                sumaMax=estaSuma    # Actualiza la suma máxima con la suma actual
    return sumaMax                  # Devuelve la máxima suma
            
#Si no encuentra ninguna combinación que de un número mayor que 0, entonces el valor que devuelve siempre es 0. (Que es valor orginal de SumaMax, aún así debe ejecutar todos las iteraciones del algoritmo para comprobar todas las convinaciones y así comprobar que no existe ninguna convinación que de mayor que cero, por lo que la complejidad viene siendo la misma que en los otros caso en los que encuentra una solución al problema)


#Algoritmo 2: O(n)
def sumaSubMax2(v:list) -> int: 
    n=len(v)                    # n es la longitud del arreglo
    estaSuma=0                  # Inicializa la suma actual en 0
    sumaMax=0                   # Inicializa la suma máxima en 0

    for j in range(0,n):            # Itera a través de todos los elementos del arreglo
        estaSuma+=v[j]              # Agrega el valor del elemento v[j] a la suma actual

        if estaSuma > sumaMax:      # Si la suma actual es mayor que la suma máxima registrada
            sumaMax=estaSuma        # Actualiza la suma máxima con la suma actual

        elif estaSuma < 0:          # Si la suma actual es negativa
            estaSuma=0              # Reinicia la suma actual a 0

    return sumaMax                  # Devuelve la suma máxima encontrada


# La razón por la cual el primer algoritmo tiene una complejidad de O(n^2) es debido a su estructura de bucles anidados, 
# que hace que el número de operaciones aumente cuadráticamente con el tamaño de entrada.
# En contraste, el segundo algoritmo utiliza un solo bucle y realiza operaciones lineales en función del tamaño de entrada, 
# lo que lo hace más eficiente en términos de complejidad computacional.