import start


def main():
	db = open('db_file.txt', 'r')
	for line in db:
		print(line)
		
	db.close()
	
	start.main()
	
	
if __name__ == '__main__':
	main()