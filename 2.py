presents_sizes_file = open('inputs/2.txt', 'r')
presents_sizes = presents_sizes_file.read()
presents_sizes_file.close()

def get_list_of_sizes_from_string(str):
	sizes = [[int(dimension) for dimension in one_present.split('x')] for one_present in str.split('\n')]

	return sizes

def get_paper_size_for_one_present(present_dimensions):
	sides = [present_dimensions[0] * present_dimensions[1], present_dimensions[1] * present_dimensions[2], present_dimensions[0] * present_dimensions[2]]
	
	return 2 * sum(sides) + min(sides) 

def get_total_paper_size(presents):
	return sum(get_paper_size_for_one_present(present) for present in presents)

def multiply(numbers):
	return reduce(lambda x, y: x * y, numbers)

def get_ribbon_length_for_one_present(present_dimensions):
	return multiply(present_dimensions) + 2 * (sum(present_dimensions) - max(present_dimensions))

def get_total_ribbon_length(presents):
	return sum(get_ribbon_length_for_one_present(present) for present in presents)

sizes_list = get_list_of_sizes_from_string(presents_sizes)
print get_total_paper_size(sizes_list)
print get_total_ribbon_length(sizes_list)