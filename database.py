'''
Write to a db
'''

def create_database():
	try:
		db = open('db_file.txt', 'r')
		db.close()
	except IOError:
		db = open('db_file.txt', 'w')
		print('created a database file')
		db.close()

		
def add_database(item):
	db = open('db_file.txt', 'a')
	db = open('db_file.txt', 'a')
	db.write(item + '\n')
	db.close()