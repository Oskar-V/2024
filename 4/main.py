import sys 
if len(sys.argv) < 2:
	print("Please define input file")
	exit()
file_name = sys.argv[1]

directions = [
	(-1,-1),(0,-1),(1,-1),
	(-1,0)      ,(1,0),
	(-1,1),(0,1),(1,1)
]

valid_words = set()

with open(file_name) as f:
	keyword = "XMAS"
	keyword_counter = 0
	matrix = [x.rstrip() for x in f.readlines()]
	for row_idx, row in enumerate(matrix):
		for col_idx, char in enumerate(row):
			if char == keyword[0]:
				for i in directions:
					y, x = row_idx, col_idx
					current_index = 0
					current_char = char
					tmp = set()
					while True:
						if current_index >= len(keyword):
							keyword_counter+=1
							valid_words.update(tmp)
							break
						if current_char != keyword[current_index]:
							break
						tmp.add((x,y))
						current_index += 1
						x += i[0]
						y += i[1]
						# Add a guard clause to not go out of bounds
						if not (x < 0 or y < 0 or x > len(row)-1 or y > len(matrix)-1):
							current_char = matrix[y][x]
	print(keyword_counter)

	with open(f"./{file_name}-out-{keyword}", "w+") as out_file:
		for y, row in enumerate(matrix):
			for x, char in enumerate(row):
				if (x,y) in valid_words:
					out_file.write(char)
				else:
					out_file.write('.')
			out_file.write("\n")


