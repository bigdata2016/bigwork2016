#!/usr/bin/python
from mrjob.job import MRJob
import re
import time
start_time = time.time()
WORD_RE = re.compile(r"[\w']+")

class Count_triangles(MRJob):
	def steps(self):
		return[
			self.mr(mapper=self.mapper_1,
					reducer=self.reducer_1),
			self.mr(mapper= self.mapper_2,
					reducer=self.reducer_2),
			self.mr(mapper=self.mapper_3,
					reducer=self.recuder_3),
			self.mr(mapper=self.mapper_div_duplicate),
		]

	def mapper_1(self, _, line):
		yield line.split()[0],line.split()[1]
		yield line.split()[1],line.split()[0]
	
	def reducer_1(self, key, value):
		yield key, self.concatenate(value)

	def mapper_2(self, key, value):
		for element in value:
			yield (min(key, element),max(key, element)), value

	def reducer_2(self, key, value):
		yield key, self.concatenate(value)

	def mapper_3(self, key, value):
		yield None, len(self.concatenate(set(value[0]).intersection(value[1])))

	def recuder_3(self, key, value):
		yield 'Total Number of Tirangle:', sum(value)

	def mapper_div_duplicate(self, key, value):
		yield 'Total Number of Tirangle: ', value/3

	def concatenate(self, input_value):
		concatenate_list = []
		for i in input_value:
			concatenate_list.append(i)
		return concatenate_list


if __name__ == '__main__':
	Count_triangles.run()
print (time.time() - start_time)
