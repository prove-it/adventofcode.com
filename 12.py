from modules.files import get_file_content
import re

json_doc = get_file_content('12.json')

pattern = r'(\-?\d+)'
print sum(map(int, re.findall(pattern, json_doc)))