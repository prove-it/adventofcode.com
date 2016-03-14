from modules.files import get_file_content
import re

def count_chars(str, chars):
    regexp = r'[' + chars + ']'
    str_vowels = re.findall(regexp, str)

    return len(str_vowels)

def has_repetitions(source_str, substr_len=1, is_separated=False, separator_len=0):
    if not is_separated:
        separator = ''
    elif is_separated and separator_len != 0:
        separator = '\w{'+ str(separator_len) + '}'
    elif is_separated and separator_len == 0:
        separator = '\w*'

    regexp = r'(\w{' + str(substr_len) + '})' + separator + r'\1'
    str_repetitions = re.search(regexp, source_str)

    return bool(str_repetitions)

def has_one_of_subs(source_str, subs):
    regexp = r'(' + '|'.join(subs) + ')'
    subs_in_str = re.search(regexp, source_str)

    return bool(subs_in_str)

def is_nice_string(source_str):
    exceptions = ['ab', 'cd', 'pq', 'xy']
    vowels = 'aeiou'

    if (count_chars(source_str, vowels) >= 3
        and has_repetitions(source_str)
        and not has_one_of_subs(source_str, exceptions)):
        return True
    else:
        return False

def is_nice_string_v2(source_str):
    if (has_repetitions(source_str, 1, True, 1)
        and has_repetitions(source_str, 2, True)):
        return True
    else:
        return False

def count_nice_strings(str_list, cheking_func):
    return sum(1 for source_str in str_list if cheking_func(source_str))


strings = get_file_content('5.txt')
strings_list = strings.split('\n')

print count_nice_strings(strings_list, is_nice_string)
print count_nice_strings(strings_list, is_nice_string_v2)
