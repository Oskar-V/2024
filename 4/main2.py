import sys 
if len(sys.argv) < 2:
	print("Please define input file")
	exit()
file_name = sys.argv[1]

def rotate_matrix(m):
    return [[m[j][i] for j in range(len(m))] for i in range(len(m[0])-1,-1,-1)]

def check_matrix(m,k):
	for idx, i in enumerate(k):
		for jdx, j in enumerate(i):
			if j != " " and j!= m[idx][jdx]:
				return False
	return True

with open(file_name) as f:
	key_matrix = [
		["M"," ","S"],
		[" ","A"," "],
		["M"," ","S"]
	]
	keyword_counter = 0

	matrix = [x.rstrip() for x in f.readlines()]

	for row_idx in range(1,len(matrix)-1):
		for col_idx in range(1,len(matrix[row_idx])-1):
			matches = False
			if matrix[row_idx][col_idx] != key_matrix[1][1]:
				continue
			# Take a 3x3 cut from the matrix with A being in the center
			t = [(x[col_idx-1:col_idx+2]) for x in matrix[row_idx-1:row_idx+2]]

			for _ in range(4):
				key_matrix = rotate_matrix(key_matrix)
				tmp = check_matrix(t, key_matrix)
				if check_matrix(t, key_matrix):
					keyword_counter += 1
					break
				
	print(keyword_counter)