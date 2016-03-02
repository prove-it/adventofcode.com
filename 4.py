from hashlib import md5

key = 'yzbqklnj'
start = '00000'
start_len = len(start)

i = 1
while md5(key + str(i)).hexdigest()[:start_len] != start:
    i += 1

print i