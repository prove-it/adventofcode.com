def get_santas_floor(santas_map):
	up_moves = santas_map.count('(')
	down_moves = len(santas_map) - up_moves

	return up_moves - down_moves

def get_basement_index(santas_map):
	current_floor = 0
	basement_index = 0

	for index, direction in enumerate(santas_map):
		current_floor += 1 if direction == '(' else -1

		if current_floor == -1:
			basement_index = index
			break

	return basement_index + 1

santas_map_file = open('inputs/1.txt', 'r')
santas_map = santas_map_file.read()
santas_map_file.close()

print get_santas_floor(santas_map)
print get_basement_index(santas_map)