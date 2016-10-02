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

###Lookup CustomerIDs Same key value
	cur.execute("SELECT Products.ProductID, Products.ProductName					\
				 FROM 'Products'													\
				 WHERE Products.ProductName IN(										\
				 	SELECT ProductName FROM 'Products' WHERE ProductID IN( 			\
				 	SELECT DISTINCT ProductID FROM 'Order Details' WHERE OrderID IN(\
				 	SELECT OrderID FROM 'Orders' WHERE CustomerID IN(				\
				 	SELECT CustomerID FROM 'Orders' WHERE OrderID IN 				\
					(SELECT OrderID FROM 'Order Details' WHERE ProductID=7)))))		\
				GROUP BY Products.ProductID")
	temp = cur.fetchall()
	#for row in temp:
	#	for col in row:
	#		print col
 	print len(temp)
	
	

