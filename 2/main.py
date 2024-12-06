import sys 
if len(sys.argv) < 2:
	print("Please define input file")
	exit()
file_name = sys.argv[1]

def hasError(x,y):
	return x-y <= 0 or x-y > 3

def detectDirection(val):
	positive = 0
	negative = 0
	no_dif = 0
	for i in range(1, len(val)):
		dif = val[i-1] - val[i]
		if dif == 0:
			no_dif +=1
		elif dif > 0:
			positive += 1
		else:
			negative += 1
	return (positive, negative, no_dif)

with open(file_name) as f:
	answer = {
		'safe_reports': 0,
		'safe_reports_with_dampener': 0
	}
	for line in f.readlines():
		line = [int(x) for x in line.strip().split(' ')]
		if len(line) < 2:
			# Edge case where there are less than 2 values in array
			break

		# Set initial values:
		error_counter = 0
		idx = 1

		# Get all change counters
		a, b, c = detectDirection(line)
		# If array is increasing flip it around so we only have to do one way comparisons
		if b > a:
			line = line[::-1]

		if c > 1:
			is_safe = False
		if a > 1 and b > 1:
			is_safe = False

		# Measure differences
		while error_counter < 2 and idx < len(line)-1:
			x, y, z = line[idx-1:idx+2]

			# Detect errors on both sides:
			errors = [hasError(x,y), hasError(y,z), hasError(x,z)]
			if (errors[0] or errors[1]) and not errors[2]:
				# Remove middle value
				line.pop(idx)
			elif errors[0] and errors[2]:
				# Remove left value
				line.pop(idx-1)
			elif errors[1]:
				# Remove right value
				line.pop(idx+1)
			else:
				idx+=1
				continue
			error_counter +=1
		
		# Decide if the column was safe
		if error_counter < 1:
			answer['safe_reports'] += 1
		if error_counter < 2:
			answer['safe_reports_with_dampener'] += 1
	print(answer)