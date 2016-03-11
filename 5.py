from modules.files import get_file_content
import re

def count_of_chars(str, chars):
    regexp = r'[' + chars + ']'

    str_vowels = re.findall(regexp, str)

    return len(str_vowels)

def has_repetitions(str):
    regexp = r'(\w)\1+'

    str_repetitions = re.search(regexp, str)

    return bool(str_repetitions)

def has_one_of_subs(str, subs):
    regexp = r'(' + '|'.join(subs) + ')'

    subs_in_str = re.search(regexp, str)

    return bool(subs_in_str)

def is_nice_string(str):
    exceptions = ['ab', 'cd', 'pq', 'xy']
    vowels = 'aeiou'

    if count_of_chars(str, vowels) >= 3 and has_repetitions(str) and not has_one_of_subs(str, exceptions):
        return True
    else:
        return False

def is_nice_string_v2(str):
    pass

def count_nice_strings(str_list, cheking_func):
    return sum(1 for str in str_list if cheking_func(str))

strings = get_file_content('5.txt')

print count_nice_strings(strings.split('\n'), is_nice_string)