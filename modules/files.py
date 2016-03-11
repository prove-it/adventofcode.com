inputs_dir = 'inputs/'

def get_file_content(file_name):
    f = open('inputs/' + file_name, 'r')
    file_content = f.read()
    f.close()

    return file_content
