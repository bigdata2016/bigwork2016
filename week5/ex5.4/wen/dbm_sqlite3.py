#!/usr/bin/python
# -*- coding: utf-8 -*-
import sqlite3 as sql
import sys

con = sql.connect('northwind.db') #1.make connection
with con:	
	con.text_factory = str
	cur = con.cursor()
	cust_ID = 'ALFKI'			  #not used
	prd_id7 = 7

###Look up the product name by ProductID in Products
	cur.execute("SELECT ProductName FROM Products WHERE ProductID=:Id", {"Id": prd_id7})
	prd_name = cur.fetchone()
	#print prd_name

###Lookup OrderIDs from by ProductID = 7 in 'Order Details'
	cur.execute("SELECT OrderID FROM 'Order Details' WHERE ProductID=:Id", {"Id": prd_id7})
	order_ids = cur.fetchall()
	#for row in order_ids:
	#	for col in row:
	#		print col	
	#print order_id
	
###placeholder lookup the CustomerID with specific OrderIDs in Orders     # Determine how many orders of the "uncle bob"?
	cstm_ids = []
	for row in order_ids:
		for col in row:
			cur.execute("SELECT CustomerID FROM Orders WHERE OrderID=:Id", {"Id": col})
			cstm_id = cur.fetchone()
			print cstm_id[0]
		cstm_ids.append(cstm_id)
	#print cstm_ids

###lookup the ContactName with sepecific CustomerID in Customers
	cont_names = []
	for row in cstm_ids:
		for col in row:
			cur.execute("SELECT ContactName FROM Customers WHERE CustomerID=:Id", {"Id": col})			
			cont_name = cur.fetchone()
			print cont_name[0]
		cont_names.append(cont_name)
	#print cont_names
