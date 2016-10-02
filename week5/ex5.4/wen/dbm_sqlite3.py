#!/usr/bin/python
# -*- coding: utf-8 -*-
import sqlite3 as sql
import sys

try:
	con = sql.connect('northwind.db') # connect obj
	con.text_factory = str
	cur	= con.cursor()				  # cursor obj
	prd_id7 = 7
	###Look up the product name by ProductID in Products
	cur.execute("SELECT ProductName FROM Products WHERE ProductID=:Id", {"Id": prd_id7})
	prd_name = cur.fetchone()
	#print prd_name

	cur.execute("SELECT ContactName From 'Customers' WHERE CustomerID IN(				\
				 SELECT CustomerID FROM 'Orders' WHERE OrderID IN( 					\
				 SELECT OrderID FROM 'Order Details' WHERE ProductID=7))")
	temp_prdn = cur.fetchall()
	for row in temp_prdn:
		for col in row:
			print col
	print len(temp_prdn)

except sql.Error, e:
	if con:
		con.rollback()
	print "Error %s:" % e.args[0]
	sys.exit(1)
finally:
	if con:
		con.close()



