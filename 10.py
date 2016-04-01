import re

def look_and_say(number, iterations):
    for i in xrange(iterations):
        pattern = r'(\d)\1*'
        number = re.sub(pattern, lambda m: str(len(m.group(0))) + str(m.group(0)[0]), number)

    return number

number = '1321131112'
print len(look_and_say(number, 40))
print len(look_and_say(number, 50))