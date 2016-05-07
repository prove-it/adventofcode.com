from modules.files import get_file_content
import re

class Deer:
    def __init__(self, params):
        self.name = params['name']
        self.run_time = float(params['run_time'])
        self.rest_time = float(params['rest_time'])
        self.speed = float(params['speed'])

class Track:
    def __init__(self, deer):
        self.deer = deer
        self.run_time = deer.run_time
        self.rest_time = 0
        self.distance = 0
        self.extra_points = 0

    def change_state(self):
        if self.run_time > 0:
            self._run()
        else:
            self._rest()

    def _run(self):
        self.run_time -= 1
        self.distance += self.deer.speed

        if self.run_time == 0:
            self.rest_time = self.deer.rest_time

    def _rest(self):
        self.rest_time -= 1

        if self.rest_time == 0:
            self.run_time = self.deer.run_time

    def add_point(self):
        self.extra_points += 1

class Race:
    def __init__(self, time, deers, with_score=False):
        self.time = time
        self.with_score = with_score
        self.tracks = []

        for deer in deers:
            self.tracks.append(Track(deer))

    def start(self):
        for s in xrange(self.time):
            for n, track in enumerate(self.tracks):
                track.change_state()

            if (self.with_score):
               self._change_score()

    def _change_score(self):
        leaders = self._get_leaders()
        for n in leaders:
            self.tracks[n].add_point()

    def _get_leaders(self):
        max_dist = max(self.tracks, key=lambda x: x.distance).distance
        return [n for n, track in enumerate(self.tracks) if track.distance == max_dist]

    def get_the_winner(self):
        if self.with_score:
            func = lambda x: x.distance + x.extra_points
        else:
            func = lambda x: x.distance

        return max(self.tracks, key=func)

deers_text = get_file_content('14.txt')
race_time = 2503

deers = []
pattern = r'(?P<name>\w+).*\b(?P<speed>\d+)\b.*\b(?P<run_time>\d+)\b.*\b(?P<rest_time>\d+)\b'
deers = [Deer(m.groupdict()) for m in re.finditer(pattern, deers_text)]

race = Race(race_time, deers)
race.start()
print race.get_the_winner().distance

race_with_score = Race(race_time, deers, True)
race_with_score.start()
print race_with_score.get_the_winner().extra_points