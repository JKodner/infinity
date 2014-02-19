def inf(mode="+"):
	"""Returns a Generator with an infinite amount of positive or negative numbers.
	Must input '+' to get positive infinity (default) or '-' to get negative infinity."""
	if mode not in ["+", "-"]:
		raise ValueError("Input must be '+' or '-'")
	count = 0
	while True:
		if mode == "+":
			count += 1
		elif mode == "-":
			count -= 1
		yield count
