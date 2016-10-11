#!/usr/bin/python
from mrjob.job import MRJob
import time			
start_time = time.time()

class MRWordCount(MRJob):

	def mapper(self, key, line):
		yield "chars", len(line)
		yield "words", len(line.split())
		yield "lines", 1

	def reducer(self, key, values):
		yield key, sum(values)

if __name__ == '__main__':
	MRWordCount.run()

print (time.time() - start_time)

