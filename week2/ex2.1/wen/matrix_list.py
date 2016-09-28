#!/usr/bin/python
#import json	
##fo1 = open('R9FVAdXW.txt')		 #open the file to read

##content1 = fo1.readlines()		 #read until EOF, returns a list, containing \r\n
##content1 = fo1.read()				 #reads at most (size) bytes

##matrix = ''.join(content1)		 #returns a string joins all string with ''
##s = json.dumps(content1)			 #dump the data in json type

##print matrix
##print json.loads(s)				 #load the json data

##fo2 = open('list_matrix.txt', 'w') #open a file to write

#fo2.write("%s" %matrix)			 #write string
#fo2.write("%s" %json.loads(s))      #write json type string

#fo1.close()						 #always close read file in the end
#fo2.close()						 #close write file

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

def lis2mat(filename, lis=[[]]):
	f = open(filename,'w')
	tmp=[]
	for i in range(len(lis)):
		for j in range(len(lis[i])-1):
			tmp.append(str(lis[i][j])+' ')
		tmp.append(str(lis[i][len(lis[i])-1])+'\n')
	f.writelines(tmp)
	f.close()
lis2mat('newfile.txt',mat2lis('R9FVAdXW.txt'))

