#!/usr/bin/python

import pickle as pk
from sklearn.metrics import jaccard_similarity_score
f=open('E:/repo/bigwork2016/week4/test_files/data_1000points_1000dims.dat','rb')
mat=pk.load(f,encoding='latin1')
num=mat.shape[0]
points=[]
for i in range(num):
	points.append(mat.getrow(i).todense())
status=[0 for i in range(num)]

def Jaccard_Distance(point1, point2):
	index=jaccard_similarity_score(point1,point2)
	distance=1-index
	return distance

def Region_Query(current_point, eps):
	temp=[]
	for i in range(num):
		if Jaccard_Distance(current_point, points[i])<=eps:
			temp.append(i)
	return temp

def Expand_Cluster(pt, neighbor, cluster, eps, Minpts):
	status[pt]=cluster
	for newpt in neighbor:
		if status[newpt]==0:
			new_neighbor=Region_Query(points[newpt], eps)
			if len(new_neighbor)>=Minpts:
				neighbor.extend(new_neighbor)
		if status[newpt]<=0:
			status[newpt]=cluster

def DBSCAN(eps, Minpts):
    C=0
    for i in range(num):
        if status[i]!=0:
            continue
        NeighborPts=Region_Query(points[i], eps)
        if len(NeighborPts)<Minpts:
            status[i]=-1
        else:
            C=C+1
            Expand_Cluster(i, NeighborPts, C, eps, Minpts)

DBSCAN(0.15, 2)
num_cluster=max(status)+1
print ("There are %d clusters." %(num_cluster))