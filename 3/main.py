from re import finditer
import sys 
if len(sys.argv) < 2:
	print("Please define input file")
	exit()
file_name = sys.argv[1]

pattern = r"mul\((\d{1,3}),(\d{1,3})\)|do(n't)?\(\)"

with open(file_name) as f:
	memory = f.read()
	apply_to_sum = True
	sum = 0
	for i in finditer(pattern, memory):
		a,b,c= i.groups()
		if all(x == None for x in [a,b,c]):
			apply_to_sum = True
		elif c != None:
			apply_to_sum = False
		elif apply_to_sum:
			sum += int(a)*int(b)
			
	print(sum)