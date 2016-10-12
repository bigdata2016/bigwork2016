#!/usr/bin/python
from mrjob.job import MRJob
from mrjob.step import MRStep
import re

WORD_RE = re.compile(r"[\w']+")

#The class is to find euler tour
class MR_euler_tour(MRJob):
	
	##
	def steps(self):
		return [MRStep(mapper = self.mapper_nodes_edge),
				MRStep(mapper = self.mapper_paths, 
					   combiner = self.combiner_paths,
					   reducer = self.reducer_paths)]

	## get the first line of each file
	#def mapper_nodes_edge(self, _, line):

	## map each line as a key path and give 1 as value
	def mapper_paths(self, _, line):
		
	## combine all mapped key, count the how many value of each key has
	##count each line 
	def combiner_paths(self, word, counts):
		
	## analise each value of key, which if the value is even or odd
	def reducer_paths(self, word, counts):
		
#run the class
if __name__ == '__main__':
	MR_euler_tour.run()
