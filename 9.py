from modules.files import get_file_content
from itertools import permutations

class Route:
    def __init__(self, cities_text):
        self.cities = set()
        self.distance_m = {}
        self.routes = []

        self._build_distance_matrix(cities_text)

    def _build_distance_matrix(self, cities_text):
        for s in cities_text.split('\n'):
            from_city, _, to_city, _, distance = s.split()
            self.cities.add(from_city)
            self.cities.add(to_city)
            self.distance_m.setdefault(from_city, {})[to_city] = int(distance)
            self.distance_m.setdefault(to_city, {})[from_city] = int(distance)

    def calc_distance(self, route):
        return sum(map(lambda x, y: self.distance_m[x][y], route[:-1], route[1:]))

    def find_routes(self):
        for route in permutations(self.cities):
            dist = self.calc_distance(route)
            self.routes.append({'dist': dist, 'route': route})

    def get_route_extremum(self, func):
        return func(self.routes, key=lambda x: x['dist'])

cities_text = get_file_content('9.txt')

route = Route(cities_text)
route.find_routes()
print route.get_route_extremum(min)['dist']
print route.get_route_extremum(max)['dist']