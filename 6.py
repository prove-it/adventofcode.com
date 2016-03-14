from modules.files import get_file_content
import re

class Grid:
    def __init__(self, rows=1000, cols=1000):
        self.rows = rows
        self.cols = cols
        self.grid = [0] * rows

    def make_one_change(self, inst):
        block_width = inst['end'][1] - inst['start'][1] + 1
        right_lights = self.cols - inst['end'][1] - 1

        changer = int('1' * block_width, base=2) << right_lights
        if inst['action'] == 'turn on':
            func = lambda x, changer: x | changer
        elif inst['action'] == 'turn off':
            func = lambda x, changer: x & ~changer
        elif inst['action'] == 'toggle':
            func = lambda x, changer: x ^ changer

        for row in xrange(inst['start'][0], inst['end'][0] + 1):
            self.grid[row] = func(self.grid[row], changer)

    def make_changes(self, inst_list):
        for inst in inst_list:
            self.make_one_change(inst)

    def count_lit_lights(self):
        return ''.join([bin(row) for row in self.grid]).count('1')

class CoolerGrid():
    def __init__(self, rows=1000, cols=1000):
        self.rows = rows
        self.cols = cols
        self.grid = [[0] * cols for x in xrange(rows)]

    def make_one_change(self, inst):
        if inst['action'] == 'turn on':
            changer = 1
        elif inst['action'] == 'turn off':
            changer = -1
        elif inst['action'] == 'toggle':
            changer = 2

        for col in xrange(inst['start'][0], inst['end'][0] + 1):
            for row in xrange(inst['start'][1], inst['end'][1] + 1):
                self.grid[col][row] += changer
                if self.grid[col][row] < 0:
                    self.grid[col][row] = 0

    def make_changes(self, inst_list):
        for inst in inst_list:
            self.make_one_change(inst)

    def total_brightness(self):
        return sum([sum(row) for row in self.grid])

class Instruction:
    def __init__(self, text):
        self.instructions = self._transform_text_to_list(text)

    def _transform_str_to_dict(self, str):
        pattern = r'([\w\s]*)\s(\d{1,3})\,(\d{1,3})\s\w*\s(\d{1,3})\,(\d{1,3})'
        m = re.match(pattern, str)

        return {
                'action': m.group(1),
                'start': [int(m.group(2)), int(m.group(3))],
                'end': [int(m.group(4)), int(m.group(5))]
                }

    def _transform_text_to_list(self, text):
        return [self._transform_str_to_dict(one_str) for one_str in text.split('\n')]


instructions_text = get_file_content('6.txt')
instr = Instruction(instructions_text)

grid = Grid()
grid.make_changes(instr.instructions)
print grid.count_lit_lights()

cooler_grid = CoolerGrid()
cooler_grid.make_changes(instr.instructions)
print cooler_grid.total_brightness()