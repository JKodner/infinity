def inf(mode="+", start=0, step=1):
	"""Returns a Generator with an infinite amount of positive or negative numbers.
	
	There are three parameters that one can input. 
	The first is the positive or negative mode +/-.
	The second is the starting point of the infinity generator.
	The third is the incremtor (step) for the generator."""
	if mode in ["+", "-"]:
		if isinstance(start, (int, float)) and isinstance(step, (int, float)):
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

def fibonacci(mode="+", start=1):
	"""Returns a Generator with incrementing fibonacci values.

	There are three parameters that one can input:
	The 'mode' parameter: Input '+'/'-' for whether you want positive or negative values.
	The 'start' parameter: Input an integer which is the starting point of the values.
	"""
	if mode in ["+", "-"]:
		if isinstance(start, (int, float)):
			if mode == "+":
				lst = [0, start]
			elif mode == "-":
				lst = [-start, 0]
			count = 1
			while True:
				current = lst[count]
				previous = lst[count - 1]
				next = current + previous
				lst.append(next)
				count += 1
				yield next
		else:
			raise ValueError("'start' value must be an integer.")
	else:
		raise ValueError("'mode' input must be '+' or '-'")