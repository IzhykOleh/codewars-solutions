def faro_cycles(deck_size):
	def shuffle(half1, half2):
		d_shuffled = []
		for x, y in zip(half1, half2):
		    d_shuffled+=[x,y]
		return d_shuffled
	def div_half(d):
		half1 = d[:int(len(d)/2)]
		half2 = d[int(len(d)/2):]
		return half1, half2
	d = list(range(deck_size))
	counter = 0
	d_shuffled = d[:]
	while not (d_shuffled == d and counter != 0):
		d_shuffled = shuffle(*div_half(d_shuffled))
		counter+=1
	return counter
