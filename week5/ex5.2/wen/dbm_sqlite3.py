#!/usr/bin/python
# -*- coding: utf-8 -*-
import sqlite3 as sql
import sys

con = sql.connect('northwind.db') # connect obj
with con:
	con.text_factory = str
	cur	= con.cursor()				  # cursor obj
	cust_ID = 'ALFKI'
	
#show all table names
	#cur.execute("SELECT NAME FROM sqlite_master WHERE type='table'")	 
	#tables = cur.fetchall()											 # output tuples
	#for table in tables:											 	 # output tuple by line
	#	print table

#show customer metadata	
	#cur.execute("PRAGMA table_info(Customers)") 					 	 
	#data = cur.fetchall()											 	 #fetchall									 
	#for sublist in data:											 	 #iterate row in data
		#print sublist[0], sublist[1], sublist[2] #sublist[0:3]

#show the row of the custormer table - tuples
	#cur.execute("SELECT * FROM 'Customers'")							 
	#cstmID = cur.fetchall()
	#for row in cstm:
	#	print sublist	

#show the customer - ALFKI info clean
	#cur.execute("SELECT * FROM 'Customers' WHERE CustomerID = 'ALFKI'")	#the row of the custormer's
	#row_cstm = cur.fetchall()											#fetchall
	#for sublist in row_cstm:											#iterate the row in table
	#	for col in sublist:												#iterate the col in table
	#		print col													#clean print one elem per line

#show the row of the order table - tuples
	#cur.execute("SELECT * FROM Orders")							 	#show Orders table
	#
	#while True:
	#	row_Order = cur.fetchone()										#fetch single row, print would come with symbol
	#	if row_Order == None:
	#		break
	#	print row_Order[0]												#if not in row[col]form would print tuple, otherwise clean text 

#show Orders table 
	#cur.execute("PRAGMA table_info(Orders)") 					 	 
	#data = cur.fetchall()											 	 #fetchall meta 									 
	#for sublist in data:											 	 #iterate row in data
	#	print sublist[0], sublist[1], sublist[2] 						 #sublist[0:3]

####placeholder looup the OrderID with specific CustomerID
	cur.execute("SELECT OrderID FROM Orders WHERE CustomerID=:Id", {"Id": cust_ID})
	# sqlite q : "SELECT OrderID FROM Orders WHERE CustomerID='ALFKI'
	order_id = cur.fetchall()											#one tuple of tuples
	#print order_id														
	#for row in order_id:
	#	for col in row:
	#		print col													#output the IDS, clean

#show the table of 'Order Details' single prduct id
	#cur.execute("SELECT ProductID FROM 'Order Details' WHERE OrderID=11011")
	#prd_id = cur.fetchone()
	#print prd_id
	
#lookup the ProductID with OrderIDs			#id is integer
	prd_ids=[]
	for row in order_id:
		for col in row:
			cur.execute("SELECT ProductID FROM 'Order Details' WHERE OrderID=:Id", {"Id": col})
			prd_id = cur.fetchone()												#prd_id not clean
			print prd_id[0]														#prd_id[x] = col clean multiple value shafe o
		prd_ids.append(prd_id)	
	#print prd_ids

#show Product -single
	#cur.execute("SELECT ProductName FROM 'Products' WHERE ProductID=58")
	#prd_name = cur.fetchone()
	#print prd_name

#show the prductnames datatype, id is integer	
	#cur.execute("PRAGMA table_info(ProductName)") 					 	 
	#data = cur.fetchall()											 	 #fetchall meta 									 
	#for sublist in data:											 	 #iterate row in data
	#	print sublist[0], sublist[1], sublist[2] 						 #sublist[0:3]

###lookup the Products with ProductIDs
	for row in prd_ids:
		for col in row:
			cur.execute("SELECT ProductName FROM 'Products' WHERE ProductID=:Id", {"Id": col})
			prd_name = cur.fetchone()
			print prd_name[0]
		prd_names.append(prd_name)
	#print prd_names
		
