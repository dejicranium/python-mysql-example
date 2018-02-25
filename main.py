import pymysql, pymysql.cursors

"""
Showing how to connect python to a MySQL database

You need to install pymysql (pip install pymysql), 
which is a convenience library for accessing MySQL databases
"""

def get_database_connection(host, user, password, db, 
	charset='utf8', cursorclass=pymysql.cursors.DictCursor):
	"""Connects to a MySQL database and returns connection instance
	See example.py for usage"""

	conn = pymysql.connect(host=host, user=user, password=password, 
		db=db, charset=charset, cursorclass=cursorclass)
	return conn

