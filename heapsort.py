'''
    ANÁLISIS Y DISEÑO DE ALGORITMOS

    El problema del Zoológico de Cali


    Programa que organiza un espectáculo en un zoológico, donde se
    presentan escenas con animales en orden ascendente según su 
    grandeza. Se busca determinar estadísticas como el animal que 
    participó en más y menos escenas, la escena con menor y mayor 
    grandeza total, y el promedio de grandeza de todo el espectáculo.
    Se apoya en el algoritmo Heapsort.
    

    @Autor:
    - Wilson Andres Mosquera Zapata
    - mosquera.wilson@correounivalle.edu.co
    - 2182116-3743

'''


# Inicializa un objeto Animal con un nombre y una grandeza.
class Animal:
    def __init__(self, nombre, grandeza):
        self.nombre = nombre
        self.grandeza = grandeza

    def __str__(self):
        return f"{self.nombre} ({self.grandeza})"



# Inicializa un objeto Escena con una lista de animales.
class Escena:
    def __init__(self, animales):
        self.animales = ordenar_animales(animales)
        self.grandeza_total = sum(animal.grandeza for animal in self.animales)
        self.max_grandeza_individual = max(animal.grandeza for animal in self.animales)

    def __str__(self):
        return ", ".join(str(animal) for animal in self.animales)

    
# Ordena la lista de animales utilizando el algoritmo Heapsort.
def ordenar_animales(animales):
        def heapify(arr, n, i):
            largest = i
            left = 2 * i + 1
            right = 2 * i + 2

            if left < n and arr[left].grandeza > arr[largest].grandeza:
                largest = left

            if right < n and arr[right].grandeza > arr[largest].grandeza:
                largest = right

            if largest != i:
                arr[i], arr[largest] = arr[largest], arr[i]
                heapify(arr, n, largest)

        n = len(animales)

        for i in range(n // 2 - 1, -1, -1):
            heapify(animales, n, i)

        for i in range(n - 1, 0, -1):
            animales[i], animales[0] = animales[0], animales[i]
            heapify(animales, i, 0)

        return animales

# Ordena la lista de escenas utilizando el algoritmo Heapsort.
def ordenar_escenas(escenas):
        def heapify(arr, n, i):
            largest = i
            left = 2 * i + 1
            right = 2 * i + 2

            if left < n and arr[left].grandeza_total > arr[largest].grandeza_total:
                largest = left

            if right < n and arr[right].grandeza_total > arr[largest].grandeza_total:
                largest = right

            if largest != i:
                arr[i], arr[largest] = arr[largest], arr[i]
                heapify(arr, n, largest)

        n = len(escenas)

        for i in range(n // 2 - 1, -1, -1):
            heapify(escenas, n, i)

        for i in range(n - 1, 0, -1):
            escenas[i], escenas[0] = escenas[0], escenas[i]
            heapify(escenas, i, 0)

        return escenas

# Ordena las escenas por su grandeza_total.
def ordenar_escenas_por_grandeza_total(escenas):
        return sorted(escenas, key=lambda x: x.grandeza_total)

# Inicializa el objeto Solucion
class Solucion:
    def __init__(self, n, m, k, animales, apertura, partes):

        self.n = n
        self.m = m
        self.k = k
        self.animales = animales
        self.apertura = [Escena([animal for animal in escena]) for escena in apertura]
        self.partes = [
            [Escena([animal for animal in partida]) for partida in parte] for parte in partes
        ]


    # Muestra las escenas en la consola.
    def imprimir_escenas(self, escenas):
        for escena in escenas:
            print(escena)


    # Calcula el promedio de las grandezas de todas las escenas en el espectáculo.
    def calcular_promedio_grandezas(self):
        apertura_heap = ordenar_escenas(self.apertura)
        partes_heap = [ordenar_escenas(parte) for parte in self.partes]

        escenas_ordenadas = apertura_heap + sum(partes_heap, [])
        grandeza_total_espectaculo = 0

        for escena in escenas_ordenadas:
            grandeza_total_espectaculo += escena.grandeza_total

        escenas_totales = (self.m - 1) * self.k + self.m

        promedio_grandezas = grandeza_total_espectaculo / escenas_totales

        return promedio_grandezas


    # Ejecuta y muestra la solución del espectáculo, incluyendo el orden de presentación de los animales,
    # estadísticas de participación de animales y características de las escenas.
    def solucion(self):

        apertura_heap = ordenar_escenas(self.apertura)
        partes_heap = [ordenar_escenas(parte) for parte in self.partes]
        print("El orden en el que se debe presentar los animales es:")
        print("Apertura:")
        self.imprimir_escenas(apertura_heap)
        print()

        for i, parte in enumerate(partes_heap, 1):
            print(f"Parte {i}:")
            self.imprimir_escenas(parte)
            print()

        escenas_ordenadas = apertura_heap + sum(partes_heap, [])
        animales_escenas = [
            animal for escena in escenas_ordenadas for animal in escena.animales
        ]

        # Encontrar el animal más participante.
        animales_contador = {}
        for animal in animales_escenas:
            if animal not in animales_contador:
                animales_contador[animal] = 1
            else:
                animales_contador[animal] += 1

        animal_mas_participante = None
        max_participacion = 0
        for animal, participacion in animales_contador.items():
            if participacion > max_participacion:
                animal_mas_participante = animal
                max_participacion = participacion

        # Encontrar el animal menos participante.
        animales_menos_participante = []
        min_participacion = float('inf')
        for animal, participacion in animales_contador.items():
            if participacion < min_participacion:
                animales_menos_participante = [animal]
                min_participacion = participacion
            elif participacion == min_participacion:
                animales_menos_participante.append(animal)

        # Encontrar la escena con la menor grandeza total.
        escena_menor_grandeza = escenas_ordenadas[0]
        for escena in escenas_ordenadas[1:]:
            if escena.grandeza_total < escena_menor_grandeza.grandeza_total:
                escena_menor_grandeza = escena

        # Encontrar la escena con la mayor grandeza total.
        escena_mayor_grandeza = escenas_ordenadas[0]
        for escena in escenas_ordenadas[1:]:
            if escena.grandeza_total > escena_mayor_grandeza.grandeza_total:
                escena_mayor_grandeza = escena

        
        # Obtener las grandezas de los animales.
        grandezas_animales = [animal.grandeza for animal in ANIMALES.values()]

        # Calcular la suma total de grandezas.
        suma_total_grandezas = sum(grandezas_animales)

        # Calcular el promedio de grandezas.
        promedio_grandezas = self.calcular_promedio_grandezas()

        # Imprime la solución en pantalla.
        print(f"Los animales que participaron en más escenas con su respectivo numero de apariciones fueron: {animal_mas_participante} quienes participaron en {max_participacion} escenas cada uno.")

        print(f"Los animales que participaron en menos escenas con su respectivo numero de apariciones fueron: {', '.join(animal.nombre for animal in animales_menos_participante)} quienes participaron en {min_participacion} escenas cada uno")
        
        print("La escena de menor grandeza total fue la escena", escena_menor_grandeza)
        
        print("La escena de mayor grandeza total fue la escena", escena_mayor_grandeza)
        
        print("El promedio de grandeza de todo el espectáculo fue de", promedio_grandezas)



print('Ejemplo 1')
### Parametros de entrada
ANIMALES = {
    "Ciempies": Animal("Ciempies", 1),
    "Libelula": Animal("Libelula", 2),
    "Gato": Animal("Gato", 3),
    "Perro": Animal("Perro", 4),
    "Tapir": Animal("Tapir", 5),
    "Nutria": Animal("Nutria", 6),
}

n = len(ANIMALES)
# Numero de partes
m = 3
# Numero de escenas de cada parte
k = 2

ciempies, libelula, gato, perro, tapir, nutria = ANIMALES.values()


apertura = [
    [tapir, nutria, perro],
    [tapir, perro, gato],
    [ciempies, tapir, gato],
    [gato, ciempies, libelula],
]


parte_1 = [
    [tapir, nutria, perro],
    [ciempies, tapir, gato],
]

parte_2 = [
    [gato, ciempies, libelula],
    [tapir, perro, gato],
]

partes = [apertura, parte_1, parte_2]


espectaculo = Solucion(n, m, k, ANIMALES, apertura, partes)

espectaculo.solucion()

print('\n')


