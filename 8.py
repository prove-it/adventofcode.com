from modules.files import inputs_dir
import re

def string_in_memory_length(one_str):
    QUOTES = 2
    pattern = r'\\"|\\\\|\\x\w{2}'
    return len(re.sub(pattern, '_', r'' + one_str)) - QUOTES

def escape_string(one_str):
    return '"' + re.escape(one_str) + '"'


answer_1, answer_2 = 0, 0
with open(inputs_dir + '8.txt', 'r') as f:
    for one_string in f:
        one_string = re.sub(r'\n', '', one_string)
        answer_1 += len(one_string) - string_in_memory_length(one_string)
        answer_2 += len(escape_string(one_string)) - len(one_string)
f.close()

print answer_1
print answer_2