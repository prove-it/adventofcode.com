from modules.files import get_file_content

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

santas_map = get_file_content('1.txt')

print get_santas_floor(santas_map)
print get_basement_index(santas_map)