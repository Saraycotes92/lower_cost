class Station:
    def __init__(self, name, heuristic_cost_to_goal):
        self.name = name
        self.heuristic_cost_to_goal = heuristic_cost_to_goal
        self.adjacencies = []

    def add_adjacency(self, station, travel_cost):
        self.adjacencies.append((station, travel_cost))

class TransportSystem:
    def __init__(self):
        self.stations = {}

    def add_station(self, name, heuristic_cost_to_goal):
        self.stations[name] = Station(name, heuristic_cost_to_goal)

    def connect_stations(self, from_station, to_station, travel_cost):
        self.stations[from_station].add_adjacency(self.stations[to_station], travel_cost)
