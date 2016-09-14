#!/usr/bin/python
import json
print("Enter the natural of input: ")
in_put = input()

def list_tt (in_put):
	tt = []
	for bit_val in range(2**in_put, 0, -1):
		pattern=[]
		for scale_val in range(in_put, 0, -1):
			if bit_val >2**(scale_val-1):
				bit_val = bit_val-2**(scale_val-1)
				pattern.append(1)
				#print 1
			elif bit_val <= 2**(scale_val-1):
				#print 0
				pattern.append(0)
		tt.append(pattern)
	return tt


if in_put <= 0:
	print("invalid number")
else:
	print list_tt(in_put)

