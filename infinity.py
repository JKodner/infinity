def inf(mode="+", start=0, step=1):
	"""Returns a Generator with an infinite amount of positive or negative numbers.
	There are three parameters that one can input. The first is the positive or negative mode +/-.
	The second is the starting point of the infinity generator.
	The third is the incremtor (step) for the generator."""
	if mode in ["+", "-"]:
		if isinstance(start, int) and isinstance(step, int):
			while True:
				if mode == "+":
					start += step
				elif mode == "-":
					start -= step
				yield start
		else:
			raise ValueError("Start/Step must be integers.")
	else:
		raise ValueError("Input must be '+' or '-'")

