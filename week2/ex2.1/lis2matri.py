#!/usr/bin/python
fo1 = open('R9FVAdXW.txt')
content1 = fo1.readlines() ##it is a list
matrix = ''.join(content1)
print matrix 
fo2 = open('list_matrix.txt', 'w')
fo2.write("%s" %matrix)
fo1.close()
fo2.close()
