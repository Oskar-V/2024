from functools import cmp_to_key
import sys 
if len(sys.argv) < 2:
	print("Please define input file")
	exit()
file_name = sys.argv[1]

with open(file_name) as f:
	answer = {
		"correct_middle_sum":0,
		"corrected_middle_sum": 0
	}
	data = [x.rstrip() for x in f.readlines()]
	rules = {}
	for rule in data[:data.index("")]:
		a, b = rule.split('|')
		if a in rules:
			rules[a] += [b]
		else:
			rules[a] = [b]
	pages = [x.split(',') for x in data[data.index("")+1:]]
	incorrect_pages = []

	for release in pages:
		is_correct = True
		for page_idx, page_number in enumerate(release):
			if page_number in rules:
				for x in rules[page_number]:
					if x in release[:page_idx]:
						is_correct = False
						break
		if is_correct:
			answer["correct_middle_sum"] +=int(release[int(len(release)/2)])
		else:
			incorrect_pages.append(release)

	def compare(a, b):
		if a not in rules:
			return 0
		return -1 if b in rules[a] else 1

	## Correct the invalid releases
	for release in incorrect_pages:
		release.sort(key=cmp_to_key(compare))
		answer["corrected_middle_sum"] +=int(release[int(len(release)/2)])
	print(answer)