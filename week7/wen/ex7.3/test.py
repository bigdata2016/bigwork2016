#!/usr/bin/python
from mrjob.job import MRJob
from mrjob.step import MRStep
from mrjob.protocol import JSONValueProtocol
from collections import defaultdict
import re
import sys
import time
start_time = time.time()
##triplet, triad
##globale clustering coefficent 
##C = (3xNo._trian)/(No._connected_triplets_vertices)
##C = (No._closed_triplets)/(No._connected_triplets_vertices)

class MR_triangle(MRJob):
	#OUTPUT_PROTOCOL = JSONValueProtocol
	def steps(self):
		return [MRStep(mapper=self.mapper_e, reducer=self.reducer_e)]
				#MRStep(mapper=self.mapper_v, reducer=self.reducer_v)]#,MRStep(mapper=self.mapper_am, reducer=self.reducer_am)
	
	##mapper	
#	def mapper_n(self, _, line):
#		for node in sorted(line.split()):
#			yield node, 1

	##reducer
#	def reducer_n(self, key, value):
#		yield key, sum(value)

#"0"	4
#"1"	4
#"2"	3
#"3"	2
#"4"	2
#"5"	1



	##map edges
#	def mapper_e(self, _, line):
#		#for each line split and sort
#		e = line.split()
#		#for each node i, j from half adjacency matrix
#		vi = e [0]
#		vj = e [1]
#		yield vi, vj
		#yield vi, 1

	##reduce
#	def reducer_e(self, key, value):
#		vj = [vj for vj in value]
#		yield key, vj

#{"0": "1"}			#d = {e[0]: e[1]}
#{"0": "2"}
#{"0": "3"}
#{"0": "4"}
#{"1": "2"}
#{"1": "4"}
#{"1": "5"}
#{"2": "3"}

#"0"	["1", "2", "3", "4"]
#"1"	["2", "4", "5"]
#"2"	["3"]

#"0"	["['0', '1']", "['0', '2']", "['0', '3']", "['0', '4']"]     e [0]     e = sorted(line.split())
#"1"	["['1', '2']", "['1', '4']", "['1', '5']"]
#"2"	["['2', '3']"]



	##map edges
#	def mapper_e(self, _, line):
#		#for each line split and sort
#		e = sorted(line.split())
#		for vi in line.split():
#		#for each node i, j from half adjacency matrix
#			yield vi, e
		

	##reduce
#	def reducer_e(self, key, value):
#		vi = key
#		ei = [ei for ei in value] 
#		yield vi, ei



#"0"	[["0", "1"], ["0", "2"], ["0", "3"], ["0", "4"]]
#"1"	[["0", "1"], ["1", "2"], ["1", "4"], ["1", "5"]]
#"2"	[["0", "2"], ["1", "2"], ["2", "3"]]
#"3"	[["0", "3"], ["2", "3"]]
#"4"	[["0", "4"], ["1", "4"]]
#"5"	[["1", "5"]]


		##map edges
	def mapper_e(self, _, line):
		#for each line split and sort
		e = sorted(line.split())
		vi = e[0]
		yield vi, e
		

	##reduce
	def reducer_e(self, key, value):
		edge = [edge for edge in value]
		adj_list = defaultdict(lambda: defaultdict(lambda: 0))
		for vi, vj in edge:
			adj_list[vi][vj] += 1
		yield key, adj_list

#"0"	[["0", "1"], ["0", "2"], ["0", "3"], ["0", "4"]]
#"1"	[["1", "2"], ["1", "4"], ["1", "5"]]
#"2"	[["2", "3"]]


#{"0": {"1": 1, "3": 1, "2": 1, "4": 1}}	null
#{"1": {"2": 1, "5": 1, "4": 1}}	null
#{"2": {"3": 1}}	null


	##map edges
#	def mapper_v(self, _, line):
#		#for each line split and sort
#		e = sorted(line.split())
#		vi = e[0]
#		vj = e[1]
#		#for vi in line.split():
#		#for each node i, j from half adjacency matrix
#		yield vi, vj
		

	##reduce
#	def reducer_v(self, key, value):
#		vi = key
#		vj = [vj for vj in value]
#		yield vi, vj


#	def mapper_am(self, key, edge):
#		adjMatrix = [[0 for i in range(key)] for j in range(key)]
#		for i in range(len(edge_u)):
#        	u = edge_u[i]
#        	v = edge_v[i]
#        adjMatrix[u][v] = 1
#
#	def mapper_am(self, key, line):
		


	## map of each number of possible closed edge
	#def mapper_wedge(self, v, occur):
	#	yield v, (occur*(occur-1))/2


if __name__ == '__main__':
    MR_triangle.run()	
print (time.time() - start_time)
