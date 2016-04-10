from modules.files import get_file_content
import re
from itertools import permutations
from math import factorial

class Seating:
    def __init__(self, guest_list_t):
        self.guests = set()
        self.happiness_m = {}
        self.seatings = []
        self._build_happiness_matrix(guest_list_t)

    def _build_happiness_matrix(self, guest_list_t):
        pattern = r'(\w+).*(gain|lose)\s(\d+)\s.+\b(\w+)\b\.'
        for str in guest_list_t.split('\n'):
            m = re.findall(pattern, str)[0]
            sign = 1
            if m[1] == 'lose':
                sign = -1
            self.guests.add(m[0])
            self.happiness_m.setdefault(m[0], {})[m[3]] = int(m[2]) * sign

    def calc_happiness(self, seating):
        return sum(map(lambda x, y: self.happiness_m[x][y] + self.happiness_m[y][x], seating, list(seating[1:]) + [seating[0]]))

    def find_seatings(self):
        self.seatings = []

        counter = 0
        max = factorial(len(self.guests) - 1)
        for seating in permutations(self.guests):
            if counter >= max:
                break

            happiness = self.calc_happiness(seating)
            self.seatings.append({'happiness': happiness, 'seating': seating})
            counter += 1

    def get_best_seating(self):
        return max(self.seatings, key=lambda x: x['happiness'])

    def add_me(self):
        my_name = 'I'

        self.happiness_m[my_name] = {}
        for guest in self.guests:
          self.happiness_m[guest][my_name] = 0
          self.happiness_m[my_name][guest] = 0

        self.guests.add(my_name)

guest_list_text = get_file_content('13.txt')

seating = Seating(guest_list_text)
seating.find_seatings()
print seating.get_best_seating()['happiness']

seating.add_me()
seating.find_seatings()
print seating.get_best_seating()['happiness']

