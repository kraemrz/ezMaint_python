import add_item
import show_items

def print_menu():
	print(30*'-', 'MENY', 30*'-')
	print('1. Skapa ett jobb')
	print('2. Avsluta ett jobb')
	print('3. Skapa en artikel')
	print('4. Visa artiklar')
	print('5. Avsluta')
	print(67*'-')
	
def main():
	loop = True
	while loop:
		print_menu()
		choice = int(input('Ange ditt val [1-5]: '))

		if choice == 1:
			print('du valde nr 1\n')
		elif choice == 2:
			print('Du valde nr 2\n')
		elif choice == 3:
			print('Du valde nr 3\n')
			add_item.main()
		elif choice == 4:
			print('Du valde nr 4\n')
			show_items.main()
		elif choice == 5:
			print('Du valde nr 5\n')
			quit()
		else:
			print('Välj siffra mellan 1-5\n')
			
			
			
if __name__ == '__main__':
	main()