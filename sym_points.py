'''
task from Ya interview.
[(x1,y1),(x2,y2),(x3,y3),...]
Find verical line which divide set of points symmetrically
'''

def line(X):
	#make a dict from a list of coordinates
	dct_X = {x[0]:x[1] for x in X}
	
	#seek for min, max x in X
	min_x, max_x = min(dct_X.keys()), max(dct_X.keys())
	
	#get the needed x
	x = min_x + (max_x - min_x)/2
	
	#for each key <x look for a symm key
	answer = True	
	for key, val in dct_X.items():
		if key<x:
			answer = answer and key+2*(x-key) in dct_X.keys() and dct_X[key+2*(x-key)]==val
			if not answer: return False				
			dct_X.pop(key)
			dct_X.pop(key+2*(x-key))
	err=list(filter(lambda key: key>x, dct_X.keys()))
	if err: return False
	return answer, x

def main():
	X = [(1,2), (3,2), (2,0), (2,10), (-5, 5), (9, 5), (2, 3)]
	answer, x = line(X)
	if answer:
		print('Axis of symmetry is x={}'.format(x))
	else: print('There is no vertical axis of symmetry')

if __name__=='__main__':
	main()

