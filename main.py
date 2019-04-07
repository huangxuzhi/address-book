from cls import ContactManager
from cls import NotEnoughInfoException
import time

contacts = []
cm = ContactManager(contacts)

choices = {
	1 : 'View the address book',
	2 : 'Add a contact',
	3 : 'Modify a contact',
	4 : 'delete a contact',
	5 : 'search in address book',
	6 : 'Quit'
}
print('\nWelcome! Choose a number to use this program!')

while True:
	time.sleep(2)
	print('\n-----------------------------------------Menu------------------------------------------')
	for choice, desc in choices.items():
		print('\t\t\t\t',choice,'.',desc)
	no = int(input('Your choice:'))
	if no == 1:
		cm.showAllContacts()
		k = input('Press any key to continue:')
		continue
	if no == 2:
		name = input('Name:')
		email = input('Email:')
		address = input('Address:')
		try:
			cm.addContact(name, email, address)
		except NotEnoughInfoException as ex:
			print('Please input one of info below : name or email or address.')
	if no == 3:
		pass
	if no == 6:
		print('Exit now...')
		break
	time.sleep(2)
	print('\nPlease make an another choice')






