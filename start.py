import print_menu


def main():

	try:
		with open('db_file.txt') as db:
			pass
	except IOError as e:
		print('ingen databas fil funnen!')
		choise = input('skapa en? j/n: ')
		if choise == 'J' or choise == 'j':
			open('db_file.txt', 'w')
			print('Databasfilen är skapad')
		elif choise == 'N' or choise == 'n':
			pass
		else: 
			print('Ange j eller n')
		
		
	print_menu.main()
	

if __name__ == '__main__':
	main()