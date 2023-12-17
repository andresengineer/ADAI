'''
    ANÁLISIS Y DISEÑO DE ALGORITMOS

    El problema del Zoológico de Cali


    Programa que organiza un espectáculo en un zoológico, donde se
    presentan escenas con animales en orden ascendente según su 
    grandeza. Se busca determinar estadísticas como el animal que 
    participó en más y menos escenas, la escena con menor y mayor 
    grandeza total, y el promedio de grandeza de todo el espectáculo.
    Se apoya en el algoritmo Counting Sort.
    

    @Autor:
    - Wilson Andres Mosquera Zapata
    - mosquera.wilson@correounivalle.edu.co
    - 2182116-3743

'''

import time, random

# Encuentra el valor máximo en una lista de datos.
def encontrar_valor_maximo(datos):

    if not datos:
        return None
    
    maximo_valor = datos[0]
    
    for valor in datos:
        if valor > maximo_valor:
            maximo_valor = valor
    
    return maximo_valor



# Encuentra el valor mínimo en una lista de datos.
def encontrar_valor_minimo(datos):

    if not datos:
        return None
    
    minimo_valor = datos[0]
    
    for valor in datos:
        if valor < minimo_valor:
            minimo_valor = valor
    
    return minimo_valor



# Ordena un array de escenas en función de sus grandezas máximas.
def ordenar_escenas_por_grandeza_maxima(escenas, grandezas_totales):

    if not escenas or not grandezas_totales:
        return  

    tamaño = 0
    for escena in escenas:
        tamaño += 1
    resultado = [0] * tamaño

    índice_máximo = encontrar_valor_maximo(grandezas_totales) + 1
    conteo = [0] * índice_máximo  

    for i in range(0, tamaño):
        if len(escenas[i]) < 3:
            continue 

        conteo[escenas[i][2]] += 1

    for i in range(1, índice_máximo):
        conteo [i] += conteo[i - 1]

    i = tamaño - 1
    while i >= 0:
        escena = escenas[i]
        if len(escena) < 3:
            continue 

        grandeza_max = escena[2]
        resultado[conteo[grandeza_max] - 1] = escena
        conteo[grandeza_max] -= 1
        i -= 1

    for i in range(0, tamaño):
        escenas[i] = resultado[i]



# Ordena un array de escenas en función de sus grandezas totales.
def ordenar_escenas_por_grandezas_totales(escenas, grandezas_totales):

    if not escenas or not grandezas_totales:
        return  

    tamaño = 0
    for escena in escenas:
        tamaño += 1
    resultado = [0] * tamaño

    índice_máximo = encontrar_valor_maximo(grandezas_totales) + 1
    conteo = [0] * índice_máximo  

    for i in range(0, tamaño):
        if len(escenas[i]) < 3:
            continue 

        conteo[escenas[i][2]] += 1

    for i in range(1, índice_máximo):
        conteo [i] += conteo[i - 1]

    i = tamaño - 1
    while i >= 0:
        escena = escenas[i]
        if len(escena) < 3:
            continue 

        grandeza_max = escena[2]
        resultado[conteo[grandeza_max] - 1] = escena
        conteo[grandeza_max] -= 1
        i -= 1

    for i in range(0, tamaño):
        escenas[i] = resultado[i]



# Ordena un array de partes en función de sus grandezas totales.
def ordenar_partes_por_grandezas_totales(partes, grandezas_totales):

    if not partes or not grandezas_totales:
        return  

    tamaño = 0
    for parte in partes:
        tamaño += 1

    resultado = [0] * tamaño
    índice_máximo = encontrar_valor_maximo(grandezas_totales) + 1
    conteo = [0] * índice_máximo 

    for i in range(0, tamaño):
        if i < tamaño and partes[i]:
            grandeza_total = grandezas_totales[i]
            conteo[grandeza_total] += 1

    for i in range(1, índice_máximo):
        conteo[i] += conteo[i - 1]

    i = tamaño - 1
    while i >= 0:
        if i < tamaño and partes[i]:
            parte = partes[i]
            grandeza_total = grandezas_totales[i]
            resultado[conteo[grandeza_total] - 1] = parte
            conteo[grandeza_total] -= 1
        i -= 1

    for i in range(tamaño):
        partes[i] = resultado[i]


# Solucion #1 al problema usando Counting Sort
def solucion(partes, grandezas, n, m, k):
    grandeza_total_espectaculo = 0
    aperture = partes[0] 
    parts = partes[1:]
    animales = grandezas.keys()
    contador_apariciones = {}

    for animal in animales:
        contador_apariciones[animal] = 0


    # Calcula la suma total de grandezas y encuentra la máxima grandeza en una escena dada.
    def calcular_grandezas(escena, grandezas):
        animal_actual  = escena[0]
        contador_apariciones[animal_actual ] += 1
        grandeza_total = grandezas[animal_actual ]
        grandeza_max = grandezas[animal_actual ]

        for animalN in escena[1:]:    
            contador_apariciones[animalN] += 1
            grandeza_total += grandezas[animalN]

            if grandezas[animalN] > grandezas[animal_actual ]:
                grandeza_max = grandezas[animalN]
                animal_actual  = animalN

        return (grandeza_total, grandeza_max) 
    

    # Ordena la escena de animales según sus grandezas 
    def ordenar_escena_animales_por_grandezas(scene, animales):
        tamano = len(scene)
        salida = [0] * tamano
        (grandeza_total, grandeza_max) = calcular_grandezas(scene, animales)

        # Inicializar array de conteo
        max_indice = grandeza_max + 1
        conteo = [0] * max_indice

        # Almacenar el conteo de cada elemento en el array de conteo
        for i in range(0, tamano):
            conteo[animales[scene[i]]] += 1

        # Almacenar el conteo acumulado
        for i in range(1, max_indice):
            conteo[i] += conteo[i - 1]

        # Ordenar
        i = tamano - 1

        animales_lista = list(animales.keys())
        grandezas_lista = list(animales.values())

        while i >= 0:
            grandeza = animales[scene[i]]
            indice = grandezas_lista.index(grandeza)
            salida[conteo[grandeza] - 1] = animales_lista[indice]
            conteo[grandeza] -= 1
            i -= 1

        return [salida, grandeza_total, grandeza_max]


    # Ordena una parte de escenas según las grandezas de los animales y la grandeza total de cada escena.
    def ordenar_parte_escenas_grandezas(parte):

        escenas_Ordenadas_Internas = []
        grandezas_totales = []
        grandezas_max = []
        grandeza_total_escena = 0

        for escena in parte:
            (escena_ordenada, grandeza_total, grandeza_max) = ordenar_escena_animales_por_grandezas(escena, ANIMALES)
            escenas_Ordenadas_Internas.append((escena_ordenada, grandeza_total, grandeza_max))
            grandezas_totales.append(grandeza_total)
            grandezas_max.append(grandeza_max)
            grandeza_total_escena += grandeza_total
                    
        ordenar_escenas_por_grandeza_maxima(escenas_Ordenadas_Internas, grandezas_max)
        ordenar_escenas_por_grandezas_totales(escenas_Ordenadas_Internas, grandezas_totales)

        return [escenas_Ordenadas_Internas, grandeza_total_escena]


    # Ordena una lista de partes según las grandezas de los animales y la grandeza total de cada parte.
    def ordenar_partes(partes):
        partes_ordenadas = []
        grandezas_totales = []

    # Obtener partes ordenadas y grandezas totales
        for parte in partes:
            (parte_ordenada, grandeza_total) = ordenar_parte_escenas_grandezas(parte)
            partes_ordenadas.append(parte_ordenada)
            grandezas_totales.append(grandeza_total)

        # Ordenar las partes por la grandeza total
        ordenar_partes_por_grandezas_totales(partes_ordenadas, grandezas_totales)

        return ([partes_ordenadas, grandezas_totales])


    # Ordena una apertura de escenas según las grandezas de los animales y la grandeza total de cada escena.
    def ordenar_apertura(apertura):
            
            escenas_ordenadas = []
            grandezas_totales = []
            grandezas_maximas = []
            grandeza_total_escena = 0
            for escena in apertura:
                (escena_ordenada, grandeza_total, grandeza_max) = ordenar_escena_animales_por_grandezas(escena, ANIMALES)
                escenas_ordenadas.append((escena_ordenada, grandeza_total, grandeza_max))
                grandezas_totales.append(grandeza_total)
                grandezas_maximas.append(grandeza_max)
                grandeza_total_escena += grandeza_total
            
            escena_max = encontrar_valor_maximo(grandezas_totales)
            escena_min = encontrar_valor_minimo(grandezas_totales)

            ordenar_escenas_por_grandeza_maxima(escenas_ordenadas, grandezas_maximas)
            ordenar_escenas_por_grandezas_totales(escenas_ordenadas, grandezas_totales)

            return [escenas_ordenadas,
                    escenas_ordenadas[grandezas_totales.index(escena_max)], 
                    escenas_ordenadas[grandezas_totales.index(escena_min)],
                    grandeza_total_escena]

    # Gestión


    (aperturaF, escena_minima, escena_maxima, grandeza_total_aperture) = ordenar_apertura(aperture)
    (partesF, grandezas_totales) = ordenar_partes(parts)

    contador_animales = list(contador_apariciones.values())
    animales_maximo = encontrar_valor_maximo(contador_animales)
    animales_minimo = encontrar_valor_minimo(contador_animales)

    lista_animales_max = []
    lista_animales_min = []

    for animal in contador_apariciones:
        numero_apariciones_animal = contador_apariciones[animal]

        if numero_apariciones_animal == animales_maximo:
            lista_animales_max.append([animal, numero_apariciones_animal])

        if numero_apariciones_animal == animales_minimo:
            lista_animales_min.append([animal, numero_apariciones_animal])


    for grand in grandezas_totales:
        grandeza_total_espectaculo += grand
    grandeza_total_espectaculo += grandeza_total_aperture

    escenas_totales = ((m-1)*k)*2
    promedio = grandeza_total_espectaculo/escenas_totales

    #Resultados en terminal:


    print("El orden en el que se debe presentar los animales es:")

     print("Apertura =", aperturaF)

     for parte in partesF:
         print('Parte: ', parte)

    print("Los animales que participaron en más escenas con su respectivo numero de apariciones fueron: ",lista_animales_max )

    print("Los animales que participaron en menos escenas con su respectivo numero de apariciones fueron: ",lista_animales_min )
    
    print("La escena de menor grandeza total fue la escena", escena_minima)
    
    print("La escena de mayor grandeza total fue la escena", escena_maxima)
    
    print("El promedio de grandeza de todo el espectáculo fue de", promedio)


print('Ejemplo 1')
### Parametros de entrada
ANIMALES = {'Ciempies': 1,
            'Libelula': 2,
            'Gato': 3,
            'Perro': 4,
            'Tapir': 5,
            'Nutria': 6}

n = len(ANIMALES)
# Numero de partes
m = 3
# Numero de escenas de cada parte
k = 2

apertura = [['Tapir', 'Nutria', 'Perro'], ['Tapir', 'Perro', 'Gato'], ['Ciempies', 'Tapir', 'Gato'],
            ['Gato', 'Ciempies', 'Libelula']]

parte_1 = [['Tapir', 'Nutria', 'Perro'], ['Ciempies', 'Tapir', 'Gato']]

parte_2 = [['Gato', 'Ciempies', 'Libelula'], ['Tapir', 'Perro', 'Gato']]

partes = [apertura, parte_1, parte_2]

solucion(partes, ANIMALES, n, m, k)
print('\n')


## PRUEBAS:

## Genera animales aleatoriamente.
def generador_animales(n):
    animales = {}
    for i in range(1, n+1):
        animales[str(i)] = i
    return animales

## Genera una apertura aleatoriamente.
def generador_apertura(animales, m, k):
    escenas = (m-1) * k
    lista_animales = list(animales.keys())
    apertura = []
    
    for i in range(escenas):
        escena = random.sample(lista_animales, 3) 
        apertura.append(escena)
    
    return apertura

## Genera partes aleatoriamente.
def generador_partes(animales, m, k):
    numero_partes = m-1
    escenas = k
    lista_animales = list(animales.keys())
    partes = []
    for x in range (0, numero_partes):
        parte = []
        for i in range(escenas):
            escena = random.sample(lista_animales, 3)
            parte.append(escena)
        partes.append(parte)
    return partes

    
# print("Analisis de K")
# n = 1000
# ANIMALES = generador_animales(n)
# m = 1000
# k = 10
# for i in range (0,20):
#     ANIMALES = generador_animales(1000)
#     apertura = generador_apertura(ANIMALES, m, k)
#     partes = generador_partes(ANIMALES, m, k)
#     partes.insert(0, apertura) 
#     tiempo_inicio = time.time()
#     solucion(partes, ANIMALES, n, m, k)
#     tiempo_final = time.time()
#     tiempo_ejecucion = tiempo_final - tiempo_inicio
#     print(f'k = {k}')
#     print(f'El tiempo del calculo de K fue: {tiempo_ejecucion}') 
#     k += 5


# print("Analisis de M")
# n = 1000
# ANIMALES = generador_animales(n)
# m = 500
# k = 10
# for i in range (0,20):
#     ANIMALES = generador_animales(1000)
#     apertura = generador_apertura(ANIMALES, m, k)
#     partes = generador_partes(ANIMALES, m, k)
#     partes.insert(0, apertura) 
#     tiempo_inicio = time.time()
#     solucion(partes, ANIMALES, n, m, k)
#     tiempo_final = time.time()
#     tiempo_ejecucion = tiempo_final - tiempo_inicio
#     print(f'm = {m}')
#     print(f'El tiempo del calculo de M fue: {tiempo_ejecucion}') 
#     m += 500


# print("Analisis de N")
# n = 500
# m = 1000
# k = 10
# for i in range (0,20):
#     ANIMALES = generador_animales(n)
#     n = len(ANIMALES)
#     apertura = generador_apertura(ANIMALES, m, k)
#     partes = generador_partes(ANIMALES, m, k)
#     partes.insert(0, apertura)
#     tiempo_inicio = time.time()
#     solucion(partes, ANIMALES, n, m, k)
#     tiempo_final = time.time()
#     tiempo_ejecucion = tiempo_final - tiempo_inicio
#     print(f'n = {n}')
#     print(f'El tiempo del calculo de N fue: {tiempo_ejecucion}')
#     n += 500  
