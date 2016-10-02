#!/usr/bin/python
# -*- coding: utf-8 -*-
import sqlite3 as sql
import sys

try:
	con = sql.connect('northwind.db') # connect obj
	con.text_factory = str
	cur	= con.cursor()				  # cursor obj
#	cur.execute("SELECT Orders.OrderID,Products.ProductID,ProductName,CategoryID FROM Orders,'Order Details',Products WHERE Orders.OrderID='Order Details'.OrderID AND 'Order Details'.ProductID=Products.ProductID AND Orders.OrderID IN (SELECT Orders.OrderID FROM Orders,'Order Details',Products WHERE Orders.OrderID='Order Details'.OrderID AND 'Order Details'.ProductID=Products.ProductID AND CustomerID='ALFKI' GROUP BY Orders.OrderID HAVING count(CategoryID)>1)")

	cur.execute("SELECT Orders.OrderID,Products.ProductID,ProductName,CategoryID 					\
				 FROM Orders,'Order Details',Products 												\
				 WHERE Orders.OrderID='Order Details'.OrderID AND									\
					  'Order Details'.ProductID=Products.ProductID AND								\
					  Orders.OrderID IN (SELECT Orders.OrderID FROM Orders,'Order Details',Products	\
					  WHERE Orders.OrderID='Order Details'.OrderID AND 								\
							'Order Details'.ProductID=Products.ProductID AND 						\
							CustomerID='ALFKI' 														\
					  		GROUP BY Orders.OrderID 											    \
							HAVING count(CategoryID)>1)")
	temp_prdn = cur.fetchall()
	#for row in temp_prdn:
	#	print row
	#	for col in row:
	#		print col
	print temp_prdn

except sql.Error, e:
	if con:
		con.rollback()
	print "Error %s:" % e.args[0]
	sys.exit(1)
finally:
	if con:
		con.close()

#"SELECT CategoryName FROM 'Categories' WHERE CategoryID IN(\
#SELECT CategoryID FROM 'Products' WHERE ProductName IN(	\
#SELECT ProductName FROM 'Products' WHERE ProductID IN(		\
#SELECT ProductID FROM 'Order Details' WHERE OrderID IN(	\
#SELECT OrderID FROM 'Orders' WHERE CustomerID = 'ALFKI'))))")

