from modules.files import get_file_content

def houses_with_presents(instructions, visited_houses = None):
    moves = {'^': (1, 0), 'v': (-1, 0), '>': (0, 1), '<': (0, -1)}

    if visited_houses is None:
        visited_houses = {'0.0' : 1}
    else:
        visited_houses['0.0'] += 1

    cur_x = 0
    cur_y = 0

    for step in instructions:
        cur_x += moves[step][0]
        cur_y += moves[step][1]

        coordinates = str(cur_x) + '.' + str(cur_y)
        visited_houses[coordinates] = visited_houses.get(coordinates, 0) + 1

    return visited_houses


santas_navigation = get_file_content('3.txt')

#last year
houses = houses_with_presents(santas_navigation)
print len(houses)

#next year
santas_map = santas_navigation[::2]
robosantas_map = santas_navigation[1::2]
santa_houses = houses_with_presents(santas_map)
total_houses = houses_with_presents(robosantas_map, santa_houses)
print len(total_houses)