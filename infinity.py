def inf(mode="+", start=0):
	"""Returns a Generator with an infinite amount of positive or negative numbers.
	There are two parameters that one can input. The first is the positive or negative mode +/-.
	The second is the starting point of the infinity generator."""
	if mode not in ["+", "-"]:
		raise ValueError("Input must be '+' or '-'")
	while True:
		if mode == "+":
			start += 1
		elif mode == "-":
			start -= 1
		yield start
