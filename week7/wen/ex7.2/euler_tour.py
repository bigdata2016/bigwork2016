#!/usr/bin/python
from mrjob.job import MRJob
from mrjob.step import MRStep
import re
import sys
import time			
WORD_RE = re.compile(r"[\w']+")

class MR_euler_tour(MRJob):

	#map each nodes and set each occurence as 1
	def mapper(self, key, line):
		for elem in line.split():
			yield elem, 1

	#count each nodes occurences and determine the if the graph is a Euler Tour
	#If it checks a node has odd degree and out put reason
	#Else it will check all nodes 			
	def reducer(self, key, values):
		v = [v for v in values]
		if sum(v) % 2 != 0:
			print ("Node%s has odd degree of %d" % (key, sum(v)))
			sys.exit()
		yield key, sum(v)
		del v[:]

##Run MRJob
if __name__ == '__main__':
    MR_euler_tour.run()	
##If program didn't stop it the graph Euler Tour
print "The graph has Euler Tour"

