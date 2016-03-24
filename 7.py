from modules.files import get_file_content
import re

class Circuit:
    BITWISE_DICT = {'AND': '&', 'OR': '|', 'LSHIFT': '<<', 'RSHIFT': '>>', 'NOT': '~'}

    def __init__(self, instruction):
        self.inst = instruction

    @staticmethod
    def _replace_text(repl_dict, text):
        pattern = r'\b' + r'\b|\b'.join(repl_dict.keys()) + r'\b'
        return re.sub(pattern, lambda m: str(repl_dict[m.group(0)]), text)

    def _get_computable_wires(self, text):
        pattern = r'^((?:[\-\d]*)?\s?(?:' + '|'.join(self.BITWISE_DICT.keys()) + r')?\s?(?:[\-\d]*))\s\->\s([a-z]+)$'
        return {wire: value for value, wire in re.findall(pattern, text, re.MULTILINE)}

    def _replace_bitwise_ops(self, text):
        return self._replace_text(self.BITWISE_DICT, text)

    def _replace_computed_wires(self, wires, text):
        return self._replace_text(wires, text)

    def override_wire(self, wire, new_expr):
        pattern = r'(.*)(?=\s\->\s\b' + wire + r'\b)'
        self.inst = re.sub(pattern, str(new_expr), self.inst)

    def find_wire_signal(self, searched_wire):
        inst = self.inst

        while True:
            cur_wires = self._get_computable_wires(inst)

            for wire, expr in cur_wires.iteritems():
                cur_wires[wire] = eval(self._replace_bitwise_ops(expr))
                if wire == searched_wire:
                    return cur_wires[wire]

            inst = self._replace_computed_wires(cur_wires, inst)


instructions_text = get_file_content('7.txt')
circuit = Circuit(instructions_text)

a = circuit.find_wire_signal('a')
print a

circuit.override_wire('b', a)
print circuit.find_wire_signal('a')
