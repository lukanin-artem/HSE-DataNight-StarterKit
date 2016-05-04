def test():
	result = 0
	with open("answer.txt", "r") as f:
		result = float(f.read())
	return result > 0.63
