#!/usr/bin/python
import MySQLdb

db = MySQLdb.connect(host="us-cdbr-east-04.cleardb.com", # your host, usually localhost
                     user="bb0a1cc0c68104", # your username
                      passwd="6a7aa761", # your password
                      db="heroku_50dfb2472b04de8") # name of the data base

def get_users():
	# you must create a Cursor object. It will let
	#  you execute all the query you need
	# cur = db.cursor() 

	# # Use all the SQL you like
	# cur.execute("SELECT * FROM users")

	# # print all the first cell of all the rows
	# for row in cur.fetchall() :
	#     return row[0]
	#  
	return 0