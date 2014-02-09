#!/usr/bin/python
import MySQLdb

def login(user_email):
	db = MySQLdb.connect(host="us-cdbr-east-05.cleardb.net", # your host, usually localhost
                     user="b54cb4dd444247", # your username
                      passwd="3e31ed0e", # your password
                      db="heroku_2f2035f7b6d3027") # name of the data base
	# you must create a Cursor object. It will let
	#  you execute all the query you need
	cur = db.cursor() 

	# Use all the SQL you like
	sql = "SELECT id FROM users WHERE email = %s"
	args= [user_email]
	cur.execute(sql,args)

	for row in cur.fetchall():
		return {'results': row[0], 'status': 0}
	sql = "INSERT INTO users (email) VALUES (%s)"
	args= [user_email]
	cur.execute(sql,args)
	return {'results': cur.lastrowid, 'status' : 0}


def get_questions():
	db = MySQLdb.connect(host="us-cdbr-east-05.cleardb.net", # your host, usually localhost
                     user="b54cb4dd444247", # your username
                      passwd="3e31ed0e", # your password
                      db="heroku_2f2035f7b6d3027") # name of the data base
	# you must create a Cursor object. It will let
	#  you execute all the query you need
	cur = db.cursor() 
	# Use all the SQL you like
	sql = "SELECT * FROM questions"
	cur.execute(sql)
	results = []
	for row in cur.fetchall():
		results.append({
            		'question_id' : row[0],
                    'question_text': row[1]})
	return {'results': results, 'status': 0}

def get_answers(user_id):
	db = MySQLdb.connect(host="us-cdbr-east-05.cleardb.net", # your host, usually localhost
                     user="b54cb4dd444247", # your username
                      passwd="3e31ed0e", # your password
                      db="heroku_2f2035f7b6d3027") # name of the data base

	questions = get_questions()
	questions = questions['results']
	# you must create a Cursor object. It will let
	#  you execute all the query you need
	cur = db.cursor() 
	# Use all the SQL you like
	sql = "SELECT * FROM answers WHERE user_id = %s"
	args= [user_id]
	cur.execute(sql,args)	
	results = []
	for row in cur.fetchall():
		for v in questions:
		    if v['question_id']==row[1]:
		         question = v['question_text']
		results.append({
			'question_text' : question,
    		'question_id' : row[1],
            'answer_text': row[2]})
	return {'results': results, 'status': 0}

# def set_answer(user_id, question_id, answer_text):
# 	db = MySQLdb.connect(host="us-cdbr-east-05.cleardb.net", # your host, usually localhost
#                      user="b54cb4dd444247", # your username
#                       passwd="3e31ed0e", # your password
#                       db="heroku_2f2035f7b6d3027") # name of the data base
# 	# you must create a Cursor object. It will let
# 	#  you execute all the query you need
# 	cur = db.cursor() 

# 	# Use all the SQL you like
# 	sql = "SELECT * FROM answers WHERE user_id = %s AND question_id = %s AND answer_text = %s"
# 	args= [user_id, question_id, answer_text]
# 	cur.execute(sql,args)
# 	for row in cur.fetchall():
# 		sql = "INSERT INTO answers (user_id, question_id, answer_text) VALUES (%s)"
# 		args= [user_email]
# 		cur.execute(sql,args)
# 		return {'results': row[0], 'status': 0}
# 	sql = "INSERT INTO answers (email) VALUES (%s)"
# 	args= [user_email]
# 	cur.execute(sql,args)
# 	return {'results': cur.lastrowid, 'status' : 0}

