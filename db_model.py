#!/usr/bin/python
import MySQLdb

def connect():
	db = MySQLdb.connect(host="us-cdbr-east-05.cleardb.net", # your host, usually localhost
                     user="b54cb4dd444247", # your username
                      passwd="3e31ed0e", # your password
                      db="heroku_2f2035f7b6d3027") # name of the data base
	return db

def login(fb_id):
	db = connect()
	cur = db.cursor() 

	# Use all the SQL you like
	sql = "SELECT id FROM users WHERE fb_id = %s"
	args = [fb_id]
	cur.execute(sql,args)

	for row in cur.fetchall():
		return {'results': row[0], 'status': 0}
	sql = "INSERT INTO users (fb_id) VALUES (%s)"
	args= [fb_id]
	cur.execute(sql,args)
	db.commit()
	return {'results': cur.lastrowid, 'status' : 0}

# def login(user_email):
# 	db = connect()
# 	# you must create a Cursor object. It will let
# 	#  you execute all the query you need
# 	cur = db.cursor() 

# 	# Use all the SQL you like
# 	sql = "SELECT id FROM users WHERE email = %s"
# 	args= [user_email]
# 	cur.execute(sql,args)

# 	for row in cur.fetchall():
# 		return {'results': row[0], 'status': 0}
# 	sql = "INSERT INTO users (email) VALUES (%s)"
# 	args= [user_email]
# 	cur.execute(sql,args)
# 	db.commit()
# 	return {'results': cur.lastrowid, 'status' : 0}

def get_questions():
	db = connect()
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
	db = connect()
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

def get_answers_fb_id(fb_id):
	db = connect()
	questions = get_questions()
	questions = questions['results']
	cur = db.cursor() 
	sql = "SELECT * FROM answers a INNER JOIN users u ON u.id = a.user_id AND u.fb_id = %s" 
	args= [fb_id]
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


def get_questions_without_answer(user_id):
	db = connect()
	# you must create a Cursor object. It will let
	#  you execute all the query you need
	cur = db.cursor() 
	# Use all the SQL you like
	sql = "SELECT * From questions WHERE questions.id NOT IN (SELECT question_id from answers WHERE questions.id = question_id AND user_id = %s);"
	args= [user_id]
	cur.execute(sql,args)	
	results = []
	for row in cur.fetchall():
		results.append({
			'question_id' : row[0],
    		'question_text' : row[1]})
	return {'results': results, 'status': 0}



def set_answer(user_id, question_id, answer_text):
	db = connect()
	# you must create a Cursor object. It will let
	#  you execute all the query you need
	cur = db.cursor() 
	sql = "SELECT * FROM answers WHERE user_id = %s AND question_id = %s"
	args= [user_id, question_id]
	cur.execute(sql,args)
	for row in cur.fetchall():
		sql = "UPDATE answers SET answer_text = %s WHERE user_id = %s AND question_id = %s"
		args= [answer_text, user_id, question_id]
		cur.execute(sql,args)
		db.commit()
		return {'status': 2}
	sql = "INSERT INTO answers (user_id, question_id, answer_text) VALUES (%s, %s, %s)"
	args= [user_id, question_id, answer_text]
	cur.execute(sql,args)
	db.commit()
	for row in cur.fetchall():
		return {'results': cur.lastrowid, 'status' : 0}
	return {'status': 1}

def delete_answer(user_id, question_id):
	db = connect()
	# you must create a Cursor object. It will let
	#  you execute all the query you need
	cur = db.cursor() 
	sql = "DELETE FROM answers WHERE user_id = %s AND question_id = %s"
	args= [user_id, question_id]
	cur.execute(sql,args)
	db.commit()

	# TODO: check if actually deleted
	return {'status': 1}

