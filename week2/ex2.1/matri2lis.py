#!/usr/bin/python
##fo1 = open('R9FVAdXW.txt')
##content1 = fo1.readlines() ##it is a list
##print content1
#####print ''.join(content1)
##fo2 = open('list_list.txt', 'w')
##fo2.write("%s" %content1)
##fo1.close()
##fo2.close()

import json
fo1 = open('R9FVAdXW.txt')
content1 = fo1.readlines() ##it is a list
print json.dumps(content1)
fo2 = open('list_list.txt', 'w')
fo2.write("%s" %json.dumps(content1))
fo1.close()
fo2.close()


