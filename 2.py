from modules.files import get_file_content

def get_list_of_sizes_from_string(str):
	sizes = [map(int, one_present.split('x')) for one_present in str.split('\n')]

	return sizes

def paper_size_for_one_present(sizes):
	sides = [sizes[0] * sizes[1], sizes[1] * sizes[2], sizes[0] * sizes[2]]
	
	return 2 * sum(sides) + min(sides)

def total_paper_size(presents):
	return sum(paper_size_for_one_present(present) for present in presents)

def multiply(numbers):
	return reduce(lambda x, y: x * y, numbers)

def ribbon_length_for_one_present(sizes):
	smallest_perimeter = 2 * (sum(sizes) - max(sizes))
	bow = multiply(sizes)

	return smallest_perimeter + bow

def total_ribbon_length(presents):
	return sum(ribbon_length_for_one_present(present) for present in presents)


presents_sizes = get_file_content('2.txt');

sizes_list = get_list_of_sizes_from_string(presents_sizes)
print total_paper_size(sizes_list)
print total_ribbon_length(sizes_list)