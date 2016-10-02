#!/usr/bin/python
# -*- coding: utf-8 -*-
import sqlite3 as sql
import sys

try:
	con = sql.connect('northwind.db') # connect obj
	con.text_factory = str
	cur	= con.cursor()				  # cursor obj

	cur.execute("SELECT ProductName FROM 'Products' WHERE ProductID IN(		\
				 SELECT ProductID FROM 'Order Details' WHERE OrderID IN(	\
				 SELECT OrderID FROM 'Orders' WHERE CustomerID = 'ALFKI'))")
	temp_prdn = cur.fetchall()
	for row in temp_prdn:
		for col in row:
			print col
	print len(temp_prdn)
###lookup orderid			DEBUG INNER JOIN
#	cur.execute("SELECT OrderID FROM 'Orders' WHERE CustomerID = 'ALFKI'")
#	temp_ord = cur.fetchall()
#	for row in temp_ord:
#		for col in row:
#			print col													#output the IDS, clean

#	print temp_ord


except sql.Error, e:
	if con:
		con.rollback()
	print "Error %s:" % e.args[0]
	sys.exit(1)
finally:
	if con:
		con.close()

###Lookup ProductID
#	cur.execute("SELECT ProductID FROM 'Order Details' WHERE OrderID IN(	\
#				SELECT OrderID FROM 'Orders' WHERE CustomerID = 'ALFKI')")
#	temp_prd = cur.fetchall()
#	for row in temp_prd:
#		for col in row:
#			print col			



#	cur.execute("SELECT DISTINCT Products.ProductName FROM Products										\
#				INNER JOIN 'Order Details' ON Products.ProductID = 'Order Details'.ProductID			\
#				INNER JOIN Orders ON 'Order Details'.OrderID = Orders.OrderID 							\
#				WHERE Orders.CustomerID = 'ALFKI'														\
#				UNION																					\
#				SELECT DISTINCT Products.ProductName FROM Products										\
#				LEFT OUTER JOIN 'Order Details' ON Products.ProductID = 'Order Details'.ProductID			\
#				LEFT OUTER JOIN Orders ON 'Order Details'.OrderID = Orders.OrderID 							\
#				WHERE Orders.CustomerID = 'ALFKI'")
#	temp_prd_join = cur.fetchall()
#	print temp_prd_join
#	for row in temp_prd_join:
#		for col in row:
#			print col

