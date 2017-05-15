import random
import numpy as np
import matplotlib as mp
from sklearn.metrics.pairwise import cosine_similarity
from scipy import sparse
from numpy import dot
from numpy.linalg import norm
import math

dim = [1,10,100,1000]
noOfPoints = 10

def cosineDistance(a,b):
	a = np.asarray(a)
	b = np.asarray(b)
	return dot(a, b)/(norm(a)*norm(b))



def l2Distance(a,b):
	a = np.asarray(a)
	b = np.asarray(b)
	dist = np.linalg.norm(a-b)
	return dist

pointsListxx = []
pointsListyy= []
def maxpossibledist(i):
	for j in range(noOfPoints):
		pointsListx = []
		pointsListy= []
		for i in range(i):
			x = 1
			pointsListx.append(x)
			y = 0
			pointsListy.append(y)
		pointsListxx.append(pointsListx)
		pointsListyy.append(pointsListy)
	print pointsListyy
	#return l2Distance(np.asarray(pointsListxx),np.asarray(pointsListyy))

def frange(x, y, jump):
  while x < y:
    yield x
    x += jump

def CreatePoints(noOfPoints,dim):
	pointsList = []
	#rand = random.sample(list(frange(0,1, 0.00001)),dim)
	#my_randoms= [random.uniform(0.0,1.0) for _ in range (noOfPoints)]
	for j in range(noOfPoints):
		pointsListx = []
		for i in range(dim):
			x = random.random()
			pointsListx.append(x)
		pointsList.append(pointsListx)
	return pointsList
#def FindDistances(pointsList):


def main():
	for i in dim:
		summ = 0
		pointsList = CreatePoints(noOfPoints,i)
		for x in range(len(pointsList)-1):
			l2 = l2Distance(pointsList[x],pointsList[x+1])
			summ = summ + l2
		print 'for dim = ',i,' L2 sum of distance = ',summ
		print 'ratio is', float(summ)/ math.sqrt(i)
		for x in range(len(pointsList)-1):
			cosine = cosineDistance(pointsList[x],pointsList[x+1])
			summ = summ + cosine
		print 'for dim = ',i,' cosine sum of distance = ',summ
		print 'ratio is', float(summ)/ math.sqrt(i)

		


if __name__ == "__main__":
	main()
