#!/usr/bin/python

import json
import string
import re
with open('pizza-train.json') as f_i:				#file_i = open('pizza-train.json')
	content_str = f_i.read()
	json_dict = json.loads(content_str)			#json_content = json.loads(open('pizza-train.json').read()) s(content_file)
	f_i.close()										#json.dump

symbol = [',', ':', ';', '.',  '"', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '=', '[', ']', '{', '}', '|', '/', '\n', '\\', '\r', '?', '-', '~']#, '\''

def search_kw(j_dict):								#* means dereferencing all value in list or array, no asterisk means the list
	request_txt=[]
	for i in range(len(j_dict)):
		temp=(j_dict[i]['request_text']).lower()	#each text
		for sym in symbol:
			temp = temp.replace(sym,' ')
		request_txt.append(temp)
	return request_txt								# list of request_texts
#print search_kw(json_dict)
kw = search_kw(json_dict)							#
#print len(kw)

def elem_word (lis):								
	unique_word = []
	for elem in lis:
		temp = sorted(elem.split())					# split the words as element to sublist
		unique_word.append(temp)
	return unique_word								# list of lists of word
#print elem_word(kw)
word = elem_word(kw)

def bag_word (lis):									#	classification
	word_set = set(''.join(lis).split()) 			#	join string lists to one list and split in word lists
	word_lis = list(word_set)
	#return sorted(word_lis)
	return sorted(word_lis)
#print bag_word(kw)
bag = bag_word(kw)
#print len(bag)

def record_freq (lis_a, lis_b):
	lis_c = [[0 for col in range(len(lis_b))] for row in range(len(lis_a))]
	for i in range(len(lis_a)):
		for j in range(len(lis_a[i])):
			if lis_a[i][j] in lis_b:
				lis_c[i][j] = 1
			else:
				lis_c[i][j] = 0
	return lis_c 
print record_freq (word, bag)

#with open('record.txt', 'w') as f_o:
#	f_o.write("%s" %record_freq (word, bag))
#	f_o.close()
