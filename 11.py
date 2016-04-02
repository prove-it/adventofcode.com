import re

def first_rule(password):
    pattern = r'(abc|bcd|cde|def|efg|fgh|ghi|hij|ijk|jkl|klm|lmn|mno|nop|opq|pqr|qrs|rst|stu|tuv|uvw|vwx|wxy|xyz)'
    return bool(re.findall(pattern, password))

def second_rule(password):
    pattern = r'i|o|l'
    return not bool(re.findall(pattern, password))

def third_rule(password):
    pattern = r'(\w)\1'
    return len(re.findall(pattern, password)) >= 2

def is_valid(password):
    return second_rule(password) & third_rule(password) & first_rule(password)

def increase_password(password):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    cur_letter = password[-1:]
    next_index = alphabet.index(cur_letter) + 1
    if next_index < len(alphabet):
        return password[:-1] + alphabet[next_index]
    else:
        return increase_password(password[:-1]) + alphabet[0]

def generate_new_password(old_password):
    new_password = increase_password(old_password)
    while not is_valid(new_password):
        new_password = increase_password(new_password)

    return new_password


old_password = 'cqjxjnds'
new_password = generate_new_password(old_password)
print new_password

old_password = new_password
print generate_new_password(old_password)