import database
import start


def main():
	item = input('Ange artikel du vill lägga till: ')
	print(item)
	database.add_database(item)
	start.main()
	
	
if __name__ == '__main__':
	main()