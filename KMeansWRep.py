import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import random
import math

n_clusters=2
n_representative = 4


def L1Distance(a,b):
	sum = 0
	if len(a) != len(b):
		sum = 100
	else:
		for x in range(len(a)):
			sum = sum + abs(a[x] - b[x])
	return sum

def calculateDistance():
	for i in range(n_clusters):
		count = 1
		listt =[]
		for item in pointsLabel:
			if item[0] == i:
				count = count + 1
				listt.append([item[1],item[2],item[3]])
		summ = 0
		for x in range(len(listt)-1):
			l2 = L1Distance(listt[x],listt[x+1])
			summ = summ + l2
		avg = float(summ)/count
		print 'the avg sum for cluster ',i,',the sum is',summ , 'no of points',count

def KMedian(n_clusters):
	return



pointsLabel = []
def getlabel(point):
	min_dist = 100
	min_label = 100
	count = 0
	for i in sampleArray:
		#dist = L1Distance(point[:,[1, 2, 3]],i[:,[0, 1, 2]])
		dist = L1Distance([point[1],point[2],point[3]],[i[0],i[1],i[2]])
		if dist < min_dist:
			min_dist = dist
			min_label = i[3]
		print min_dist,min_label
	pointsLabel.append([min_label,point[1],point[2],point[3]])
	return min_label
		
data = np.genfromtxt('3D_spatial_network.txt', delimiter=',')

#data = np.genfromtxt('3D_spatial_network.txt', delimiter=',',skip_header=1)
#travian = np.delete(data, np.s_[::1], 1)
sample = random.sample(data[:, [1, 2, 3]],int(2*math.ceil(math.sqrt(len(data)))))

X = np.asarray(sample)

#kmeans = KMeans(n_clusters)

kmeans = KMeans(n_clusters,n_init = 2)
kmeans.fit(X)

kmedian = KMedian(n_clusters)

centroids = kmeans.cluster_centers_
labels = kmeans.labels_


sam = []
for i in range(len(X)):
	a = np.array([])
	a = np.append(X[i],labels[i])
	sam.append(a)
	#sampleArray.append(np.append(X[i],labels[i]))
    #print("point:",X[i], "label:", labels[i])

#representative points 
sampleArray = []
for i in range(n_clusters):
	x = []
	for label in sam:
		if(label[3] == i):
			x.append(label)
	rep_points = random.sample(x,n_representative)
	for x in rep_points:
		sampleArray.append(x)

print sampleArray
file = open('output.txt','a')
count1 = 0
for i in range(len(data)):
	count1 = count1+1
	getlabel(data[i])
    #print("point:",data[i], "label:", getlabel(data[i]))
    #file.write(str(("point:",data[i], "label:", getlabel(data[i]))))
calculateDistance()

