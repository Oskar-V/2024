import sys 
if len(sys.argv) < 2:
	print("Please define input file")
	exit()
file_name = sys.argv[1]

with open(file_name) as f:
	d1, d2 = [], []
	counter = {}
	answer = {
		'distance': 0,
		'similarity': 0
	}
	for i in f.readlines():
		a, b = [int(x) for x in i.strip().split('   ')]
		if b not in counter:
			counter[b] = 0
		counter[b] += 1
		d1.append(a)
		d2.append(b)
	d1.sort()
	d2.sort()
	for idx, i in enumerate(d1):
		answer['distance'] += abs(d2[idx] - i)
		answer['similarity'] += i * (counter[i] if i in counter else 0)
	print(answer)