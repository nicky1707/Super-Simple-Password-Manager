import sqlite3
import pandas as pd


def store_master(password,name='mas'):
	pack = name,password

	con = sqlite3.Connection("passwords.db")
	cur = con.cursor()
	cur.execute("""
        CREATE TABLE IF NOT EXISTS master
        (name text PRIMARYKEY, pass text)
""")
	cur.execute("""
        INSERT OR IGNORE INTO master values(?,?)""", pack)
	con.commit()
	con.close()

def query_master(query):
	con = sqlite3.Connection("passwords.db")
	cur = con.cursor()
	cur.execute(f"select rowid,* from master where name = '{query}'")
	pas = cur.fetchall()
	tup = pas[0]
	return tup
	# for i in cur.fetchall():
	# 	print(i)
	con.commit()
	con.close()




def store_pass(password):
	con = sqlite3.Connection("passwords.db")
	cur = con.cursor()
	cur.execute("""
        CREATE TABLE IF NOT EXISTS user_pass
        (name text PRIMARYKEY, pass text)
""")
	cur.execute("""
        INSERT OR IGNORE INTO user_pass values(?,?)""",password)
	con.commit()
	con.close()

def query_all():
	con = sqlite3.Connection("passwords.db")
	cur = con.cursor()
	cur.execute("select rowid,* from user_pass")
	pas = cur.fetchall()
	return pas

def query_pass(query):
	con = sqlite3.Connection("passwords.db")
	cur = con.cursor()
	cur.execute(f"select rowid,* from user_pass where name = '{query}'")
	pas = cur.fetchall()
	tup = pas[0]
	return tup
	# for i in cur.fetchall():
	# 	print(i)
	con.commit()
	con.close()

def delete_pass(query):
	con = sqlite3.Connection("passwords.db")
	cur = con.cursor()
	cur.execute(f"delete from user_pass where name = '{query}'")
	# for i in cur.fetchall():
	# 	print(i)
	con.commit()
	con.close()
	

