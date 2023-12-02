import heapq
import time #libreria para el tiempo

class Graph:
    
    def __init__(self):
        self.vertices = set()
        self.edges = {}
    
    def add_vertex(self, value):
        self.vertices.add(value)
        self.edges[value] = []
    
    def add_edge(self, from_vertex, to_vertex, weight):
        self.edges[from_vertex].append((to_vertex, weight))
    
    def dijkstra(self, start_vertex):
        # Inicializar diccionario de distancias mínimas
        distances = {vertex: float('infinity') for vertex in self.vertices}
        distances[start_vertex] = 0

        # Inicializar cola de prioridad con la tupla (distancia, vértice)
        priority_queue = [(0, start_vertex)]

        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)

            # Verificar si ya se ha encontrado un camino más corto
            if current_distance > distances[current_vertex]:
                continue

            # Explorar los vecinos del vértice actual
            for neighbor, weight in self.edges[current_vertex]:
                distance = current_distance + weight

                # Actualizar la distancia mínima si se encuentra un camino más corto
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances

# Ejemplo de uso

def casoPrueba1():

    print("Caso de prueba 5")

    inicio = time.time()

    graph = Graph()

    # Agregar vértices
    graph.add_vertex("A")
    graph.add_vertex("B")
    graph.add_vertex("C")
    graph.add_vertex("D")
    graph.add_vertex("E")
    graph.add_vertex("F")
    graph.add_vertex("G")
    graph.add_vertex("H")
    graph.add_vertex("I")
    graph.add_vertex("J")

    # Agregar aristas con pesos
    graph.add_edge("A", "D", 4)
    graph.add_edge("A", "C", 3)
    graph.add_edge("A", "B", 8)
    graph.add_edge("B", "E", 3)
    graph.add_edge("B", "F", 2)
    graph.add_edge("C", "F", 4)
    graph.add_edge("D", "G", 9)
    graph.add_edge("D", "H", 1)
    graph.add_edge("E", "I", 8)
    graph.add_edge("F", "I", 7)
    graph.add_edge("F", "J", 6)
    graph.add_edge("G", "J", 9)
    graph.add_edge("H", "J", 8)
    graph.add_edge("I", "J", 1)
    

    # Calcular caminos mínimos desde el vértice "A"
    start_vertex = "A"
    min_distances = graph.dijkstra(start_vertex)
    
    # Mostrar resultados
    for vertex, distance in min_distances.items():
        print(f"Distancia mínima desde {start_vertex} a {vertex}: {distance}")

    fin= time.time()
    tiempo_ejecutado = fin-inicio
    print("tiempo de ejecucion: ",tiempo_ejecutado)



def casoPrueba2():

    print("Caso de prueba 4")

    inicio= time.time()

    graph = Graph()

    # Agregar vértices
    graph.add_vertex("A")
    graph.add_vertex("B")
    graph.add_vertex("C")
    graph.add_vertex("D")
    graph.add_vertex("E")
    graph.add_vertex("F")
    graph.add_vertex("G")
    graph.add_vertex("H")
    graph.add_vertex("I")
    graph.add_vertex("J")

    # Agregar aristas con pesos
    graph.add_edge("A", "D", 9)
    graph.add_edge("A", "C", 8)
    graph.add_edge("A", "B", 7)
    graph.add_edge("B", "E", 6)
    graph.add_edge("B", "F", 2)
    graph.add_edge("C", "F", 1)
    graph.add_edge("D", "G", 2)
    graph.add_edge("D", "H", 1)
    graph.add_edge("E", "I", 6)
    graph.add_edge("F", "I", 8)
    graph.add_edge("F", "J", 9)
    graph.add_edge("G", "J", 7)
    graph.add_edge("H", "J", 4)
    graph.add_edge("I", "J", 2)

    # Calcular caminos mínimos desde el vértice "A"
    start_vertex = "A"
    min_distances = graph.dijkstra(start_vertex)
    

    # Mostrar resultados
    for vertex, distance in min_distances.items():
        print(f"Distancia mínima desde {start_vertex} a {vertex}: {distance}")

    fin= time.time()
    tiempo_ejecutado = fin - inicio
    print("tiempo de ejecucion: ",tiempo_ejecutado)
    
    

casoPrueba1()
print("___________________________________________")
casoPrueba2()
