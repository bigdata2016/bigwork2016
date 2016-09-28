#!/usr/bin/python
#import json

def matrix2list (filename):				#list using array method
	with open(filename) as f:		 			#f = open(filename), which can skip, open(),default read mode, could be iterate
		array = f.readlines()				
		for i in range(len(array)):		  		#iterate the list			
			array[i]=array[i].split() 			#returns a list of all words in string
			for j in range(len(array[i])):
				array[i][j] = int(array[i][j])  #type convert from string to integer
	f.close()
	return array
print matrix2list('R9FVAdXW.txt')

def list2matrix(lis, f_o):
	with open(f_o, 'w') as data_o:
		for i in range(len(lis)):
			for j in range(len(lis[i])):
				line = ""
				matrix = lis[i][j]
				line += str(matrix)
				data_o.write(line + ' ')
			data_o.write('\n')
	data_o.close()
print list2matrix(matrix2list('R9FVAdXW.txt'), 'matrix.txt')
