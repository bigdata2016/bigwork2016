#!/usr/bin/python
import sys

##outout the previous_key if the key is true
def output(previous_key, total):
	if previous_key is not None:
		print "%s was found %d times" % (previous_key, total)
##initialize the previous_key and total
previous_key = None
total = 0
##iterate the input
for line in sys.stdin:
	key, value = line.split("\t", 1)
	if key != previous_key:
		output(previous_key, total)
		previous_key = key
		total = 0
	total += int(value)
output(previous_key, total)

