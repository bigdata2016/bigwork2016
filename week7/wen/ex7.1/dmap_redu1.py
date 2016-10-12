#!/usr/bin/python
from mrjob.job import MRJob
from mrjob.step import MRStep
import re
import time			
start_time = time.time()



class MRWordCount(MRJob):

	def mapper(self, key, line):
		yield "chars", len(line)
		yield "words", len(line.split())
		yield "lines", 1

	def reducer(self, key, values):
		yield key, sum(values)

	def gen(self, key, line):
		for line in sys.stdin:		
			words = line.split()
			for word in words:
				print "%s\t%d" % (word, 1)
	
if __name__ == '__main__':
	MRWordCount.run()


print (time.time() - start_time)

