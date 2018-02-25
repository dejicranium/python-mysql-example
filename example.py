from .main import get_database_connection


#connect to the database and get instance
connection = get_database_connection('host', 'usernamehere', 'password', 'dbname')


#(this example depends on pymysql so you have to write raw SQL. Shouldn't be a problem if you know SQL)
try:
	#trying to get a column named 'column' from a table called 'table', for example
	with connection.cursor() as cursor:
		cursor.execute("SELECT 'column' FROM 'table'")
		result = cursor.fetchone() #fetch one record from the column

		#or you can get all records from column (this will return a list)  
		results = cursor.fetchall()

		#since 'results' is a list, you can iterate through it and do something
		#in this example, I'll add the word 'tessa' to each record in the column and append it to a list
		#just to show how data can be manipulated
		for row in results: 
			lst_of_records_with_tessa = []
			new_row = "{} tessa".format(row)
			lst_of_records_with_tessa.append(new_row)
finally: 
	connection.close()


#for more info on how to carry out other operations, go to https://pymysql.readthedocs.io/en/latest/
