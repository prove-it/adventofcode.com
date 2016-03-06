from hashlib import md5

key = 'yzbqklnj'
start = '000000'

i = 1
while not md5(key + str(i)).hexdigest().startswith(start):
    i += 1

print i