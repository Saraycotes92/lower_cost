from transport_system import TransportSystem
import heapq

def a_star_search(transport_system, start, goal):
    open_list = []
    heapq.heappush(open_list, (0 + transport_system.stations[start].heuristic_cost_to_goal, 0, start, [start]))
    visited = set()

    while open_list:
        _, cost, current, path = heapq.heappop(open_list)

        if current in visited:
            continue

        visited.add(current)

        if current == goal:
            return path, cost

        for adjacency, travel_cost in transport_system.stations[current].adjacencies:
            if adjacency.name not in visited:
                total_cost = cost + travel_cost
                heuristic_cost = total_cost + adjacency.heuristic_cost_to_goal
                heapq.heappush(open_list, (heuristic_cost, total_cost, adjacency.name, path + [adjacency.name]))

    return [], 0

if __name__ == "__main__":
    # Crear el sistema de transporte
    system = TransportSystem()
    system.add_station('A', heuristic_cost_to_goal=10)
    system.add_station('B', heuristic_cost_to_goal=5)
    system.add_station('C', heuristic_cost_to_goal=0)  # C es el objetivo

    # Conectar estaciones
    system.connect_stations('A', 'B', 5)
    system.connect_stations('B', 'C', 3)

    # Encontrar la mejor ruta de A a C
    route, cost = a_star_search(system, 'A', 'C')
    print(f"La mejor ruta es: {route} con un costo de: {cost}")
