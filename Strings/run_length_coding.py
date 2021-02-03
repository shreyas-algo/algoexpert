# Questions to ask:
# 1. Will all the As or Bs etc be stacked together? - No. eg it can be: "aAaAaaaaaAaaaAAAABbbbBBBB" So simply creating count dict won't work

# 10/15 passing
def runLengthEncoding(string):
    count_map = create_count_map(string)
	print(count_map)
	encoding = []
    for key, value in count_map.items():
		code = find_encoding(key, value)
		encoding.append(code)
	print(encoding)
	return ''.join(encoding)

def create_count_map(string):
	count_map = {}
	for char in string:
		existing_val = count_map.setdefault(char, 0)
		count_map[char] = existing_val + 1
	return count_map

def find_encoding(key, value):
	code = []
	while True:
		# if value is single digit, stop
		if value < 10:
			break
		code.append('9'+key)
		value = value - 9
	if value != 0:
		code.append(str(value)+key)
	print(code)
	return ''.join(code)
