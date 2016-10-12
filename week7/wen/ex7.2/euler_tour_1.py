#!/usr/bin/python
from mrjob.job import MRJob
from mrjob.step import MRStep
import re
import sys
import time			
start_time = time.time()
WORD_RE = re.compile(r"[\w']+")

class MR_euler_tour(MRJob):

	## Take each line as a path and count occurencies
	def mapper(self, key, line):
		#for each line in file, yield 1
		#yield line.split(), 1
		#for each element
		for elem in line.split():
			yield elem, 1

	def reducer(self, key, values):
		#if (sum(values)%2 != 0):
		#	print "1"
		#	sys.exit()
		#else: 
		#	print "0"		
		yield key, sum(values)

if __name__ == '__main__':
    MR_euler_tour.run()	


print (time.time() - start_time)

