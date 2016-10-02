#!/usr/bin/python
# -*- coding: utf-8 -*-
import sqlite3 as sql
import sys

con = None 			# in case disk is full
try:
	con = sql.connect('northwind.db') # connect obj
	con.text_factory = str
	cur	= con.cursor()				  # cursor obj
	cust_ID = 'ALFKI'


#show all table names
	cur.execute("SELECT NAME FROM sqlite_master WHERE type='table'")	 
	tables = cur.fetchall()											 # output tuples
	for table in tables:											 	 # output tuple by line
#		print table

#show the row of the custormer table - tuples
	cur.execute("SELECT CustomerID FROM 'Customers' LIMIT 5")							 
	cstmID = cur.fetchall()
	for row in cstm:
#		print sublist	

#show customer metadata	
#	cur.execute("PRAGMA table_info(Customers)") 					 #	 
#	data = cur.fetchall()											 #	 #fetchall									 
#	for sublist in data:											 #	 #iterate row in data
#		#print sublist[0], sublist[1], sublist[2] #sublist[0:3]

#show the customer - ALFKI info clean
	cur.execute("SELECT * FROM 'Customers' WHERE CustomerID = 'ALFKI'")	#the row of the custormer's
	row_cstm = cur.fetchall()											#fetchall
	for sublist in row_cstm:											#iterate the row in table
		for col in sublist:												#iterate the col in table
#			print col													#clean print one elem per line

#show the row of the order table - tuples
	cur.execute("SELECT * FROM Orders")							 	#show Orders table
	
	while True:
		row_Order = cur.fetchone()										#fetch single row, print would come with symbol
		if row_Order == None:
			break
#		print row_Order[0]												#if not in row[col]form would print tuple, otherwise clean text 

#show Orders table 
	cur.execute("PRAGMA table_info(Orders)") 					 	 
	data = cur.fetchall()											 	 #fetchall meta 									 
	for sublist in data:											 	 #iterate row in data
#		print sublist[0], sublist[1], sublist[2] 						 #sublist[0:3]

except sql.Error, e:
	print "Error %s:" % e.args[0]
	sys.exit(1)

finally:
	if con:
		con.close()
