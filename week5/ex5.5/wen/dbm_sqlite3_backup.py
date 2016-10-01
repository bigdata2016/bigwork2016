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

###Look up the product name by ProductID in 'Products' 
	cur.execute("SELECT ProductName FROM 'Products' WHERE ProductID=:Id", {"Id": prd_id7})
	prd_name = cur.fetchone()
	#print prd_name

###Lookup OrderIDs from by ProductID = 7 in 'Order Details'
	cur.execute("SELECT OrderID FROM 'Order Details' WHERE ProductID=:Id", {"Id": prd_id7})
	order_ids = cur.fetchall()
	#for row in order_ids:
	#	for col in row:
	#		print col	
	#print len(order_ids)
#	print order_ids

###Lookup CustomerIDs Same key value
	cur.execute ("SELECT CustormerID FROM Orders WHERE OrderID, PruductID IN(SELECT OrderID FROM 'Order Details' WHERE ProductID = 7)")
				
	temp = cur.fetchall()
	print temp

