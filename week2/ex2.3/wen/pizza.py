#!/usr/bin/python

import json
with open('pizza-train.json') as file_i:				#file_i = open('pizza-train.json')
	content_string = file_i.read()
	list_dict_json = json.loads(content_string)			#json_content = json.loads(open('pizza-train.json').read()) s(content_file)
	file_i.close()										#json.dump

def search_kw(*list_dict_json):
	request_txt=[]
	for i in range(0, len(list_dict_json)-1, +1):
		request_txt.append(list_dict_json[i]['request_text'])	#request_txt = list_dict_json[0]['request_text']
	return request_txt					#return len(request_txt[0])	#return request_txt[0].split(' ', len(request_txt[0]))

def bag_words(*request_txt):
	word_list=[]
	for i in range(0, len(request_txt)-1, +1):
		uniq_word=[]
		uniq_word=set(request_txt[i].split(' ')
		word_list.append(sorted(uniq_word))
	return word_list						#return set(uniq_word[0]) #return len(uniq_word) #return word_list[0]
	

request_txt=search_kw(*list_dict_json)
#print search_kw(*list_dict_json)
print bag_words(*request_txt)


with open('Bag_of_words.json', 'w') as file_o:
	file_o.write("%s" %json.dumps(bag_words(*request_txt)))
	file_o.close()
	
	

