from modules.files import get_file_content
import re

class Circuit:
    BITWISE_DICT = {'AND': '&', 'OR': '|', 'LSHIFT': '<<', 'RSHIFT': '>>', 'NOT': '~'}

    def __init__(self, instruction):
        self.inst = instruction
        self._wires = {}
        self.signals = {}

    @staticmethod
    def _replace_text(repl_dict, text):
        pattern = r'\b' + r'\b|\b'.join(repl_dict.keys()) + r'\b'
        return re.sub(pattern, lambda m: str(repl_dict[m.group(0)]), text)

    def compute_signal(self, wire):
        if wire.isdigit():
            return int(wire)
        else:
            if wire not in self.signals:
                self.signals[wire] = eval(self._wires[wire])
            return self.signals[wire]

    def set_wires(self):
        for one_inst in self.inst.split('\n'):
            expr, wire = re.split(r'\s\->\s', one_inst)
            expr = self._replace_text(self.BITWISE_DICT, expr)
            self._wires[wire] = re.sub('([a-z]+)', lambda m: 'self.compute_signal("' + m.group(0) + '")', expr)

instructions_text = get_file_content('7.txt')
circuit = Circuit(instructions_text)
circuit.set_wires()

a = circuit.compute_signal('a')
print a

circuit.signals = {'b': a}
print circuit.compute_signal('a')