#! python2.7
# normalize.py - standard the English name, 
# which uppercases the inital and lowcases the rest.

def normalize(name):
	return name[0].upper() + name[1:].lower()
	
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
