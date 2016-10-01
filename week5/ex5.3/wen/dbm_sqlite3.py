#!/usr/bin/python
# -*- coding: utf-8 -*-
import sqlite3 as sql
import sys

con = sql.connect('northwind.db') #1.make connection
with con:	
	con.text_factory = str
	cur = con.cursor()
	cust_ID = 'ALFKI'
	
####placeholder looup the OrderID with specific CustomerID
	cur.execute("SELECT OrderID FROM Orders WHERE CustomerID=:Id", {"Id": cust_ID})
	order_id = cur.fetchall()													
	for row in order_id:
		for col in row:
			print col	

###lookup the ProductID in 'Order Detaisl'with OrderIDs			#id is integer
	prd_ids=[]
	for row in order_id:
		for col in row:
			cur.execute("SELECT ProductID FROM 'Order Details' WHERE OrderID=:Id", {"Id": col})
			prd_id = cur.fetchone()												#prd_id not clean
			print prd_id[0]														#prd_id[x] = col clean multiple value shafe o
		prd_ids.append(prd_id)	
	#print prd_ids

###lookup the ProductName in Products with ProductIDs
	prd_names=[]
	for row in prd_ids:
		for col in row:
			cur.execute("SELECT ProductName FROM 'Products' WHERE ProductID=:Id", {"Id": col})
			prd_name = cur.fetchone()
			print prd_name[0]
		prd_names.append(prd_name)
	#print prd_names

###lookup the CategoryID in Products with ProductIDs
	cate_ids=[]
	for row in prd_ids:
		for col in row:
			cur.execute("SELECT CategoryID FROM 'Products' WHERE ProductID=:Id", {"Id": col})
			cate_id = cur.fetchone()
			print cate_id[0]
		cate_ids.append(cate_id)
	#print cate_ids

###lookup the CategoryName in Categories with CategoryID
	
	cate_names=[]
	for row in cate_ids:
		for col in row:
			cur.execute("SELECT CategoryName FROM 'Categories' WHERE CategoryID=:Id", {"Id": col})
			cate_name = cur.fetchone()
			print cate_name[0]
		cate_names.append(cate_name)
	#print cate_names



