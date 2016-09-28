#!/usr/bin/python

#import string		

#s = "string. with. Punctuation?s"								# remove punctuations from string
#out = s.translate(string.maketrans("",""), string.punctuation)
#print out

#x = [['a','b'],['c']]			# lists of list to one list
#result = []
#[result.extend(el) for el in x]

#print result

#l = [[1, 2, 3], [4, 5, 6]]		# lists of list to one list
#flattened_l = [item for sublist in l for item in sublist]
#print flattened_l

#a = [6]					# list comprehansion
#b = [6,7,8]
#c = [item for item in b if item in a]
#print c

a = [[2, 3], [1, 2], [4, 7]]
b = [2, 4, 7, 15, 44, 234, 34, 7, 4 ,15]
c = []

#new_a = set(a.split())
#new_b = set(b.split())

#for sublist in a:
	c_elem = []
	for elem in sublist:
		true = '1';
		false = '0';
		if elem in b:
			c_elem.append(true)
		else:
			c_elem.append(false)
	c.append(c_elem)
print c
