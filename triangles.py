#! python2.7
# triangles.py - generate a Yang Hui Triangle 

def triangles():
	yield [1]
	out = [1, 1]
	while True:
		yield out
		outPrevious = out[:]
		out = [1, 1]
		for i in range(len(outPrevious)-1):
			out.insert(i+1,outPrevious[i]+outPrevious[i+1])
			
n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break
