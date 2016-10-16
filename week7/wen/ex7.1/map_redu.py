#!/usr/bin/python
from mrjob.job import MRJob
from mrjob.step import MRStep
import re
import time			
WORD_RE = re.compile(r"[\w']+")
class MRWordCount(MRJob):

	def mapper(self, key, line):
		for word in WORD_RE.findall(line):
			yield word.lower(), 1

	def reducer(self, key, values):
		yield key, sum(values)
	
if __name__ == '__main__':
	MRWordCount.run()



