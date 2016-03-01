def get_list_of_sizes_from_string(str):
	sizes = [map(int, one_present.split('x')) for one_present in str.split('\n')]

	return sizes

def get_paper_size_for_one_present(sizes):
	sides = [sizes[0] * sizes[1], sizes[1] * sizes[2], sizes[0] * sizes[2]]
	
	return 2 * sum(sides) + min(sides) 

def get_total_paper_size(presents):
	return sum(get_paper_size_for_one_present(present) for present in presents)

def multiply(numbers):
	return reduce(lambda x, y: x * y, numbers)

def get_ribbon_length_for_one_present(sizes):
	perimeter = 2 * (sum(sizes) - max(sizes))
	bow = multiply(sizes)

	return perimeter + bow

def get_total_ribbon_length(presents):
	return sum(get_ribbon_length_for_one_present(present) for present in presents)

presents_sizes_file = open('inputs/2.txt', 'r')
presents_sizes = presents_sizes_file.read()
presents_sizes_file.close()

sizes_list = get_list_of_sizes_from_string(presents_sizes)
print get_total_paper_size(sizes_list)
print get_total_ribbon_length(sizes_list)