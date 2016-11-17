#!/usr/bin/python
from mrjob.job import MRJob
from mrjob.step import MRStep
import re
import sys
import time
start_time = time.time()

class MR_triangle(MRJob):
		
	def steps(self):
		return [MRStep(mapper=self.mapper_1, reducer=self.reducer_1),##find vjs for each vi
				MRStep(mapper=self.mapper_2, reducer=self.reducer_2),##
				MRStep(mapper=self.mapper_3, reducer=self.reducer_3)]

	def concat(self, input_value):
		lis = []
		for i in input_value:
			lis.append(i)
		return lis
	
	def mapper_1(self, _, line):
		yield line.split()[0],line.split()[1]
		yield line.split()[1],line.split()[0]
	
		
	def reducer_1(self, key, value):
		yield key, self.concat(value)
	
	def mapper_2(self, key, value):
		for vj in value:
			yield sorted((key, vj)), value
	
	def reducer_2(self, key, value):
		yield key, self.concat(value)

	def mapper_3(self, key, value):
		yield None, len(set(value[0]).intersection(value[1]))

	def reducer_3(self, key, value):
		yield "Triangles",sum(value)/3

if __name__ == '__main__':
	MR_triangle.run()	
print (time.time() - start_time)
