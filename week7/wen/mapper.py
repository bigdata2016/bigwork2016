#!/usr/bin/python

##import sys library
import sys


##iterate the stdi strings 
for line in sys.stdin:		
	words = line.split()
	for word in words:
		print "%s\t%d" % (word, 1)

#import time			
#start_time = time.time()

#def mapper(fn): 
#	with open(fn) as f:
#		array = f.readlines()
#		for line in array:		
#			words = line.split()
#			for word in words:
#				print "%s\t%d" % (word, 1)
#	f.close()
#mapper('news.txt')
#print (time.time() - start_time)


